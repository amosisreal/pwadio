# Create your views here.
from django.http import HttpResponse
from pwadio_be_2.models import RunningPlaylist, MusicServices_Track_Lookup, ItunesTrackInfo, Track, Artist, RadioStation
from django.template import Context, loader
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic.list_detail import object_list


def index(request):
    from django.db.models import Q
    runningplaylist = RunningPlaylist.objects.select_related().order_by('-date_added')
    #num_stations = RadioStation.objects.count()

    return object_list(request, template_name='running_playlist/list.html', queryset=runningplaylist, paginate_by=25)

def tracklist(request):
    from django.db.models import Q

    tracks = Track.objects.select_related().order_by('name')

    return object_list(request, template_name='tracks/list.html', queryset=tracks, paginate_by=25)

def trackdetail(request, id):
    tr = Track.objects.select_related().get(pk=id)
    tr_info = tr.mstl_track.all()

    template = loader.get_template('tracks/detail.html')
    context = Context({
        'tr': tr,
		'tr_info' : tr_info,
    })
    return HttpResponse(template.render(context))

def artistlist(request):
    from django.db.models import Q   
    artists = Artist.objects.select_related().order_by('name')
    
    return object_list(request, template_name='artists/list.html', queryset=artists, paginate_by=25)


def artistdetail(request, id):

    artist = Artist.objects.select_related().get(pk=id)
    artist_tracks = artist.t_artist.all()

    template = loader.get_template('artists/detail.html')
    context = Context({
        'artist': artist,
	'artist_tracks': artist_tracks ,
    })
    return HttpResponse(template.render(context))

def rslist(request):
    from django.db.models import Q

    radiostations = RadioStation.objects.select_related().order_by('name')
    return object_list(request, template_name='radiostations/list.html', queryset=radiostations, paginate_by=25)
    
def rsdetail(request, id):

    rs = RadioStation.objects.select_related().get(pk=id)

    template = loader.get_template('radiostations/detail.html')
    context = Context({
        'rs': rs,

    })
    return HttpResponse(template.render(context))
