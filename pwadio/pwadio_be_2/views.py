# Create your views here.
from django.http import HttpResponse
from pwadio_be_2.models import RunningPlaylist, MusicServices_Track_Lookup, ItunesTrackInfo, Track, Artist, RadioStation
from django.template import Context, loader
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def index(request):
    runningplaylist = RunningPlaylist.objects.select_related().order_by('-date_added')[:50]
    num_stations = RadioStation.objects.count()

    template = loader.get_template('running_playlist/list.html')
    context = Context({
        'runningplaylist': runningplaylist,
	    'num_stations': num_stations,
    })
    return HttpResponse(template.render(context))

def tracklist(request):
    tracks = Track.objects.select_related().order_by('name')[:50]

    template = loader.get_template('tracks/list.html')
    context = Context({
        'tracks': tracks,
    })
    return HttpResponse(template.render(context))

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
    artists = Artist.objects.select_related().order_by('name')[:50]
    
    template = loader.get_template('artists/list.html')
    context = Context({
        'artists': artists,
    })
    return HttpResponse(template.render(context))

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
    radiostations = RadioStation.objects.select_related().order_by('name')[:50]
    
    template = loader.get_template('radiostations/list.html')
    context = Context({
        'radiostations': radiostations,
    })
    return HttpResponse(template.render(context))

def rsdetail(request, id):

    rs = RadioStation.objects.select_related().get(pk=id)

    template = loader.get_template('radiostations/detail.html')
    context = Context({
        'rs': rs,

    })
    return HttpResponse(template.render(context))
