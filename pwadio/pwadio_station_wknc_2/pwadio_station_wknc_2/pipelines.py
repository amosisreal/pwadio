# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/topics/item-pipeline.html
import sys
import datetime
from datetime import date, timedelta
from scrapy.exceptions import DropItem
from scrapy.http import Request
from scrapy import log
from pwadio_be_2.models import RunningPlaylist, RadioStation, ItunesTrackInfo, Artist, Track, ProcessingTime, Album, MusicServices, MusicServices_Artist_Lookup, MusicServices_Track_Lookup
import itunes

class PwadioStationWknc2Pipeline(object):
    log.msg("!~!~!~!~!~!~!~!~!~!~!~!~ STARTING PIPELINE !~!~!~!~!~!~!~!~!~!~!~", level=log.INFO)
	
    def __init__(self):
	# Get last date_added in db.
	try:
    	    last_added = RunningPlaylist.objects.order_by('-date_added')[0]
	    if last_added.date_added is not None:
	        self.last_date_in_db = last_added.date_added
	    else:
	        self.last_date_in_db = datetime.datetime.now() - timedelta(days=365)
	except MySQLdb.Error, e:
	    log.msg("Exception found", level=log.ERROR)
	    log.msg("Error %d: %s" % (e.args[0], e.args[1]), level=log.ERROR)

    def process_item(self, item, spider):
        if(item['true_date'] > self.last_date_in_db):
	    log.msg("true_date is is more recent than last_date_in_db, add it to db", level=log.INFO)
            item['processing_time'].number_of_tracks_added_this_batch += 1
	    item['processing_time'].save()	

	    a_name = item['artist_name_text']
	    if a_name and a_name[-1] == "*":
	        a_name = a_name[:-1]
	        log.msg("Stripped trailing * from artist name text.", level=log.INFO) 
	
	    t_name = item['track_name_text']
	    if t_name and t_name[-1] == "*":
	        t_name = t_name[:-1]
	        log.msg("Stripped trailing * from track name text", level=log.INFO)

            ### New flow here
            # Compare item artist_name_text to artist.name - if exists do something, if not add it.
            try:
		log.msg("ARTIST name from radio station: [" + a_name + "].", level=log.INFO)
        	check_for_artist = Artist.objects.get(name__iexact=""+a_name+"")
		log.msg("Checking local ARTIST table by name: [" + check_for_artist.name + "].", level=log.INFO)
                if check_for_artist:
                    item['artist'] = check_for_artist
	  	    log.msg("ARTIST exists in table, setting current ARTIST to existing ARTIST from table.", level=log.INFO)
                else:
                    #add_artist = Artist.objects.create(name=item['artist_name_text'])
                    #item['artist'] = add_artist 
		    log.msg("<><><><><><><><><><><><><><><> strange race condition here.", level=log.WARNING)	
            except:
                #print "Error %d: %s" % (e.args[0], e.args[1])
		try:
		    add_artist = Artist.objects.create(name=a_name, date_added=item['true_date'])
                    item['artist'] = add_artist 
		    log.msg("ARTIST doesn't exist in table, creating new ARTIST and setting current ARTIST to new ARTIST.", level=log.INFO)	
		except:
	            log.msg("Something failed with grabbing or creating an ARTIST, setting to default ARTIST.", level=log.ERROR)
	            item['artist'] = Artist.objects.get(pk=1)
            # Compare item track_name_text to track.name - if exists do something, if not, add it.
            try:
                log.msg("TRACK name from radio station: [" + t_name + "].", level=log.INFO)
                check_for_track = Track.objects.get(name =""+t_name+"")
                log.msg("Checking local TRACK table for TRACK by name: [" + check_for_track.name + "].", level=log.INFO)
                if check_for_artist:
                    item['track'] = check_for_track
                    log.msg("TRACK exists in table, setting current TRACK to existing TRACK from table.",level=log.INFO )
                else:
                    log.msg("><><><><><><><><><><><><><><> strange race condition here.", level=log.INFO)
	    except:
                try:
                    add_track = Track.objects.create(name=t_name, date_added=item['true_date'], artist=item['artist'])
                    item['track'] = add_track
		    log.msg("TRACK doesn't exist in table, creating new TRACK and setting current TRACK to new TRACK.", level=log.INFO)
                except:
                    log.msg("Something failed with grabbing or creating a TRACK, setting to default TRACK.", level=log.WARNING)
		    item['track'] = Track.objects.get(pk=1)
          
            # We now have a track and an artist object, let's see if we have seen it before anywhere.
	    # Create the Music Service object.
	    try:
		ms = MusicServices.objects.get(pk=1)
		log.msg("Created MUSICSERVICE [ms]." + ms.name + ". ", level=log.INFO)
	    except: 	    
		log.msg("Unable to instantiate MUSICSERVICE.", level=log.WARNING)
	    # Okay, we have the music service object.  Have we seen this track from iTunes before?
	    # Look in the MusicService_Track_Lookup table for this track at iTunes.
	    try:			
    	        check_track = MusicServices_Track_Lookup.objects.filter(track=item['track'], music_service=ms)
		log.msg("Checking to see if this TRACK already exists in local tables. ", level=log.INFO)
                log.msg("item [" + item['track'].name + "]", level=log.DEBUG)
	    except:
	        check_track = None
		log.msg("TRACK relationship not found in local tables. : " + unicode(check_track) + "", level=log.INFO)
		
            if check_track:
		#  If there is a value for check_track, then we don't need to do anything except add the song/track to running_playlist
		log.msg("The track relationship already exists, just save the item to running playlists.", level=log.INFO)
		try:
                    log.msg("Item should be saved here.", level=log.INFO)
                    item.save()
                except MySQLdb.Error, e:
                    log.msg("Exception found", level=log.ERROR)
                    log.msg("Error %d: %s" % (e.args[0], e.args[1]), level=log.ERROR)
	    # If there is no check_track, then we dont know anything about the relationship.
	    else:
		log.msg("The track relationship doesnt exist, create the track relationship.  See if iTunes has any information on it.", level=log.INFO)
		log.msg("Get information from iTunes.", level=log.INFO)
	       	try:
		    # Grab the information from iTunes to marry to the track and the artist.
	            iTunes_track = itunes.search(query="" + item['artist_name_text'] + " " + item['track_name_text'] + "", media='music')
		    log.msg("Info from iTunes: Track name: " + iTunes_track[0].get_name() + " | iTunes Track ID: " + unicode(iTunes_track[0].get_id()) + " | Artist name: " + iTunes_track[0].get_artist().get_name() + " | iTunes Artist ID: " + unicode(iTunes_track[0].get_artist().get_id()) + " ", level=log.INFO)
     	        except:
		    # Couldn't get anything from iTunes.
	    	    iTunes_track = None	
		    log.msg("Unable to gather data from iTunes.", level=log.WARNING)

	        if iTunes_track:
		    log.msg("Grabbed track_id [ %i ] from iTunes, let's do some work with it." % (iTunes_track[0].get_id()), level=log.INFO)
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
		    if found_this_track.track_id:
			try:
			    check_local_iTunes = ItunesTrackInfo.objects.get(track_id=found_this_track.track_id)
			    log.msg("Checking if this track_id already exists in local iTunes table.", level=log.INFO)	
			except:
			    check_local_iTunes = None
			    log.msg("Track_id doesn't exist in local iTunes table.", level=log.INFO)	
			
		    if check_local_iTunes:
		    	log.msg("Track_id exists in local itunes table, skipping.", level=log.INFO)
		    else:
			log.msg("Track_id doesn't exist, saving to database.", level=log.INFO)
			found_this_track.save()
			# Now that we have iTunes info, create the relationships to ARTIST and TRACK.
		        try:
		            check_a_msl = MusicServices_Artist_Lookup.objects.filter(artist=item['artist'], music_service_object_id_from_web=found_this_track.artist_id)
		            #log.msg("ARTIST relationship exists in table, skipping.", level=log.INFO)
		        except:
		            check_a_msl = None
                            log.msg("Setting ARTIST relationship to none.", level=log.WARNING) 
		        if not check_a_msl:
		            try:
		                a_msl = MusicServices_Artist_Lookup.objects.create(date_added=datetime.datetime.now(), artist=item['artist'], music_service=ms, music_service_object_id_from_web=found_this_track.artist_id)
	                        log.msg("Created a new ARTIST lookup relationship", level=log.INFO)
		            except Exception as e:
		                log.msg("Unable to assign ARTIST relationship to MusicServiceLookupTable.", level=log.ERROR)
		                log.msg( e, level=log.ERROR)

		        try:
		            check_t_msl = MusicServices_Track_Lookup.objects.filter(track=item['track'], music_service_object_id_from_web=found_this_track.track_id)
                            #log.msg("TRACK relationship exists in table, skipping.", level=log.INFO)
		        except:
			    check_t_msl = None
			    log.msg("Setting TRACK relationship to none.", level=log.WARNING)
		        if not check_t_msl:
	                    try:
		                t_msl = MusicServices_Track_Lookup.objects.create(date_added=item['processing_time'].start_time, track=item['track'], music_service=ms, music_service_object_id_from_web=found_this_track.track_id)
		                log.msg("Created a new TRACK lookup relationship", level=log.INFO)
	                    except:
			        log.msg("Unable to assign TRACK relationship to MusicServiceLookupTable.", level=log.ERROR)
                                log.msg( e, level=log.ERROR)

                try:
	            log.msg("Item should be saved here.", level=log.INFO)
		    item.save()
		    log.msg("Looks like save was successful!", level=log.INFO)
	        except MySQLdb.Error, e:
	            log.msg("Exception found", level=log.ERROR)
	            log.msg("Error %d: %s" % (e.args[0], e.args[1]), level=log.ERROR)
    	else:
	    log.msg("Bypass this TRACK, it is older", level=log.INFO)
	
    	return item

