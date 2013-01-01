#   pwadio/api.py
from django.contrib.auth.models import User
from tastypie import fields
from tastypie.resources import ModelResource, ALL, ALL_WITH_RELATIONS
from tastypie.authentication import BasicAuthentication, ApiKeyAuthentication
from tastypie.authorization import DjangoAuthorization

from pwadio.models import RunningPlaylist, RadioStation, ProcessingTime, ItunesTrackInfo

class UserResource(ModelResource):
    class Meta:
        queryset = User.objects.all()
        resource_name = 'user'
        fields = ['username', 'first_name', 'last_name', 'last_login', 'is_active']
        excludes = ['password']
        allowed_methods = ['get']
#        authentication = BasicAuthentication()
#        authorization = DjangoAuthorization()

class RadioStationResource(ModelResource):
    class Meta:
            queryset = RadioStation.objects.all()
            resource_name = 'RadioStation'
            filtering = {
                'name': ALL,
            }


class RunningPlaylistResource(ModelResource):
    radio_station = fields.ForeignKey(RadioStationResource, 'RadioStation', full=True)

    class Meta:
        queryset = RunningPlaylist.objects.all()
        resource_name = 'RunningPlaylist'
        fields = ['radio_station','artist_name_text','track_name_text','time_played']
        allowed_methods = ['get']
 #       authentication = BasicAuthentication()
 #       authorization = DjangoAuthorization()
        filtering = {
            'radio_station': ALL_WITH_RELATIONS,
            'time_played': ['exact','lt','lte','gte','gt']
        }

class ProcessingTimeResource(ModelResource):
    processing_Time = fields.ForeignKey(RadioStationResource, 'station_ID', full=True)

    class Meta:
        queryset = ProcessingTime.objects.all()
        resource_name = 'ProcessingTime'
        fields = ['station_ID','date_added','download_site_time','processing_time','total_elapsed_time','number_of_tracks_added_this_batch']
        allowed_methods = ['get']
        filtering = {
            'radio_station': ALL_WITH_RELATIONS,
            'date_added': ['exact','lt','lte','gte','gt']
        }

class ItunesTrackInfoResource(ModelResource):
    class Meta:
            queryset = ItunesTrackInfo.objects.all()
            resource_name = 'iTunestracks'
            allowed_methods = ['get']

