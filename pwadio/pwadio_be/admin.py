from pwadio_be.models import Artist, Album, Track, LibraryConnection, radio_station, processing_Time, running_playlist, iTunes_track_info
from django.contrib import admin

admin.site.register(Artist)
admin.site.register(Album)
admin.site.register(Track)
admin.site.register(LibraryConnection)
admin.site.register(radio_station)

class running_playlistAdmin(admin.ModelAdmin):
    list_display =  ('radio_station', 'date_added','artist_name_text', 'track_name_text')
#    pass

admin.site.register(running_playlist, running_playlistAdmin)

class iTunes_track_infoAdmin(admin.ModelAdmin):
    list_display =  ('artist_name', 'track_name', 'collection_name')

admin.site.register(iTunes_track_info, iTunes_track_infoAdmin)

class processing_TimeAdmin(admin.ModelAdmin):
    list_display =  ('station_ID', 'date_added', 'download_site_time', 'processing_time', 'total_elapsed_time', 'number_of_tracks_added_this_batch')

admin.site.register(processing_Time, processing_TimeAdmin)
