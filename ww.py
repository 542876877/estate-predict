# -*- coding: utf-8 -*-
import scrapy
from scrapy.contrib.spiders import CrawlSpider
from scrapy.http import Request
from scrapy.selector import Selector
from vv.items import VvItem

class Vv(CrawlSpider):
    name = "vv"
        start_urls = ['http://bj.lianjia.com/ershoufang/']
    def parse(self,response):
        item = VvItem()
        selector = Selector(response)
        houses = selector.xpath('//div[@class="info clear"]')

        for eachhouse in houses:
            title=eachhouse.xpath('div[@class="title"]/a/text()').extract()
            fullTitle = ''
            for each in title:#/html/body/div[4]/div[1]/ul/li[2]/div[1]/div[2]/div/text()
                fullTitle += each#/html/body/div[4]/div[1]/ul/li[2]/div[1]/div[3]/div/text()
            condition = eachhouse.xpath('div[@class="address"]/div[@class="houseInfo"]/text()').extract()[0]
            address = eachhouse.xpath('div[@class="flood"]/div[@class="positionInfo"]/a/text()').extract()[0]
            lc =eachhouse .xpath('div[@class="flood"]/div[@class="positionInfo"]/text()').extract()[0]
            tag = eachhouse.xpath('div[@class="followInfo"]/text()').extract()[0]
            price = eachhouse.xpath('div[@class="priceInfo"]/div[@class="totalPrice"]/span/text()').extract()[0]

            item['title']=fullTitle.replace("\r\n","").strip()
            item['condition'] =condition .replace("\n"," ").strip()
            item['address'] = address.replace("\n", " ").strip()
            item['lc'] = lc.replace("\n", " ").strip()
            item['tag'] = tag.replace("\n", " ").strip()
            item['price'] = price.replace("\n", " ").strip()
            yield item
               for i in range(1,2):
            yield Request('http://bj.lianjia.com/ershoufang/pg'+str(i)+'/', callback=self.parse)  # 完整地址
piplines.py:
# -*- coding: utf-8 -*-
from openpyxl import Workbook
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class VvPipeline(object):
    wb = Workbook()
    ws = wb.active
    ws.append(['title','condition','address','lc','tag','price(元/月)'])  # 设置表头,'main7','main8','main9','main10'

    def process_item(self, item, spider):  # 工序具体内容
        line = [item['title'],item['condition'],item['address'],item['lc'],item['tag'],item['price']]  # 把数据中每一项整理出来,item['main7'],item['main8'],item['main9'],item['main10']
        self.ws.append(line)  # 将数据以行的形式添加到xlsx中
        self.wb.save('lianjia.xlsx')  # 保存xlsx文件
        return item

Items.py:
# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

from scrapy import Item, Field
class VvItem(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = Field()
    condition=Field()
    address = Field()
    lc = Field()
    tag= Field()
    price = Field()


