## ORDER of OPERATIONS
# 1 Run Processing times tables.
# 2 Run Running Playlist tables.

import MySQLdb
import MySQLdb.cursors
import imp, os
from django.core.management import setup_environ
path = '/home/amosbrown/pydev/pwadio/pwadio'
f, filename, desc = imp.find_module('settings', [path])
project = imp.load_module('settings', f, filename, desc)
setup_environ(project)

# Add django project to sys.path
import sys
sys.path.append(os.path.abspath(os.path.join(path, os.path.pardir)))
from django.db import models
import logging
import itunes

from pwadio_be_2.models import RunningPlaylist, RadioStation, ItunesTrackInfo, Artist, Track, ProcessingTime, Album, MusicServices, MusicServices_Artist_Lookup, MusicServices_Track_Lookup

conn = MySQLdb.connect(host="localhost", user="root", passwd="password", db="pwadio_2013", compress=1, cursorclass=MySQLdb.cursors.DictCursor)
cursor = conn.cursor()

### Grab data from pwadio_2013.pwadio_be_runningplaylist and convert it to the format in use in pwadio_2013.pwadio_be_2_runningplaylist.
table_name = "pwadio_be_runningplaylist"
cursor.execute("select Unique_ID, date_added, time_played, artist_name_text, track_name_text, artist, track from " + table_name + " order by id limit 10")

rows = cursor.fetchall()
rows_added = 0

for row in rows:
    print row['Unique_ID'], row['date_added'], row['time_played'], row['artist_name_text'], row['track_name_text'], row['artist'], row['track']
    pt = ProcessingTime.objects.get(pk=1)   
    rs = RadioStation.objects.get(pk=1)
    ra = Artist.objects.get(pk=1)
    rt = Track.objects.get(pk=1)
    try:
        check_rp = RunningPlaylist.objects.get(Unique_ID=row['Unique_ID'])
    except:
	check_rp = None
    if not check_rp:
        logging.warning("[check_rp]: is None, add this row to the new database - Unique_ID: " + row['Unique_ID'])
	try:
	    logging.warning("ARTIST name from radio station: [" + row['artist_name_text']+ "].")
            check_for_artist = Artist.objects.get(name__iexact=""+row['artist_name_text']+"")
	    logging.warning("Checking local ARTIST table by name: [" + check_for_artist.name + "].")
            if check_for_artist:
                ra = check_for_artist
	        logging.warning("ARTIST exists in table, setting current ARTIST to existing ARTIST from table.")
            else:
                #add_artist = Artist.objects.create(name=item['artist_name_text'])
                #item['artist'] = add_artist 
		logging.warning("<><><><><><><><><><><><><><><> strange race condition here.")	
        except:
            #print "Error %d: %s" % (e.args[0], e.args[1])
	    try:
		add_artist = Artist.objects.create(name=row['artist_name_text'], date_added=row['date_added'])
                ra = add_artist 
		logging.warning("ARTIST doesn't exist in table, creating new ARTIST and setting current ARTIST to new ARTIST.")	
	    except:
	        logging.warning("Something failed with grabbing or creating an ARTIST, setting to default ARTIST.")
	        ra = Artist.objects.get(pk=1)
            # Compare item track_name_text to track.name - if exists do something, if not, add it.
	try:
            logging.warning("TRACK name from radio station: [" + row['track_name_text']+ "].")
            check_for_track = Track.objects.get(name =""+row['track_name_text']+"")
            logging.warning("Checking local TRACK table for TRACK by name: [" + check_for_track.name + "].")
            if check_for_artist:
                rt = check_for_track
                logging.warning("TRACK exists in table, setting current TRACK to existing TRACK from table.")
            else:
                logging.warning("><><><><><><><><><><><><><><> strange race condition here.")
	except:
            try:
                add_track = Track.objects.create(name=row['track_name_text'], date_added=row['date_added'], artist=ra)
                rt = add_track
		logging.warning("TRACK doesn't exist in table, creating new TRACK and setting current TRACK to new TRACK.")
            except:
                logging.warning("Something failed with grabbing or creating a TRACK, setting to default TRACK.")
	        rt = Track.objects.get(pk=1)
        rp = RunningPlaylist.objects.create(processing_time = pt, Unique_ID=row['Unique_ID'], date_added=row['date_added'], time_played=row['time_played'], radio_station=rs, artist_name_text=row['artist_name_text'], track_name_text=row['track_name_text'], artist=ra, track=rt)
	rows_added += 1
    else:
        logging.warning("[check_rp] already exists in database - Unique_ID: " + row['Unique_ID'])

logging.warning("Added [ %i ] new rows to RUNNINGPLAYLIST" % rows_added)
cursor.close()
conn.close()

