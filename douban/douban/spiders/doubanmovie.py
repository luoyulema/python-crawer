# -*- coding: utf-8 -*-
from scrapy.spiders import CrawlSpider, Rule
from scrapy.http import Request
from scrapy.linkextractors import LinkExtractor
from douban.items import DoubanItem
import sys
reload(sys)
sys.setdefaultencoding("utf-8")


class DoubanmovieSpider(CrawlSpider):
    name = "doubanmovie"
    allowed_domains = ["movie.douban.com"]
    start_urls = (
        'https://movie.douban.com/top250',
    )
    rules = [
        Rule(LinkExtractor(allow=(r'https://movie.douban.com/top250\?start=\d+.*'))),
        Rule(LinkExtractor(
            allow=(r'https://movie.douban.com/subject/\d+')), callback='parse_item'),
    ]

    def parse_item(self, response):
        item = DoubanItem()
        item['name'] = response.xpath(
            '//*[@id="content"]/h1/span[1]/text()').extract()
        item['year'] = response.xpath(
            '//*[@id="content"]/h1/span[2]/text()').extract()
        item['score'] = response.xpath(
            '//*[@id="interest_sectl"]/div[1]/div[2]/strong/text()').extract()
        item['director'] = response.xpath(
            '//*[@id="info"]/span[1]/span[2]/a/text()').extract()
        item['classification'] = response.xpath(
            '//span[@property="v:genre"]/text()').extract()
        item['actor'] = response.xpath(
            '//*[@id="info"]/span[3]/a[1]/text()').extract()
        return item
