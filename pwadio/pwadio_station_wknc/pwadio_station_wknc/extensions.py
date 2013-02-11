from scrapy import signals, stats
from scrapy.exceptions import NotConfigured
from pwadio_be.models import ProcessingTime

class LogSpiderStats(object):

    def __init__(self, stats):
        self.stats = stats

    @classmethod
    def from_crawler(cls, crawler):
        print "##~##~##~##~##~##~##~##~##"
        print unicode(cls)
        print(crawler.stats.get_stats())
        print "##~##~##~##~##~##~##~##~##"
        return cls(crawler.stats)
