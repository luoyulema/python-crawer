# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from moko.items import MokoItem
import MySQLdb
import MySQLdb.cursors
from twisted.enterprise import adbapi


class MokoPipeline(object):

    def __init__(self):
        self.file = open('test.txt', 'w')

    def process_item(self, item, spider):
        text = item['img_url'] + '\n'
        self.file.writelines(text)
        return item

    def close_spider(self, spider):
        self.file.close()


class MokoMysqlPipeline(object):

    def __init__(self):
        self.dbpool = adbapi.ConnectionPool(
            dbapiName='MySQLdb',
            host='127.0.0.1',
            db='moko',
            user='root',
            passwd='xxxxxx',
            cursorclass=MySQLdb.cursors.DictCursor,
            charset='utf-8',
            use_unicode=False,

        )

    def process_item(self, item, spider):
        query = self.dbpool.runInteraction(self.__conditional_insert, item)
        return item

    def __conditional_insert(self, tx, item):
        parms = item['img_url']
        sql = "insert into moko valuse %s" % parms
        tx.execute(sql)
