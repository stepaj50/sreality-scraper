# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import psycopg2
# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class SrealityPipeline:
    def process_item(self, item, spider):
        return item
