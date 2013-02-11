## ORDER of OPERATIONS
# 0 Copy over iTunes tables - no foreign keys. 
# 1 Run Processing times tables.
# 2 Run Running Playlist tables.
# 3 Go through Running Playlist, pull out artist / track combos, then check the local itunes database for them.

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

conn = MySQLdb.connect(host="localhost", user="root", passwd="password", db="pwadio_db", compress=1, cursorclass=MySQLdb.cursors.DictCursor)
table_name = "pwadio_itunes_track_info"
cursor = conn.cursor()

cursor.execute("select id, date_added, wrapper_type, kind, artist_id, collection_Id, track_id, artist_name, collection_name, track_name, artist_view_URL, collection_view_URL, track_view_URL, preview_URL, artwork_URL_30, artwork_URL_60, artwork_URL_100, collection_price, track_price, release_date, country, currency, primary_genre_name from " + table_name + " order by id limit 100")

rows = cursor.fetchall()
rows_added = 0

for row in rows:
    try:
        check_it = ItunesTrackInfo.objects.get(track_id=row['track_id'])
    except:
	check_it = None
    if not check_it:
        logging.warning("[check_it]: is None, add this row to the new database - track_id: " + row['track_id'])
	try:
            logging.warning("Item should be saved here.")
	    found_this_track = ItunesTrackInfo()
	    found_this_track.date_added = item['true_date']
	    found_this_track.wrapper_type = iTunes_track[0].type
  	    found_this_track.kind = iTunes_track[0].type
	    found_this_track.artist_id = iTunes_track[0].get_artist().get_id()
	    if iTunes_track[0].get_album().get_id():
	        found_this_track.collection_Id = iTunes_track[0].get_album().get_id()
	    else:
		found_this_track.collection_Id = 0
	    found_this_track.track_id = iTunes_track[0].get_id()
	    found_this_track.artist_name = iTunes_track[0].get_artist()
	    if iTunes_track[0].get_album():
	        found_this_track.collection_name = iTunes_track[0].get_album()
	    else:
	        found_this_track.collection_name = '' 
	    found_this_track.track_name = iTunes_track[0].get_name()
	    found_this_track.collection_censored_name = ''
	    found_this_track.track_censored_name = ''
	    found_this_track.artist_view_URL = iTunes_track[0].get_artist().get_url()
	    found_this_track.collection_view_URL = iTunes_track[0].get_album().get_url()
	    found_this_track.track_view_URL = iTunes_track[0].get_url()
	    found_this_track.preview_URL = iTunes_track[0].get_preview_url()
	    found_this_track.artwork_URL_30 = iTunes_track[0].get_artwork()['30']
	    found_this_track.artwork_URL_60 = iTunes_track[0].get_artwork()['60']
	    found_this_track.artwork_URL_100 = iTunes_track[0].get_artwork()['100']
	    found_this_track.collection_price = iTunes_track[0].get_price()
	    found_this_track.track_price = iTunes_track[0].get_price()
	    found_this_track.release_date = iTunes_track[0].get_release_date()
	    found_this_track.collection_explicitness = ''
	    found_this_track.track_explicitness = ''
	    found_this_track.disc_count = ''
	    found_this_track.disc_number = iTunes_track[0].get_disc_number()
	    found_this_track.track_count = ''
	    found_this_track.track_number = ''
	    found_this_track.track_time_millis = iTunes_track[0].get_duration()
	    found_this_track.country = ''
	    found_this_track.currency = ''
	    found_this_track.primary_genre_name = iTunes_track[0].get_genre()
	    found_this_track.content_advisory_rating = ''
	    found_this_track.save()
	    rows_added += 1
        except MySQLdb.Error, e:
            logging.warning("Exception found", level=log.ERROR)
            logging.warning("Error %d: %s" % (e.args[0], e.args[1]), level=log.ERROR)

    else:
        logging.warning("[check_it] already exists in database - track_id: " + row['track_id'])

logging.warning("Added [ %i ] new rows to ITUNESTRACKINFO" % rows_added)
cursor.close()
conn.close()

