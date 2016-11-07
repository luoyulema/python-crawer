# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from moko.items import MokoItem


class MokoPipeline(object):

    def __init__(self):
        self.file = open('test.txt', 'w')

    def process_item(self, item, spider):
        text = item['img_url']+'\n'
        self.file.writelines(text)
        return item

    def close_spider(self, spider):
        self.file.close()
