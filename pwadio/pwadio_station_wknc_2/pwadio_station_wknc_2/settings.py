# Scrapy settings for pwadio_station_wknc_2 project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/topics/settings.html
#

BOT_NAME = 'pwadio_station_wknc_2'

SPIDER_MODULES = ['pwadio_station_wknc_2.spiders']
NEWSPIDER_MODULE = 'pwadio_station_wknc_2.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'pwadio_station_wknc_2 (+http://www.yourdomain.com)'

ITEM_PIPELINES = [
    'pwadio_station_wknc_2.pipelines.PwadioStationWknc2Pipeline',
    ]

#EXTENSIONS = {
#    'pwadio_station_wknc_2.extensions.LogSpiderStats':500,
#}

MYEXT_ENABLED = True
MYEXT_ITEMCOUNT = "1000"

STATS_CLASS = "scrapy.statscol.MemoryStatsCollector"

WEBSERVICE_ENABLED = True

def setup_django_env(path):
    import imp, os
    from django.core.management import setup_environ

    f, filename, desc = imp.find_module('settings', [path])
    project = imp.load_module('settings', f, filename, desc)

    setup_environ(project)
    # Add django project to sys.path
    import sys
    sys.path.append(os.path.abspath(os.path.join(path, os.path.pardir)))

setup_django_env('/home/amosbrown/pydev/pwadio/pwadio/') 
