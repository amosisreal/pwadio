from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
import logging
from scrapy.log import ScrapyFileLogObserver

import datetime as dt
import dateutil.parser as dparser
import time
import string
import types

from pwadio_station_wknc.items import PwadioStationWkncItem
from pwadio_be.models import RunningPlaylist, RadioStation

class pwadio_station_wkncSpider(BaseSpider):

    name = "pwadio_station_wknc"
    allowed_domains = ["wknc.org"]
    start_urls = [
        "http://wknc.org/playlist"
    ]

    def parse(self, response):
        hxs = HtmlXPathSelector(response)
	#this is a hack to ge the radio station.  This should be a select from existing objects.
        rs = RadioStation()
        rs.id = 1
        rs.name = 'wknc'
        #get date from website
        date_str= hxs.select('//div/div/h1/text()').extract()
        date_str = date_str[1].split()
        #date format from website: Sunday, November 11, 2012
        #split into month, day, year
        month_played = date_str[1]
        day_played = date_str[2]
        year_played = date_str[3]

        songs = hxs.select('//table[@class=\"playlist\"]/tr[position()>0]')
        #get songs from website
        items = []
        for song in songs:
            item = PwadioStationWkncItem()
            item['radio_station'] = rs
            item['radio_station_id'] = 1
            #time_played comes back as a list with one index.  [0]
            time_played = song.select('td[position()=1]/text()').extract()
            time_played = time_played[0].replace(" ","")
            
            #item['track_name_text'] = song.select('td[position()=2]/i/text()')[0].extract()
            track_name_text = song.select('td[position()=2]/i/text()')
            if track_name_text:
                item['track_name_text'] = track_name_text[0].extract()
            else:
                item['track_name_text'] = ""

            artist_name_text = song.select('td[position()=3]/text()')
            if artist_name_text: 
                item['artist_name_text'] = artist_name_text[0].extract() 
            else:
                item['artist_name_text'] = ""

            #craft the approximate datetime from the data on the page.
            new_date = month_played + ' ' + day_played + ' ' + year_played + ' ' + time_played
            #print type(new_date)
            date=dt.datetime.strptime(new_date, '%B %d, %Y %I:%M%p')
            item['time_played'] = str(date)
            item['date_added'] = str(date)

            #print type(date)
            #create the date_added from the cobbled date_time
            date_added = filter(lambda c: c in string.digits, str(date))
            #print type(date_added)
            #item['date_added_mod'] = date_added
            item['true_date'] = date
            #create the Unique_ID from the radio station call letters, and cobbled date_time
            song_guid = rs.name + filter(lambda c: c in string.digits, str(date))
            item['Unique_ID'] = song_guid
            item['artist'] = '0'
            item['track'] = '0'
            items.append(item)

	#reverse items in list for proper chronology.
        items.reverse()    
#        print items
        return items