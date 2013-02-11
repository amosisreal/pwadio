import datetime
from haystack.indexes import *
from haystack import site
from pwadio_be_2.models import Artist, Track, RadioStation

class ArtistIndex(SearchIndex):
    name = CharField(document=True, use_template=True)
    date_added = DateTimeField(model_attr='date_added')

    def get_model(self):
        return Artist

    def index_queryset(self):
        """Used when the entire index for model is updated."""
        return self.get_model().objects.filter(date_added__lte=datetime.datetime.now())

class TrackIndex(SearchIndex):
    name = CharField(document=True, use_template=True)
    date_added = DateTimeField(model_attr='date_added')

    def get_model(self):
        return Track

    def index_queryset(self):
        """Used when the entire index for model is updated."""
        return self.get_model().objects.filter(date_added__lte=datetime.datetime.now())

site.register(Artist, ArtistIndex)
site.register(Track, TrackIndex)
