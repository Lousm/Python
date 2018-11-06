# -*- coding: utf-8 -*-
import scrapy


class SdaSpider(scrapy.Spider):
    name = 'sda'
    allowed_domains = ['asda.com']
    start_urls = ['http://asda.com/']

    def parse(self, response):
        pass
