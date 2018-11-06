# -*- coding: utf-8 -*-
import scrapy, xlrd
from lxml import etree
from ..items import Test03TaobaoItem


class TaobaoSpider(scrapy.Spider):
    name = 'taobao'
    allowed_domains = ['item.taobao.com', 'detail.tmall.com']
    start_urls = ['https://detail.tmall.com/item.htm?id=536493211279&ns=1&abbucket=2']

    def __init__(self):
        self.file_path = r'F:\Python\ProjectPy\0709\第4阶段_爬虫\week2\淘宝\淘宝商品--白酒.xlsx'
        data = xlrd.open_workbook(self.file_path)
        # 获取sheet(表格的某一页)sheet是页名
        self.table = data.sheet_by_name('Sheet')
        # 获取表的行数
        self.nrows = self.table.nrows

    def parse(self, response):

        # 链接--生成器（从表格里取链接）
        for i in range(self.nrows):
            # 获取链接（下标从0开始）
            if i == 0:
                continue
            # 第i行的第5列
            url = self.table.cell(i, 5).value

            new_url = response.urljoin(url)
            # print(new_url)
            # print()

            # # 如果连接是天猫,回调天猫页面函数，否则回调淘宝页面函数
            if url[:6] == '//deta':
                # print('天猫')
                yield scrapy.Request(url=new_url, callback=self.tianmao)
            else:
                # print('淘宝')
                yield scrapy.Request(url=new_url, callback=self.taobao)

    def tianmao(self, response):
        tree = etree.HTML(response.text)
        name = tree.xpath('//div[@class="tb-detail-hd"]/h1/text()')[0].strip()
        price = tree.xpath('//div[@class="tm-promo-price"]/span[@class="tm-price"]/text()')[0].strip()
        pingjia = tree.xpath('//div[@class="bd"]//em[@class="J_ReviewsCount"]/text()')[0].strip()
        print('天猫')
        # print(response.text)
        print(name)
        print(price)
        print(pingjia)

    def taobao(self, response):
        tree = etree.HTML(response.text)
        name = tree.xpath('//div[@id="J_Title"]/h3/text()')[0].strip()
        print('淘宝')
        # print(response.text)
        print(name)
