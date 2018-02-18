# -*- coding: utf-8 -*-
from scrapy import Spider
from scrapy.loader import ItemLoader

#modue used in scrapy
from scrapy.http import FormRequest

from quotes_spider.items import QuotesSpiderItem

class Test03Spider(Spider):
    name = 'test03'
    start_urls = (
        'http://quotes.toscrape.com/login',
    )

    def parse(self, response):
        token = response.xpath('//*[@name="csrf_token"]/@value').extract_first()

        return FormRequest.form_response(response,
                                         formdata={'csrf_token': token,
                                                   'password' : 'bar',
                                                   'username' : 'foo'},
                                         callback=self.scrape_home_page

       )

    def scrape_home_page(self, response):
        l = ItemLoader(item=QuotesSpiderItem(), response=response)

        h1_tag = response.xpath('//h1/a/text()').extract_first()
        tags = response.xpath('//*[@class="tag-item"]/a/text()').extract()

        l.add_value('h1_tag', h1_tag)
        l.add_value('tags', tags)

        return l.load_item()