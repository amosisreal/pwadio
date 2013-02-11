# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/topics/item-pipeline.html
import sys
import datetime 
from datetime import date, timedelta
import MySQLdb
import hashlib
import logging
from scrapy.log import ScrapyFileLogObserver
from scrapy.exceptions import DropItem
from scrapy.http import Request

from pwadio.pwadio_be.models import RunningPlaylist, RadioStation, ItunesTrackInfo
import itunes

class PwadioStationWkncPipeline(object):
	print "!~!~!~!~!~!~!~!~!~!~!~!~!~!~!~!~!~!~!~!~!~!~!~"

	def __init__(self):
		#Get last date_added in db.
		try:
			last_added = RunningPlaylist.objects.order_by('-date_added')[0]
			if last_added.date_added is not None:
				self.last_date_in_db = last_added.date_added
			else:
				self.last_date_in_db = datetime.datetime.now() - timedelta(days=365)
		except MySQLdb.Error, e:
			print "exception found"
			print "Error %d: %s" % (e.args[0], e.args[1])

	def process_item(self, item, spider):
		if(item['true_date'] > self.last_date_in_db):
			print "true_date is is more recent than last_date_in_db, add it to db"
			#Okay, now we have a new track, let's get the itunes info based on artist and track name.
			iTunes_track = itunes.search(query="" + item['artist_name_text'] + " " + item['track_name_text'] +"", media='music')
	  		
			#if we get a result, assume the first index in the list is 100% accurate at all times.
			#please be advised, this is a nasty race condition.
			if iTunes_track:
				print iTunes_track[0].get_name()
				print iTunes_track[0].get_artist()
				print iTunes_track[0].get_id()
				print iTunes_track[0].get_artist().get_id()
				item['artist'] = iTunes_track[0].get_artist().get_id()
				item['track'] = iTunes_track[0].get_id()

				#While we have the itunes song, check the db for its existence, and if not there, just add it.  
				#This is where we get all the url and image info for display
				#''' Start of long comment
				try: 
					check_track = ItunesTrackInfo.objects.get(track_id=item['track'])	
				except: 
					check_track = None	
	
				print check_track
				
				if check_track:
					print "%s already exists in local iTunes table.  Skip it." % (item['track'])
				else:
					print "%s is not in local iTunes Table, add it." % (item['track'])
					found_this_track = ItunesTrackInfo()
					found_this_track.date_added = item['true_date']
					found_this_track.wrapper_type = iTunes_track[0].type
					found_this_track.kind = iTunes_track[0].type
					found_this_track.artist_id = iTunes_track[0].get_artist().get_id()
					found_this_track.collection_Id = iTunes_track[0].get_album().get_id()
					found_this_track.track_id = iTunes_track[0].get_id()
					found_this_track.artist_name = iTunes_track[0].get_artist()
					found_this_track.collection_name = iTunes_track[0].get_album()
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
					#found_this_track.short_description = iTunes_track[0].get_description()
					#found_this_track.long_description = iTunes_track[0].get_description()
					found_this_track.save()
			#End of long comment '''
		    #if no search result, set artist and track to 0.
			else:
				item['artist'] = 0
				item['track'] = 0
			#then put it in the DB like all is perfect.
			try:
				item.save()
			except MySQLdb.Error, e:
				print "exception found"
				print "Error %d: %s" % (e.args[0], e.args[1])
		else:
			print "bypass this one, it is older"
			return item
