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

conn = MySQLdb.connect(host="localhost", user="root", passwd="password", db="pwadio_2013", compress=1, cursorclass=MySQLdb.cursors.DictCursor)
table_name = "pwadio_be_runningplaylist"
cursor = conn.cursor()

cursor.execute("select Unique_ID, date_added, time_played, artist_name_text, track_name_text, artist, track from " + table_name + " order by id limit 10")

rows = cursor.fetchall()
rows_added = 0

for row in rows:
    print row['Unique_ID'], row['date_added'], row['time_played'], row['artist_name_text'], row['track_name_text'], row['artist'], row['track']
    pt = ProcessingTime.objects.get(pk=1)   
    rs = RadioStation.objects.get(pk=1)
    ra = Artist.objects.get(pk=1)
    rt = Track.objects.get(pk=1)
    try:
        check_rp = RunningPlaylist.objects.get(Unique_ID=row['Unique_ID'])
    except:
	check_rp = None
    if not check_rp:
        logging.warning("[check_rp]: is None, add this row to the new database - Unique_ID: " + row['Unique_ID'])
	try:
	    logging.warning("ARTIST name from radio station: [" + row['artist_name_text']+ "].")
            check_for_artist = Artist.objects.get(name__iexact=""+row['artist_name_text']+"")
	    logging.warning("Checking local ARTIST table by name: [" + check_for_artist.name + "].")
            if check_for_artist:
                ra = check_for_artist
	        logging.warning("ARTIST exists in table, setting current ARTIST to existing ARTIST from table.")
            else:
                #add_artist = Artist.objects.create(name=item['artist_name_text'])
                #item['artist'] = add_artist 
		logging.warning("<><><><><><><><><><><><><><><> strange race condition here.")	
        except:
            #print "Error %d: %s" % (e.args[0], e.args[1])
	    try:
		add_artist = Artist.objects.create(name=row['artist_name_text'], date_added=row['date_added'])
                ra = add_artist 
		logging.warning("ARTIST doesn't exist in table, creating new ARTIST and setting current ARTIST to new ARTIST.")	
	    except:
	        logging.warning("Something failed with grabbing or creating an ARTIST, setting to default ARTIST.")
	        ra = Artist.objects.get(pk=1)
            # Compare item track_name_text to track.name - if exists do something, if not, add it.
	try:
            logging.warning("TRACK name from radio station: [" + row['track_name_text']+ "].")
            check_for_track = Track.objects.get(name =""+row['track_name_text']+"")
            logging.warning("Checking local TRACK table for TRACK by name: [" + check_for_track.name + "].")
            if check_for_artist:
                rt = check_for_track
                logging.warning("TRACK exists in table, setting current TRACK to existing TRACK from table.")
            else:
                logging.warning("><><><><><><><><><><><><><><> strange race condition here.")
	except:
            try:
                add_track = Track.objects.create(name=row['track_name_text'], date_added=row['date_added'], artist=ra)
                rt = add_track
		logging.warning("TRACK doesn't exist in table, creating new TRACK and setting current TRACK to new TRACK.")
            except:
                logging.warning("Something failed with grabbing or creating a TRACK, setting to default TRACK.")
	        rt = Track.objects.get(pk=1)
