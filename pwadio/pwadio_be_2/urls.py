from django.conf.urls.defaults import * 
from tastypie.api import Api
from pwadio_be_2 import views
from pwadio_be_2.api import RunningPlaylistResource, UserResource, RadioStationResource, ProcessingTimeResource, ItunesTrackInfoResource

v1_api = Api(api_name='v1')
v1_api.register(UserResource())
v1_api.register(RadioStationResource())
v1_api.register(RunningPlaylistResource())
v1_api.register(ProcessingTimeResource())
v1_api.register(ItunesTrackInfoResource())

radio_station_resource = RadioStationResource()
running_playlist_resource = RunningPlaylistResource()
processing_time_resource = ProcessingTimeResource()
iTunes_track_info_resource = ItunesTrackInfoResource()
user = UserResource()

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^(?P<running_playlist_id>\d+)/$', views.detail, name='detail'), 
#    (r'^search/', include('haystack.urls')),
    (r'^api/', include(v1_api.urls))
)
