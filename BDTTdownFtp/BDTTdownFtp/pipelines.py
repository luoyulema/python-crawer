# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
import codecs
from scrapy.exceptions import DropItem


class BdttdownftpPipeline(object):

    def __init__(self):
        self.file = codecs.open('ftp.json', 'w')
        self.ids_seen = set()

    def process_item(self, item, spider):
        if item['ftp'] in self.ids_seen:
            raise DropItem("Duplicate item found:%s" % item)
        else:
            self.ids_seen.add(item['ftp'])
        for i in self.ids_seen:
            line = json.dumps(i, ensure_ascii=False) + '\n'
            self.file.write(line)
        return item

    def spider_closed(self, spider):
        self.file.close()
