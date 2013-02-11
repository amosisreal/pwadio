# Full path and name to your csv file
csv_filepathname="/home/amosbrown/databases/exports/pwadio_processingTime_export.txt"
# Full path to your django project directory
your_djangoproject_home="/home/amosbrown/dev_Python/newPwadio/"

import sys,os
sys.path.append(your_djangoproject_home)
os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'
from time import strftime
from datetime import datetime, time, date

from pwadio.models import processing_Time, radio_station

import csv
dataReader = csv.reader(open(csv_filepathname), delimiter=',', quotechar='"')

for row in dataReader:
    if row[0] != 'id': # Ignore the header row, import everything else
        pt = processing_Time()
        rs = radio_station.objects.get(id = row[1])
        pt.station_ID = rs
        pt.download_site_time = row[2]
        pt.processing_time = row[3]
        pt.total_elapsed_time = row[4]
        pt.number_of_tracks_added_this_batch = row[5]
        pt.date_added = datetime.utcfromtimestamp(float(row[6]))
        pt.save()
