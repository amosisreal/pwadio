from django.db import models

# Create your models here.
class ItunesTrackInfo(models.Model):
    date_added = models.DateTimeField('Date Added')
    wrapper_type = models.CharField(max_length=50)
    kind = models.CharField(max_length=50)
    artist_id = models.CharField(max_length=50)
    collection_Id = models.CharField(max_length=50)
    track_id = models.CharField(max_length=50, unique=True)
    artist_name = models.CharField(max_length=200)
    collection_name = models.CharField(max_length=200)
    track_name = models.CharField(max_length=200)
    collection_censored_name = models.CharField(max_length=200)
    track_censored_name = models.CharField(max_length=200)
    artist_view_URL = models.CharField(max_length=400)
    collection_view_URL = models.CharField(max_length=400)
    track_view_URL = models.CharField(max_length=400)
    preview_URL = models.CharField(max_length=400)
    artwork_URL_30 = models.CharField(max_length=400)
    artwork_URL_60 = models.CharField(max_length=400)
    artwork_URL_100 = models.CharField(max_length=400)
    collection_price = models.CharField(max_length=50)
    track_price = models.CharField(max_length=50)
    release_date = models.CharField(max_length=50)
    collection_explicitness = models.CharField(max_length=50)
    track_explicitness = models.CharField(max_length=50)
    disc_count = models.CharField(max_length=50)
    disc_number = models.CharField(max_length=50)
    track_count = models.CharField(max_length=50)
    track_number = models.CharField(max_length=50)
    track_time_millis = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    currency = models.CharField(max_length=50)
    primary_genre_name = models.CharField(max_length=50)
    content_advisory_rating = models.CharField(max_length=50)
    short_description = models.CharField(max_length=400)
    long_description = models.CharField(max_length=400)

    def __unicode__(self):
        return self.artist_name

class MusicServices(models.Model):
    date_added = models.DateTimeField('Date Added')
    name = models.CharField(max_length=200)
    URL = models.CharField(max_length=200)
    apiURL = models.CharField(max_length=200)
    description = models.CharField(max_length=600)
    search_API_URL = models.CharField(max_length=200)
    search_URL = models.CharField(max_length=200)
    developer_ID = models.CharField(max_length=200)
	
    def __unicode__(self):
    	return self.name

class Artist(models.Model):
    date_added = models.DateTimeField('Date Added')
    name = models.CharField(max_length=200)
    #URL = models.CharField(max_length=200)
    #zip = models.CharField(max_length=200)
    #genre = models.CharField(max_length=200)

    def __unicode__(self):
        return self.name

class Album(models.Model):
    date_added = models.DateTimeField('Date Added')
    year_released = models.DateTimeField('Year Released')
    name = models.CharField(max_length=200)
    artist = models.ForeignKey(Artist)

    def __unicode__(self):
        return self.name

class Track(models.Model):
    date_added = models.DateTimeField('Date Added')
    #year_released = models.DateTimeField('Year Released')
    name = models.CharField(max_length=200)
    artist = models.ForeignKey(Artist)
    #album = models.ForeignKey(Album)

    def __unicode__(self):
        return self.name

class MusicServices_Artist_Lookup(models.Model):
    date_added = models.DateTimeField('Date Added')
    artist = models.ForeignKey(Artist, related_name='+')
    music_service = models.ForeignKey(MusicServices, related_name='+')
    music_service_object_id_from_web = models.CharField(max_length=200)

class MusicServices_Track_Lookup(models.Model):
    date_added = models.DateTimeField('Date Added')
    track = models.ForeignKey(Track, related_name='+')
    music_service = models.ForeignKey(MusicServices, related_name='+')
    music_service_object_id_from_web = models.CharField(max_length=200)

class RadioStation(models.Model):
    date_added = models.DateTimeField('Date Added')
    name = models.CharField(max_length=200)
    URL = models.CharField(max_length=200)
    playlist_URL = models.CharField(max_length=200)
    am_fm_band = models.CharField(max_length=200)
    frequency = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    zip = models.CharField(max_length=200)
    phone_1 = models.CharField(max_length=200)
    phone_2 = models.CharField(max_length=200)
    description = models.CharField(max_length=600)

    def __unicode__(self):
        return self.name

class ProcessingTime(models.Model):
    station_ID = models.ForeignKey(RadioStation)
    date_added = models.DateTimeField('Date Added')
    download_site_time = models.DecimalField(decimal_places=5, max_digits=10)
    processing_time = models.DecimalField(decimal_places=5, max_digits=10)
    total_elapsed_time = models.DecimalField(decimal_places=5, max_digits=10)
    number_of_tracks_added_this_batch = models.IntegerField()
    start_time = models.DateTimeField('Start Time')
    finish_time = models.DateTimeField('Finish Time')
    finish_reason = models.CharField(max_length='200')

    def __unicode__(self):
        return unicode(self.start_time)

class RunningPlaylist(models.Model):
    processing_time = models.ForeignKey(ProcessingTime)
    Unique_ID = models.CharField(max_length=200)
    date_added = models.DateTimeField('Date Added')
    time_played = models.DateTimeField('Time Played')
    radio_station = models.ForeignKey(RadioStation)
    artist_name_text = models.CharField(max_length=200)
    track_name_text = models.CharField(max_length=200)
    #artist = models.CharField(max_length=200)
    artist = models.ForeignKey(Artist)
    # change this to ForeignKey to Artist Table.
    #track = models.CharField(max_length=200, default=0)
    track = models.ForeignKey(Track)
    # change this to ForeignKey to Track Table.

    def __unicode__(self):
        return self.artist_name_text

