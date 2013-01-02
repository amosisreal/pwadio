# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/topics/items.html

from scrapy.item import Item, Field
from scrapy.contrib_exp.djangoitem import DjangoItem
from pwadio_be.models import RunningPlaylist, RadioStation

#class PwadioStationWkncItem(Item):
#    define the fields for your item here like:
#    name = Field()    
#    radio_station = Field()
#    radio_station_id = Field()
#    Unique_ID= Field()
#    time_played = Field()
#    track_name_text= Field()
#    artist_name_text = Field()
#    date_added = Field()
#    true_date = Field()

class PwadioStationWkncItem(DjangoItem):
    django_model = RunningPlaylist
    true_date = Field()
    date_added_mod = Field()
    radio_station_id = Field()
