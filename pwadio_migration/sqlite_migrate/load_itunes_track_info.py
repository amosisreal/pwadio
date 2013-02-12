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
hdlr = logging.FileHandler('/home/amosbrown/pydev/pwadio_migration/logs/itunes_song_info_importer.log')
formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
hdlr.setFormatter(formatter)
logger.addHandler(hdlr)
logger.setLevel(logging.DEBUG)

table_label = "ITUNESSONGINFO"

logger.info("Starting %s importer from sqlite3 to mySQL. ---------------------------------------------------------" % table_label)

#connect to sqlite3
con = lite.connect(sqlite_db)

#pull rows from itunes table
with con:
    cur = con.cursor()
    cur.execute('SELECT * FROM iTunesSongInfo order by it_Dateadded;')

    #cur.execute('SELECT * FROM iTunesSongInfo order by it_Dateadded limit 10000;')

    rows = cur.fetchall()
    for row in rows:
	try:
            check_it = ItunesTrackInfo.objects.get(track_id=row[6])
        except:
	    check_it = None
        if not check_it:
            logger.info("[check_it]: is None, add this row to the new database - track_id: " + row[6])
	    try:
                logger.info("Attempting to add [" + str(row[0]) + "] : [" + row[6] + "] : " + row[9] + " : " + row[7] + " added on " + unicode(datetime.utcfromtimestamp(float(row[1]))))
	        found_this_track = ItunesTrackInfo.objects.create(
		    date_added=datetime.utcfromtimestamp(float(row[1])), 
		    wrapper_type = row[2] if row[2] else '',
		    kind = row[3] if row[3] else '',
		    artist_id = row[4] if row[4] else '',
		    collection_Id = row[5] if row[5] else '',
     		    track_id = row[6] if row[6] else '', 
		    artist_name = row[7] if row[7] else '',
		    collection_name = row[8] if row[8] else '',
		    track_name = row[9] if row[9] else '',
		    collection_censored_name = row[10] if row[10] else '',
		    track_censored_name = row[11] if row[11] else '',
		    artist_view_URL = row[12] if row[12] else '',
		    collection_view_URL = row[13] if row[13] else '',
		    track_view_URL = row[14] if row[14] else '',
		    preview_URL = row[15] if row[15] else '',
		    artwork_URL_30 = row[16] if row[16] else '',
		    artwork_URL_60 = row[17] if row[17] else '',
		    artwork_URL_100 = row[18] if row[18] else '',
		    collection_price = row[19] if row[19] else '',
		    track_price = row[20] if row[20] else '',
		    release_date = row[21] if row[21] else '',
		    collection_explicitness = row[22] if row[22] else '',
		    track_explicitness = row[23] if row[23] else '',
		    disc_count = row[24] if row[24] else '',
		    disc_number = row[25] if row[25] else '',
		    track_count = row[26] if row[26] else '',
		    track_number = row[27] if row[27] else '',
		    track_time_millis = row[28] if row[28] else '',
		    country = row[29] if row[29] else '',
		    currency = row[30] if row[30] else '',
		    primary_genre_name = row[31] if row[31] else '',
		    content_advisory_rating = row[32] if row[32] else '')
	        rows_added += 1
            except Exception as e:
                logger.error("Exception found")
                logger.error("Error %s" % (e.args[0]))

        else:
            logger.warning("[check_it] already exists in database [" + str(row[0]) + "] - track_id: [" + row[6] + "] added on " + unicode(datetime.utcfromtimestamp(float(row[1]))))

logger.info("Added [ %i ] new rows to %s" % (rows_added, table_label))
cur.close()
logger.info("Closing cursor.")
con.close()
logger.info("Closing sqlite3 connection.")

logger.info("Finished %s importer from sqlite3 to mySQL. ---------------------------------------------------------" % table_label)