#----------------------------------------
 	    # We now have a track and an artist object, let's see if we have seen it before anywhere.
	    # Create the Music Service object.
	    try:
		ms = MusicServices.objects.get(pk=1)
		logging.warning("Created MUSICSERVICE [ms]." + ms.name + ". ")
	    except: 	    
		logging.warning("Unable to instantiate MUSICSERVICE.")
	    # Okay, we have the music service object.  Have we seen this track from iTunes before?
	    # Look in the MusicService_Track_Lookup table for this track at iTunes.
	    try:			
    	        check_track = MusicServices_Track_Lookup.objects.filter(track=rt, music_service=ms)
		logging.warning("Checking to see if this TRACK already exists in local tables. ")
                logging.warning("item [" + rt.name + "]")
	    except:
	        check_track = None
		logging.warning("TRACK relationship not found in local tables. : " + unicode(check_track) + "")
		
            if check_track:
		#  If there is a value for check_track, then we don't need to do anything except add the song/track to running_playlist
		logging.warning("The track relationship already exists, just save the item to running playlists.")
		try:
                    logging.warning("Item should be saved here.")
	            rp = RunningPlaylist.objects.create(processing_time = pt, Unique_ID=row['Unique_ID'], date_added=row['date_added'], time_played=row['time_played'], radio_station=rs, artist_name_text=row['artist_name_text'], track_name_text=row['track_name_text'], artist=ra, track=rt)
                    #item.save()
                except MySQLdb.Error, e:
                    logging.warning("Exception found", level=log.ERROR)
                    logging.warning("Error %d: %s" % (e.args[0], e.args[1]), level=log.ERROR)
	    # If there is no check_track, then we dont know anything about the relationship.
	    else:
		logging.warning("The track relationship doesnt exist, create the track relationship.  See if iTunes has any information on it.")
		logging.warning("Get information from iTunes.")
	       	try:
		    # Grab the information from iTunes to marry to the track and the artist.
	            iTunes_track = itunes.search(query="" + row['artist_name_text'] + " " + row['track_name_text'] + "", media='music')
		    logging.warning("Info from iTunes: Track name: " + iTunes_track[0].get_name() + " | iTunes Track ID: " + unicode(iTunes_track[0].get_id()) + " | Artist name: " + iTunes_track[0].get_artist().get_name() + " | iTunes Artist ID: " + unicode(iTunes_track[0].get_artist().get_id()) + " ")
     	        except:
		    # Couldn't get anything from iTunes.
	    	    iTunes_track = None	
		    logging.warning("Unable to gather data from iTunes.")

	        if iTunes_track:
		    logging.warning("Grabbed track_id [ %i ] from iTunes, let's do some work with it." % (iTunes_track[0].get_id()))
		    found_this_track = ItunesTrackInfo()
		    found_this_track.date_added = row['date_added']
		    found_this_track.wrapper_type = iTunes_track[0].type
		    found_this_track.kind = iTunes_track[0].type
		    found_this_track.artist_id = iTunes_track[0].get_artist().get_id()
		    try:
			album = iTunes_track[0].get_album()
		    except:
			album = None	  
 		    if album:
		        found_this_track.collection_Id = album.get_id()
		        found_this_track.collection_name = album
		        found_this_track.collection_view_URL = album.get_url()		    
		    else:
		        found_this_track.collection_Id = 0
		        found_this_track.collection_name = '' 
		        found_this_track.collection_view_URL = ''		    
		    found_this_track.track_id = iTunes_track[0].get_id()
		    found_this_track.artist_name = iTunes_track[0].get_artist()
		    found_this_track.track_name = iTunes_track[0].get_name()
		    found_this_track.collection_censored_name = ''
		    found_this_track.track_censored_name = ''
		    found_this_track.artist_view_URL = iTunes_track[0].get_artist().get_url()
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
		    found_this_track.disc_number = ''
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
			    logging.warning("Checking if this track_id already exists in local iTunes table.")	
			except:
			    check_local_iTunes = None
			    logging.warning("Track_id doesn't exist in local iTunes table.")	
			
		    if check_local_iTunes:
		    	logging.warning("Track_id exists in local itunes table, skipping.")
		    else:
			logging.warning("Track_id doesn't exist, saving to database.")
			found_this_track.save()
			# Now that we have iTunes info, create the relationships to ARTIST and TRACK.
		        try:
		            check_a_msl = MusicServices_Artist_Lookup.objects.filter(artist=ra, music_service_object_id_from_web=found_this_track.artist_id)
		            #logging.warning("ARTIST relationship exists in table, skipping.")
		        except:
		            check_a_msl = None
                            logging.warning("Setting ARTIST relationship to none.") 
		        if not check_a_msl:
		            try:
		                a_msl = MusicServices_Artist_Lookup.objects.create(date_added=row['date_added'], artist=ra, music_service=ms, music_service_object_id_from_web=found_this_track.artist_id)
	                        logging.warning("Created a new ARTIST lookup relationship")
		            except Exception as e:
		                logging.warning("Unable to assign ARTIST relationship to MusicServiceLookupTable.")
		                logging.warning( e )

		        try:
		            check_t_msl = MusicServices_Track_Lookup.objects.filter(track=rt, music_service_object_id_from_web=found_this_track.track_id)
                            #logging.warning("TRACK relationship exists in table, skipping.")
		        except:
			    check_t_msl = None
			    logging.warning("Setting TRACK relationship to none.")
		        if not check_t_msl:
	                    try:
		                t_msl = MusicServices_Track_Lookup.objects.create(date_added=row['date_added'], track=rt, music_service=ms, music_service_object_id_from_web=found_this_track.track_id)
		                logging.warning("Created a new TRACK lookup relationship")
	                    except:
			        logging.warning("Unable to assign TRACK relationship to MusicServiceLookupTable.")
                                logging.warning( e )

#------------------------------------------------
        rp = RunningPlaylist.objects.create(processing_time = pt, Unique_ID=row['Unique_ID'], date_added=row['date_added'], time_played=row['time_played'], radio_station=rs, artist_name_text=row['artist_name_text'], track_name_text=row['track_name_text'], artist=ra, track=rt)
	rows_added += 1
    else:
        logging.warning("[check_rp] already exists in database - Unique_ID: " + row['Unique_ID'])

logging.warning("Added [ %i ] new rows to RUNNINGPLAYLIST" % rows_added)
cursor.close()
conn.close()

