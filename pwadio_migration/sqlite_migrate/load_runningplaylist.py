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
from time import strftime
from datetime import datetime, time, date

import sqlite3 as lite

from pwadio_be_2.models import RunningPlaylist, RadioStation, ItunesTrackInfo, Artist, Track, ProcessingTime, Album, MusicServices, MusicServices_Artist_Lookup, MusicServices_Track_Lookup

sqlite_db = '/home/amosbrown/pydev/pwadio_migration/pwadio.db3'

rows_added = 0

logger = logging.getLogger('pwadio_importer')
hdlr = logging.FileHandler('/home/amosbrown/pydev/pwadio_migration/logs/runningplaylist_importer.log')
formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
hdlr.setFormatter(formatter)
logger.addHandler(hdlr)
logger.setLevel(logging.DEBUG)

table_label = "RUNNINGPLAYLIST"

logger.info("Starting %s importer from sqlite3 to mySQL. ---------------------------------------------------------" % table_label)

#connect to sqlite3
con = lite.connect(sqlite_db)
con.text_factory = str

#pull rows from itunes table
with con:
    cur = con.cursor()
    #cur.execute('SELECT * FROM runningPlaylist order by rp_DateAdded;')

    cur.execute('SELECT * FROM runningPlaylist order by rp_DateAdded limit 1000;')

    rows = cur.fetchall()
    for row in rows:
	try:
	    logger.warning("Trying to set processing time to existing processing time.")
	    pt = ProcessingTime.objects.get(date_added=datetime.utcfromtimestamp(float(row[2])))
        except:
	    logger.warning("Processing time set to default.")
	    pt = ProcessingTime.objects.get(pk=1)   
        rs = RadioStation.objects.get(pk=1)
        ra = Artist.objects.get(pk=1)
        rt = Track.objects.get(pk=1)
        try:
            check_rp = RunningPlaylist.objects.get(Unique_ID=row[1])
        except:
	    check_rp = None
        if not check_rp:
            logger.warning("[check_rp]: is None, add this row to the new database - Unique_ID: " + row[1])
	    try:
	        logger.warning("ARTIST name from radio station: [" + row[5]+ "].")
                check_for_artist = Artist.objects.get(name__iexact=""+row[5]+"")
	        logger.warning("Checking local ARTIST table by name: [" + check_for_artist.name + "].")
                if check_for_artist:
                    ra = check_for_artist
	            logger.warning("ARTIST exists in table, setting current ARTIST to existing ARTIST from table.")
                else:
                    #add_artist = Artist.objects.create(name=item['artist_name_text'])
                    #item['artist'] = add_artist 
		    logger.warning("<><><><><><><><><><><><><><><> strange race condition here.")	
            except:
                #print "Error %d: %s" % (e.args[0], e.args[1])
	        try:
		    add_artist = Artist.objects.create(name=row[5], date_added=datetime.utcfromtimestamp(float(row[2])))
                    ra = add_artist 
		    logger.warning("ARTIST doesn't exist in table, creating new ARTIST and setting current ARTIST to new ARTIST.")	
	        except:
	            logger.warning("Something failed with grabbing or creating an ARTIST, setting to default ARTIST.")
	            ra = Artist.objects.get(pk=1)
            # Compare item track_name_text to track.name - if exists do something, if not, add it.
	    try:
                logger.warning("TRACK name from radio station: [" + row[6]+ "].")
                check_for_track = Track.objects.get(name =""+row[6]+"")
                logger.warning("Checking local TRACK table for TRACK by name: [" + check_for_track.name + "].")
                if check_for_artist:
                    rt = check_for_track
                    logger.warning("TRACK exists in table, setting current TRACK to existing TRACK from table.")
                else:
                    logging.warning("><><><><><><><><><><><><><><> strange race condition here.")
	    except:
                try:
                    add_track = Track.objects.create(name=row[6], date_added=datetime.utcfromtimestamp(float(row[2])), artist=ra)
                    rt = add_track
		    logger.warning("TRACK doesn't exist in table, creating new TRACK and setting current TRACK to new TRACK.")
                except:
                    logger.warning("Something failed with grabbing or creating a TRACK, setting to default TRACK.")
	            rt = Track.objects.get(pk=1)
	    try:
                logger.warning("Item should be saved here.")
	        rp = RunningPlaylist.objects.create(
			processing_time = pt, 
			Unique_ID=row[1], 
			date_added=datetime.utcfromtimestamp(float(row[2])), 
			time_played=datetime.utcfromtimestamp(float(row[3])), 
			radio_station=rs, 
			artist_name_text=row[5], 
			track_name_text=row[6], 
			artist=ra, 
			track=rt)
	        rows_added += 1
            except Exception as e:
                logger.error("Exception found")
                logger.error("Error %s" % (e.args[0]))
        else:
            logger.warning("[check_rp] already exists in database - Unique_ID: " + row[1])


logger.info("Added [ %i ] new rows to %s" % (rows_added, table_label))
cur.close()
logger.info("Closing cursor.")
con.close()
logger.info("Closing sqlite3 connection.")

logger.info("Finished %s importer from sqlite3 to mySQL. ---------------------------------------------------------" % table_label)
