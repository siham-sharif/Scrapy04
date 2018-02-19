# -*- coding: utf-8 -*-
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

class Books01Spider(CrawlSpider):
    name = 'books01'
    allowed_domains = ['books.toscrape.com']
    start_urls = ['http://books.toscrape.com/']

    rules = (Rule(LinkExtractor(allow=('music')),  callback='parse_page', follow=True),)

    def parse_page(self, response):
        pass
