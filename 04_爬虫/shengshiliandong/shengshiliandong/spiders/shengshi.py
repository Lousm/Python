# -*- coding: utf-8 -*-
import scrapy
from shengshiliandong.items import ShengshiliandongItem
# from scrapy_redis.spiders import RedisSpider
from scrapy_redis_bloomfilter.spiders import RedisSpider


class AsdSpider(RedisSpider):
    name = 'shengshi'
    redis_key = 'AsdSpider:start_urls'
    # allowed_domains = ['stats.gov.cn']
    # start_urls = ['http://www.stats.gov.cn/tjsj/tjbz/tjyqhdmhcxhfdm/2017/index.html']

    def parse(self, response):
        cli_list = response.xpath('//tr[@class="provincetr"]/td/a')
        for cli in cli_list:
            city1 = cli.xpath('./text()').extract_first()
            city1_href = cli.xpath('./@href').extract_first()
            item = ShengshiliandongItem()
            item['first_city'] = city1
            if city1_href is not None:
                new_href = response.urljoin(city1_href)

                yield scrapy.Request(url=new_href, meta={'meat1': item}, callback=self.city2)

    def city2(self, response):
        meat2 = response.meta['meat1']
        cli2_list = response.xpath('//tr[@class="citytr"]/td[2]/a')
        for cli in cli2_list:
            city2 = cli.xpath('./text()').extract_first()
            city2_href = cli.xpath('./@href').extract_first()
            item = ShengshiliandongItem()
            item['first_city'] = meat2['first_city']
            item['second_city'] = city2
            if city2_href is not None:
                new_href = response.urljoin(city2_href)
                yield scrapy.Request(url=new_href, meta={'meat2': item}, callback=self.city3)

    def city3(self, response):
        meat3 = response.meta['meat2']
        cli3_list = response.xpath('//tr[@class="countytr"]/td[2]/a')
        for cli in cli3_list:
            city3 = cli.xpath('./text()').extract_first()
            city3_href = cli.xpath('./@href').extract_first()
            item = ShengshiliandongItem()
            item['first_city'] = meat3['first_city']
            item['second_city'] = meat3['second_city']
            item['third_city'] = city3
            if city3_href is not None:
                new_href = response.urljoin(city3_href)
                yield scrapy.Request(url=new_href, meta={'meat3': item}, callback=self.city4)

    def city4(self, response):
        meat4 = response.meta['meat3']
        cli4_list = response.xpath('//tr[@class="towntr"]/td[2]/a')
        for cli in cli4_list:
            city4 = cli.xpath('./text()').extract_first()
            city4_href = cli.xpath('./@href').extract_first()
            item = ShengshiliandongItem()
            item['first_city'] = meat4['first_city']
            item['second_city'] = meat4['second_city']
            item['third_city'] = meat4['third_city']
            item['fouth_city'] = city4
            if city4_href is not None:
                new_href = response.urljoin(city4_href)
                yield scrapy.Request(url=new_href, meta={'meat4': item}, callback=self.city5)

    def city5(self, response):
        meat5 = response.meta['meat4']
        cli5_list = response.xpath('//tr[@class="villagetr"]/td[3]/text()').extract()
        for cli in cli5_list:
            item = ShengshiliandongItem()
            item['first_city'] = meat5['first_city']
            item['second_city'] = meat5['second_city']
            item['third_city'] = meat5['third_city']
            item['fouth_city'] = meat5['fouth_city']
            item['fifth_city'] = cli
            yield item
