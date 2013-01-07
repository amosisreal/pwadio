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
	   
    	    try:
	        a_msl = MusicServices_Artist_Lookup.objects.create(date_added=item['processing_time'].start_time, artist=item['artist'], music_service=ms, music_service_object_id_from_web="0")
	    except Exception as e:
		print "unable to assign artist to MSAL."
		print e

	    try:
		t_msl = MusicServices_Track_Lookup.objects.create(date_added=item['processing_time'].start_time, track=item['track'], music_service=ms, music_service_object_id_from_web="0")
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
