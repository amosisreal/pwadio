from pwadio_be_2.models import Artist, Album, Track, RadioStation, ProcessingTime, RunningPlaylist, ItunesTrackInfo, MusicServices, MusicServices_Artist_Lookup, MusicServices_Track_Lookup
from django.contrib import admin

#admin.site.register(Artist)
#admin.site.register(Album)
#admin.site.register(Track)
admin.site.register(RadioStation)
#admin.site.register(MusicServices)
#admin.site.register(MusicServices_Artist_Lookup)
#admin.site.register(MusicServices_Track_Lookup)

class RunningPlaylistAdmin(admin.ModelAdmin):
    list_display =  ('radio_station', 'date_added','artist_name_text', 'track_name_text', 'artist', 'track')
#    pass

admin.site.register(RunningPlaylist, RunningPlaylistAdmin)

class ItunesTrackInfoAdmin(admin.ModelAdmin):
    list_display =  ('artist_name', 'track_name', 'collection_name')

admin.site.register(ItunesTrackInfo, ItunesTrackInfoAdmin)

class ProcessingTimeAdmin(admin.ModelAdmin):
    list_display =  ('station_ID', 'start_time', 'finish_time', 'finish_reason', 'date_added', 'download_site_time', 'processing_time', 'total_elapsed_time', 'number_of_tracks_added_this_batch')

admin.site.register(ProcessingTime, ProcessingTimeAdmin)

class MusicServicesAdmin(admin.ModelAdmin):
    list_display = ('date_added','name','URL','apiURL','description','search_API_URL', 'search_URL', 'developer_ID')

admin.site.register(MusicServices, MusicServicesAdmin)

class MusicServices_Artist_LookupAdmin(admin.ModelAdmin):
    list_display = ('date_added','artist','music_service','music_service_object_id_from_web')

admin.site.register(MusicServices_Artist_Lookup, MusicServices_Artist_LookupAdmin)

class MusicServices_Track_LookupAdmin(admin.ModelAdmin):
    list_display = ('date_added','track','music_service','music_service_object_id_from_web')

admin.site.register(MusicServices_Track_Lookup, MusicServices_Track_LookupAdmin)

class ArtistAdmin(admin.ModelAdmin):
    list_display = ('name','date_added')

admin.site.register(Artist, ArtistAdmin)

class TrackAdmin(admin.ModelAdmin):
    list_display = ('name','date_added', 'artist')

admin.site.register(Track, TrackAdmin)

