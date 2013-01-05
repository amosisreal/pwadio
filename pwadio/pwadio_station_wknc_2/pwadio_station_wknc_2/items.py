# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/topics/items.html

#from scrapy.item import Item, Field

#class PwadioStationWknc2Item(Item):
    # define the fields for your item here like:
    # name = Field()
    # pass

from scrapy.item import Item, Field
from scrapy.contrib.djangoitem import DjangoItem
from pwadio_be_2.models import RunningPlaylist, RadioStation, Artist, Album, Track, MusicServices, MusicServices_Artist_Lookup, MusicServices_Track_Lookup, ProcessingTime

class PwadioStationWknc2Item(DjangoItem):
    django_model = RunningPlaylist
    true_date = Field()
    date_added_mod = Field()
    radio_station_id = Field()
