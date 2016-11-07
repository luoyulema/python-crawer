# -*- coding: utf-8 -*-
from scrapy.spiders import CrawlSpider, Rule
from BDTTdownFtp.items import BdttdownftpItem
from scrapy.http import Request
from scrapy.linkextractors import LinkExtractor

import sys
reload(sys)
sys.setdefaultencoding('utf-8')
Fitems = []


class MoviedownSpider(CrawlSpider):
    name = "MovieDown"
    allowed_domains = ["dytt8.net"]
    start_urls = [
        "http://www.ygdy8.net/html/gndy/china/index.html",
        "http://www.ygdy8.net/html/gndy/oumei/index.html",
        "http://www.dytt8.net/html/gndy/rihan/index.html",
        "http://www.dytt8.net/html/tv/oumeitv/index.html",
    ]
    rules = [
        Rule(LinkExtractor(allow=(r'list_\d_\d+\.html'))),
        Rule(LinkExtractor(
            allow=(r'/html/.*?/\d{8}/\d{5}\.html')), callback="parser_ftp"),
    ]

    def parser_ftp(self, response):
        item = BdttdownftpItem()
        ftps = response.xpath('//table/tbody/tr/td/a/text()').extract()[0]
        '''for ftp in ftps:
            if ftp in Fitems:
                pass
            else:
                Fitems.add(ftp)
        for i in Fitems:
            item['ftp'] = i
        return item'''
        item['ftp'] = ftps
        yield item
