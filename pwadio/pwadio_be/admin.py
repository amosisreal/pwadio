from pwadio_be.models import Artist, Album, Track, LibraryConnection, RadioStation, ProcessingTime, RunningPlaylist, ItunesTrackInfo
from django.contrib import admin

admin.site.register(Artist)
admin.site.register(Album)
admin.site.register(Track)
admin.site.register(LibraryConnection)
admin.site.register(RadioStation)

class RunningPlaylistAdmin(admin.ModelAdmin):
    list_display =  ('radio_station', 'date_added','artist_name_text', 'track_name_text')
#    pass

admin.site.register(RunningPlaylist, RunningPlaylistAdmin)

class ItunesTrackInfoAdmin(admin.ModelAdmin):
    list_display =  ('artist_name', 'track_name', 'collection_name')

admin.site.register(ItunesTrackInfo, ItunesTrackInfoAdmin)

class ProcessingTimeAdmin(admin.ModelAdmin):
    list_display =  ('station_ID', 'date_added', 'download_site_time', 'processing_time', 'total_elapsed_time', 'number_of_tracks_added_this_batch')

admin.site.register(ProcessingTime, ProcessingTimeAdmin)
