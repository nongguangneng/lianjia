#coding:utf8

import urllib.request
import scrapy
from bs4 import BeautifulSoup
import json
import urllib.request
from lianjia.items import  HouseItem

class lianjia(scrapy.Spider):
    name = 'lianjia'
    begin_url = 'https://cq.lianjia.com/chengjiao/pg1'
    base_url = 'https://cq.lianjia.com/chengjiao/pg'

    def start_requests(self):
        req = urllib.request.urlopen(self.begin_url)
        result = req.read()
        soup = BeautifulSoup(result)
        max_num_json = soup.select('div.page-box.house-lst-page-box')[0]['page-data']
        max_num = json.loads(max_num_json)['totalPage']
        print('max_num is %d' % max_num)
        for index in range(1, 2):
            yield scrapy.Request(self.base_url + index, self.parse)

    def parse(self, response):
        print('response url:%s' % response.url)
        if (response.status == 200):
            html = BeautifulSoup(response.text)
            #print('max_num is %d' % max_num)
            title_divs = html.find('ul', class_='listContent').find_all('div', class_='title')
            for title_div in title_divs:
                one_house_url = title_div.find('a')['href']
                print(one_house_url)
                yield scrapy.Request(one_house_url, self.parseOne)

    def parseOne(self, response):
        if (response.status == 200):
            try:
                html = BeautifulSoup(response.text)
                house_item = HouseItem()
                house_item['total_price'] = html.find('span', class_='dealTotalPrice').find('i').get_text().strip()
                house_item['building_area'] = html.find('div', id='introduction').find('ul').find_all('li')[2].contents[1].string.replace('㎡', '').strip()
                house_item['inner_area'] = html.find('div', id='introduction').find('ul').find_all('li')[4].contents[1].string.replace('㎡', '').strip()
                try:
                    house_item['building_per_price'] = round(float(house_item['total_price'])/float(house_item['building_area']), 2)
                    house_item['inner_per_price'] = round(float(house_item['total_price'])/float(house_item['inner_area']), 2)
                except BaseException as e:
                    house_item['building_per_price'] = 0
                    house_item['inner_per_price'] = 0
                    print('遇到错误：%s, 跳过该内容' % e)
                house_item['toward'] = html.find('div', id='introduction').find('ul').find_all('li')[6].contents[1].string.strip()
                house_item['years_limit'] = html.find('div', id='introduction').find('ul').find_all('li')[-2].contents[1].string.strip()
                house_item['floor'] = html.find('div', id='introduction').find('ul').find_all('li')[1].contents[1].string.strip()
                house_item['decoration'] = html.find('div', id='introduction').find('ul').find_all('li')[9].contents[1].string.strip()
                house_item['building_huxing'] = html.find('div', id='introduction').find('ul').find_all('li')[5].contents[1].string.strip()
                house_item['room_huxing'] = html.find('div', id='introduction').find('ul').find_all('li')[0].contents[1].string.strip()
                house_item['floor_layout'] = html.find('div', id='introduction').find('ul').find_all('li')[-3].contents[1].string.strip()
                house_item['elevator'] = html.find('div', id='introduction').find('ul').find_all('li')[-1].contents[1].string.strip()
                house_item['url'] = response.url
                yield house_item
                # print(house_item)
            except BaseException as e:
                print('遇到错误：%s, 跳过该数据' % e)