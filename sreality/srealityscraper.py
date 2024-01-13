import scrapy
import json

from items import SrealityItem

class SrealityscraperSpider(scrapy.Spider):
    name = "srealityscraper"
    allowed_domains = ["sreality.cz"]
    start_urls = ["https://www.sreality.cz/api/en/v2/estates?category_main_cb=1&category_type_cb=1&per_page=500"]

    def parse(self, response):
        real_estates = json.loads(response.body)

        for item in real_estates['_embedded']['estates']:
            real_estate = SrealityItem()
            real_estate['title'] = item['name'].replace("²","<sup>2</sup>").replace("\xa0"," ")
            real_estate['img_url'] = item['_links']['images'][0]['href']
            yield real_estate
