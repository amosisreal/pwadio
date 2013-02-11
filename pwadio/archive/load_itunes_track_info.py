# Full path and name to your csv file
csv_filepathname="/home/amosbrown/databases/exports/pwadio_iTunes_export.txt"
# Full path to your django project directory
your_djangoproject_home="/home/amosbrown/dev_Python/newPwadio/"

import sys,os
sys.path.append(your_djangoproject_home)
os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'
from time import strftime
from datetime import datetime, time, date

from pwadio.models import iTunes_track_info

import csv
dataReader = csv.reader(open(csv_filepathname), delimiter=',', quotechar='"')

for row in dataReader:
    if row[0] != 'id': # Ignore the header row, import everything else
        iTunesTrack = iTunes_track_info()
        iTunesTrack.date_added = datetime.utcfromtimestamp(float(row[1]))
        iTunesTrack.wrapper_type = row[2]
        iTunesTrack.kind = row[3]
        iTunesTrack.artist_id = row[4]
        iTunesTrack.collection_Id = row[5]
        iTunesTrack.track_id = row[6]
        artist_name = row[7]
        iTunesTrack.artist_name = (artist_name[:100] + '...') if len(artist_name) >= 100 else artist_name 
        collection_name = row[8]
        iTunesTrack.collection_name = (collection_name[:100] + '...') if len(collection_name) >=  100 else collection_name
        track_name = row[9]
        iTunesTrack.track_name = (track_name[:100] + '...') if len(track_name) >= 100 else track_name
        collection_censored_name = row[10]
        iTunesTrack.collection_censored_name = (collection_censored_name[:100] + '...') if len(collection_censored_name) >= 100 else collection_censored_name
        track_censored_name = row[11]
        iTunesTrack.track_censored_name = (track_censored_name[:100] + '...') if len(track_censored_name) >= 100 else track_censored_name
        iTunesTrack.artist_view_URL = row[12]
        iTunesTrack.collection_view_URL = row[13]
        iTunesTrack.track_view_URL = row[14]
        iTunesTrack.preview_URL = row[15]
        iTunesTrack.artwork_URL_30 = row[16]
        iTunesTrack.artwork_URL_60 = row[17]
        iTunesTrack.artwork_URL_100 = row[18]
        iTunesTrack.collection_price = row[19]
        iTunesTrack.track_price = row[20]
        iTunesTrack.release_date = row[21]
        iTunesTrack.collection_explicitness = row[22]
        iTunesTrack.track_explicitness = row[23]
        iTunesTrack.disc_count = row[24]
        iTunesTrack.disc_number = row[25]
        iTunesTrack.track_count = row[26]
        iTunesTrack.track_number = row[27]
        iTunesTrack.track_time_millis = row[28]
        iTunesTrack.country = row[29]
        iTunesTrack.currency = row[30]
        iTunesTrack.primary_genre_name = row[31]
        iTunesTrack.content_advisory_rating = row[32]
        iTunesTrack.short_description = row[33]
        iTunesTrack.long_description = row[34]
        iTunesTrack.save()
