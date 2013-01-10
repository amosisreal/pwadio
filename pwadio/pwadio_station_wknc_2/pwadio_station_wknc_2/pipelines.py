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

from pwadio_be_2.models import RunningPlaylist, RadioStation, ItunesTrackInfo, Artist, Track, ProcessingTime, Album, MusicServices, MusicServices_Artist_Lookup, MusicServices_Track_Lookup
import itunes

class PwadioStationWknc2Pipeline(object):
    print "!~!~!~!~!~!~!~!~!~!~!~!~!~!~!~!~!~!~!~!~!~!~!~"
	
    def __init__(self):
	# Get last date_added in db.
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
            item['processing_time'].number_of_tracks_added_this_batch += 1
	    item['processing_time'].save()	
	    # Okay, now we have a new track, let's get the itunes info based on
	    # artist and track name.
            ### New flow here
            # Compare item artist_name_text to artist.name - if exists do something, if not add it.
            try:
		print "~~~~~~~~~~~~~~~~~~~~~" + item['artist_name_text']+ "~~~~~~~~~~~~~~~~~~~~~~"
                check_for_artist = Artist.objects.get(name__iexact=""+item['artist_name_text']+"")
		print "#~#~#~#~#~#~#" + check_for_artist.name + "#~#~#~#~#~#~#~#~#"
                if check_for_artist:
                    item['artist'] = check_for_artist
		    print "<><><><><><><><><><> set artist to existing artist"
                else:
                    #add_artist = Artist.objects.create(name=item['artist_name_text'])
                    #item['artist'] = add_artist 
		    print "><><><><><><><><><><><><><><> strange race condition here."	
            except:
                #print "Error %d: %s" % (e.args[0], e.args[1])
		try:
		    add_artist = Artist.objects.create(name=item['artist_name_text'], date_added=item['true_date'])
                    item['artist'] = add_artist 
		except:
	        	print "><><><><><><><><><><><><><><><> something failed with the artist thing, setting to default."
	                #print "Error %d: %s" % (e.args[0], e.args[1])
	                item['artist'] = Artist.objects.get(pk=1)
            # Compare item track_name_text to track.name - if exists do something, if not, add it.
            try:
                print "~~~~~~~~~~~~~~~~~~~~~" + item['track_name_text']+ "~~~~~~~~~~~~~~~~~~~~~~"
                check_for_track = Track.objects.get(name =""+item['track_name_text']+"")
                print "#~#~#~#~#~#~#" + check_for_artist.name + "#~#~#~#~#~#~#~#~#"
                if check_for_artist:
                    item['track'] = check_for_track
                    print "<><><><><><><><><><> set track to existing track"
                else:
                    print "><><><><><><><><><><><><><><> strange race condition here."
	            #print "Error %d: %s" % (e.args[0], e.args[1])
            except:
                try:
                    add_track = Track.objects.create(name=item['track_name_text'], date_added=item['true_date'], artist=item['artist'])
                    item['track'] = add_track
                except:
                    print "><><><><><><><><><><><><><><><> something failed with the track thing, setting to default."
		    #print "Error %d: %s" % (e.args[0], e.args[1])
                    item['track'] = Track.objects.get(pk=1)
          
            # Gather iTunes track info, compare to db, add it if it doesn't exist.
	    try:
		ms = MusicServices.objects.get(pk=1)
	    except: 	    
		print "unable to instantiate MusicService."
	    # Okay, now we have a new track, let's get the itunes info based on
	    # artist and track name.
	    try:			
		iTunes_track = itunes.search(query="" + item['artist_name_text'] + " " + item['track_name_text'] + "", media='music')
	    except:
		iTunes_track = None	
	    # please be advised, this is a nasty race condition.
	    if iTunes_track:
		print iTunes_track[0].get_name()
		print iTunes_track[0].get_artist()
		print iTunes_track[0].get_id()
		print iTunes_track[0].get_artist().get_id()
	        # While we have the itunes song, check the db for its existence, and if not there, just add it.  
	    	# This is where we get all the url and image info for display
	
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
		    # found_this_track.short_description = iTunes_track[0].get_description()
		    # found_this_track.long_description = iTunes_track[0].get_description()
		    found_this_track.save()
		    # End of long comment '''
		    # if no search result, set artist and track to 0.
    	        try:
	            a_msl = MusicServices_Artist_Lookup.objects.create(date_added=item['processing_time'].start_time, artist=item['artist'], music_service=ms, music_service_object_id_from_web=found_this_track.artist_id)
	        except Exception as e:
		    print "unable to assign artist to MSAL."
		    print e

	        try:
		    t_msl = MusicServices_Track_Lookup.objects.create(date_added=item['processing_time'].start_time, track=item['track'], music_service=ms, music_service_object_id_from_web=found_this_track.track_id)
	        except:
		    print "unable to assign track to MSTL."
     
            try:
	        item.save()
	    except MySQLdb.Error, e:
	        print "exception found"
	        print "Error %d: %s" % (e.args[0], e.args[1])
    	else:
	    print "bypass this one, it is older"
	
    	return item
