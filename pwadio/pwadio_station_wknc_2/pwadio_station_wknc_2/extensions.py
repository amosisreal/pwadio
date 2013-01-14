from scrapy import signals, stats
from scrapy.exceptions import NotConfigured
from pwadio_be_2.models import ProcessingTime
from scrapy import log

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
        return ext

    def spider_opened(self, spider):
        spider.log("##~##~##~##~##~##~##~ opened spider %s" % spider.name, level=log.INFO)


    def spider_closed(self, spider):
	pt = ProcessingTime.objects.get(start_time=spider._crawler.stats._stats['start_time'])
	pt.finish_time = spider._crawler.stats._stats['finish_time']
	pt.finish_reason = spider._crawler.stats._stats['finish_reason']
	pt.save()
        spider.log("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~`", level=log.INFO)
        #spider.log("##~##~##~##~##~##~##~ closed spider %s" % spider.name, level=log.INFO)
        spider.log("Spider Start Time: " + unicode(spider._crawler.stats._stats['start_time']), level=log.INFO)
        spider.log("Spider Stop Time: " + unicode(spider._crawler.stats._stats['finish_time']), level=log.INFO)
        spider.log("Spider Finish Reason: "  + unicode(spider._crawler.stats._stats['finish_reason']), level=log.INFO)
        spider.log("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~`", level=log.INFO)

