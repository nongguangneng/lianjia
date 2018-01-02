# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class HouseItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    total_price = scrapy.Field()
    building_area = scrapy.Field()
    inner_area = scrapy.Field()
    building_per_price = scrapy.Field()
    inner_per_price = scrapy.Field()
    toward = scrapy.Field()
    years_limit = scrapy.Field()
    floor = scrapy.Field()
    # 是否装修
    decoration = scrapy.Field()
    # 建筑户型，大平层
    building_huxing = scrapy.Field()
    # 房间户型，四房两厅
    room_huxing = scrapy.Field()
    #两梯两户
    floor_layout = scrapy.Field()
    # 有电梯
    elevator = scrapy.Field()
    url = scrapy.Field()

