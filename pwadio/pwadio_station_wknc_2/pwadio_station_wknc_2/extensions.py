from scrapy import signals, stats
from scrapy.exceptions import NotConfigured
from pwadio_be_2.models import ProcessingTime

class LogSpiderStats(object):

    def __init__(self, stats):
        self.stats = stats

    @classmethod
    def from_crawler(cls, crawler):
        if not crawler.settings.getbool('MYEXT_ENABLED'):
            raise NotConfigured

        item_count = crawler.settings.getint('MYEXT_ITEMCOUNT', 1000)

        ext = cls(item_count)

        crawler.signals.connect(ext.spider_opened, signal=signals.spider_opened)
        crawler.signals.connect(ext.spider_closed, signal=signals.spider_closed)
        #crawler.signals.connect(ext.item_scraped, signal=signals.item_scraped)
        #crawler.signals.connect(ext.start_time, signal=signals.engine_started)

        #print "##~##~##~##~##~##~##~##~##"
        #print unicode(cls)
        #print(crawler.stats.get_stats())
        #print "##~##~##~##~##~##~##~##~##"
        return ext

    def spider_opened(self, spider):
        spider.log("##~##~##~##~##~##~##~ opened spider %s" % spider.name)


    def spider_closed(self, spider):
        spider.log("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~`")
        spider.log("##~##~##~##~##~##~##~ closed spider %s" % spider.name)
        spider.log("Spider Start Time: " + unicode(spider._crawler.stats._stats['start_time']))
        spider.log("Spider Stop Time: " + unicode(spider._crawler.stats._stats['finish_time']))
	#elapsed_time = timedelta(spider._crawler.stats._stats['finish_time'] - spider._crawler.stats._stats['start_time'])
	#spider.log("Elapsed Time: " + unicode(elapsed_time)
        spider.log("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~`")


    #def item_scraped(self, item, spider):
    #    self.items_scraped += 1
    #    spider.log("##~##~##~##~##~##~##~ added 1 item, total items: %d" % self.items_scraped)
    #    if self.items_scraped == self.item_count:
    #        spider.log("##~##~##~##~##~##~scraped %d items, resetting counter" % self.items_scraped)
    #        self.item_count = 0
