# -*- coding: utf-8 -*-
import scrapy


class TaobaoSpider(scrapy.Spider):
    name = 'taobao'
    allowed_domains = ['item.taobao.com']
    start_urls = ['http://item.taobao.com/']

    def parse(self, response):
        pass
