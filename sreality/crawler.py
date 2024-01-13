from scrapy.utils.project import get_project_settings
from scrapy import signals
from scrapy.signalmanager import dispatcher
from scrapy.crawler import CrawlerProcess

from srealityscraper import SrealityscraperSpider

results = []

def crawler_results(item):
    results.append(item)

def crawl():
    dispatcher.connect(crawler_results, signal=signals.item_scraped)

    process = CrawlerProcess(get_project_settings())
    process.crawl(SrealityscraperSpider)
    process.start()

    return results

if __name__ == '__main__':
    crawl()
