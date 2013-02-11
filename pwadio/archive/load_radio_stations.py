# Full path and name to your csv file
csv_filepathname="/home/amosbrown/databases/exports/pwadio_radio_station_export.txt"
# Full path to your django project directory
your_djangoproject_home="/home/amosbrown/pydev/pwadio/pwadio/"

import sys,os
sys.path.append(your_djangoproject_home)
os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'
from time import strftime
from datetime import datetime, time, date

from pwadio_be.models import RadioStation

import csv
dataReader = csv.reader(open(csv_filepathname), delimiter=',', quotechar='"')

for row in dataReader:
    if row[0] != 'id': # Ignore the header row, import everything else
        radio_station = radio_station()
        radio_station.date_added = datetime.utcfromtimestamp(float(row[1]))
        radio_station.name = row[2]
        radio_station.URL = row[3]
        radio_station.playlist_URL = row[4]
        radio_station.am_fm_band = row[5]
        radio_station.frequency = row[6]
        radio_station.city = row[7]
        radio_station.state = row[8]
        radio_station.zipcode = row[9]
        radio_station.phone_1 = row[10]
        radio_station.phone_2 = row[11]
        radio_station.description = row[12]
        radio_station.save()
