# Create your views here.
from django.http import HttpResponse
from pwadio_be_2.models import RunningPlaylist
from django.template import Context, loader

#def index(request):
#    latest_played_tracks = RunningPlaylist.objects.order_by('-date_added')[:100]
#    output = "Last played artists " + ', '.join([p.artist_name_text for p in latest_played_tracks])
#    return HttpResponse(output)

def index(request):
    runningplaylist = RunningPlaylist.objects.order_by('-date_added')[:25]
    template = loader.get_template('running_playlist/list.html')
    context = Context({
        'runningplaylist': runningplaylist,
    })
    return HttpResponse(template.render(context))

#def detail(request, id):
#    return HttpResponse("This is running_playlist entry %s." % id)

def detail(request, id):
    template = loader.get_template('running_playlist/detail.html')
    context = Context({
        'id': id,
    })
    return HttpResponse(template.render(context))
