# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.http import Request
import codecs
import json


class DoubanPipeline(object):

    def __init__(self):
        self.file = codecs.open('doubanmovie.ftp', 'w')

    def process_item(self, item, spider):
        classification = actor = ''
        lenactor = len(item['actor'])
        lenclassification = len(item['classification'])
        for i in xrange(lenactor):
            actor += item['actor'][i]
            if i < lenactor - 1:
                actor += '/'
        for i in xrange(lenclassification):
            classification += item['classification'][i]
            if i < lenclassification - 1:
                classification += '/'
        line = item['name'][0] + '\n' + item['year'][0] + ' ' + \
            item['score'][0] + '\n' + item['director'][0] + \
            '\n' + actor + '' + classification + '\n'
        
        self.file.write(line.encode('utf-8'))

    def spider_closed(self, spider):
        self.file.close()
