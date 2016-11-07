# -*- coding: utf-8 -*-
from scrapy.spiders import CrawlSpider
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor
from moko.items import MokoItem
import re
from scrapy.http import Request
from scrapy.selector import Selector


class SpiderSpider(CrawlSpider):
    name = "spider"
    allowed_domains = ["moko.cc"]
    start_urls = (
        'http://www.moko.cc/post/aaronsky/list.html',
    )
    rules = (Rule(LinkExtractor(allow=('/post/\d*\.html',)),
                  callback='parse_img', follow=True),)

    def parse_img(self, response):
        Item = MokoItem()
        Itemurls = response.xpath('//div[@class="pic dBd"]')
        for div in Itemurls:
            Item['img_url'] = div.xpath('.//img/@src2').extract()[0]
        Itemname = response.xpath(
            '//a[contains(@class,"mwC u break-word")]/text()')
        Item['img_name'] = Itemname.extract()[0]
        yield Item
        
