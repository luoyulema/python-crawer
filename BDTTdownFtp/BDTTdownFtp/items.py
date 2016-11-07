# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
from scrapy import Item, Field


class BdttdownftpItem(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    ftp = Field()
