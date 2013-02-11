# Full path and name to your csv file
csv_filepathname="/home/amosbrown/databases/exports/pwadio_running_playlist_export.txt"
# Full path to your django project directory
your_djangoproject_home="/home/amosbrown/dev_Python/newPwadio/"

import sys,os
sys.path.append(your_djangoproject_home)
os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'
from time import strftime
from datetime import datetime, time, date

from pwadio.models import running_playlist, radio_station

import csv
dataReader = csv.reader(open(csv_filepathname), delimiter=',', quotechar='"')

for row in dataReader:
    if row[0] != 'id': # Ignore the header row, import everything else
        playlist = running_playlist()
        playlist.Unique_ID = row[1]
        playlist.date_added = datetime.utcfromtimestamp(float(row[2]))
        playlist.time_played = datetime.utcfromtimestamp(float(row[3]))
        rs = radio_station.objects.get(id = row[4])
        playlist.radio_station = rs 
        playlist.artist_name_text = row[5]
        playlist.track_name_text = row[6]
        playlist.artist = row[7]
        playlist.track = row[8]
        playlist.save()
