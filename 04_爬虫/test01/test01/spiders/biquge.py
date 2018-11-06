# -*- coding: utf-8 -*-
import scrapy
from lxml import etree
from test01.items import Biquge


class BiqugeSpider(scrapy.Spider):
    name = 'biquge'
    allowed_domains = ['biquge.com.tw']
    start_urls = ['http://www.biquge.com.tw/0_424/321010.html']

    def __init__(self):
        self.i = 140

    def parse(self, response):
        tree = etree.HTML(response.body.decode(response.encoding))
        title = tree.xpath('//div[@class="bookname"]/h1/text()')[0]
        # print(title)
        item = Biquge()
        item['title'] = title
        text_list = tree.xpath('//div[@id="content"]/text()')
        te = ''
        for text in text_list:
            te += text.strip()
        item['text'] = te.strip()
        yield item

        next = tree.xpath('//div[@class="bottem1"]/a[4]/@href')[0]
        url = response.urljoin(next)
        print('爬取到第%d章' % self.i)
        self.i += 1
        print(url)
        yield scrapy.Request(url=url, callback=self.parse)
