# Create your views here.
from django.http import HttpResponse
from pwadio_be_2.models import RunningPlaylist, MusicServices_Track_Lookup, ItunesTrackInfo, Track, Artist
from django.template import Context, loader

#def index(request):
#    latest_played_tracks = RunningPlaylist.objects.order_by('-date_added')[:100]
#    output = "Last played artists " + ', '.join([p.artist_name_text for p in latest_played_tracks])
#    return HttpResponse(output)

def index(request):
    runningplaylist = RunningPlaylist.objects.select_related().order_by('-date_added')[:50]
    msl = {}
    for rp in runningplaylist:
	t = rp.track
	a = rp.artist
	try: 
	    ml = t.mstl_track.get(track=t)	
	except:
	    ml = None
	if ml:
	    try:
		it = ItunesTrackInfo.objects.get(track_id=ml.music_service_object_id_from_web)	
	    except:
		it = None
	else:
	    it = None
    	msl[rp.id] = [t, a, ml, it]

	# get track lookup and itunes info into a variable that I can send to the template.
	#t = rp.track	
	#ml = t.mstl_track.get(track=t)
	#mls[rp.id] = '!'
	#mls[rp.id] = ml
	#it[rp.id] = ItunesTrackInfo.objects.get(track_id=ml[rp.id].music_service_object_id_from_web)

    template = loader.get_template('running_playlist/list.html')
    context = Context({
        'runningplaylist': runningplaylist,
	'msl':msl,

    })
    return HttpResponse(template.render(context))

def detail(request, id):
    tr = Track.objects.select_related().get(pk=id)
    tr_info = tr.mstl_track.all()
    
    template = loader.get_template('running_playlist/detail.html')
    context = Context({
        'tr': tr,
        'tr_info' : tr_info,
    })
    return HttpResponse(template.render(context))

def tracklist(request):
    tracks = Track.objects.select_related().order_by('-date_added')[:25]

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
    artists = Artist.objects.select_related().order_by('-date_added')[:25]
    
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
