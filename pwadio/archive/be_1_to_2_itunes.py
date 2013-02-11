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

cursor.execute("select id, date_added, wrapper_type, kind, artist_id, collection_Id, track_id, artist_name, collection_name, track_name, artist_view_URL, collection_view_URL, track_view_URL, preview_URL, artwork_URL_30, artwork_URL_60, artwork_URL_100, collection_price, track_price, release_date, track_time_millis, country, currency, primary_genre_name from " + table_name + " order by id limit 100")

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
	    found_this_track = ItunesTrackInfo.objects.create(date_added=row['date_added'], wrapper_type = row['wrapper_type'],kind = row['wrapper_type'],artist_id = row['artist_id'],collection_Id = row['collection_Id'],track_id = row['track_id'], artist_name = row['artist_name'],collection_name = row['collection_name'],track_name = row['track_name'],collection_censored_name = '',track_censored_name = '',artist_view_URL = row['artist_view_URL'],collection_view_URL = row['collection_view_URL'],track_view_URL = row['track_view_URL'],preview_URL = row['preview_URL'],artwork_URL_30 = row['artwork_URL_30'],artwork_URL_60 = row['artwork_URL_60'],artwork_URL_100 = row['artwork_URL_100'],collection_price = row['collection_price'],track_price = row['track_price'],release_date = row['release_date'],collection_explicitness = '',track_explicitness = '',disc_count = '',disc_number = '',track_count = '',track_number = '',track_time_millis = row['track_time_millis'],country = '',currency = '',primary_genre_name = row['primary_genre_name'],content_advisory_rating = '')
	    rows_added += 1
        except MySQLdb.Error, e:
            logging.warning("Exception found", level=log.ERROR)
            logging.warning("Error %d: %s" % (e.args[0], e.args[1]), level=log.ERROR)

    else:
        logging.warning("[check_it] already exists in database - track_id: " + row['track_id'])

logging.warning("Added [ %i ] new rows to ITUNESTRACKINFO" % rows_added)
cursor.close()
conn.close()

