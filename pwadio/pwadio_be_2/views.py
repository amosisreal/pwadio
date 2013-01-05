# Create your views here.
from django.http import HttpResponse
from pwadio_be.models import RunningPlaylist

def index(request):
    latest_played_tracks = RunningPlaylist.objects.order_by('-date_added')[:10]
    output = "Last played artists " + ', '.join([p.artist_name_text for p in latest_played_tracks])
    return HttpResponse(output)

def detail(request, running_playlist_id):
    return HttpResponse("This is running_playlist entry %s." % running_playlist_id)
