#coding:utf8

import urllib.request
import scrapy
from bs4 import BeautifulSoup
import json

class lianjia(scrapy.Spider):
    name = 'lianjia'
    start_urls = ['https://cq.lianjia.com/chengjiao/pg1']

    def parse(self, response):
        print('response url:%s' % response.url)
        if (response.status == 200):
            html = BeautifulSoup(response.text)
            max_num_json = html.select('div.page-box.house-lst-page-box')[0]['page-data']
            max_num = json.loads(max_num_json)['totalPage']
            #print('max_num is %d' % max_num)
            title_divs = html.find('ul', class_='listContent').find_all('div', class_='title')
            for title_div in title_divs:
                one_house_url = title_div.find('a')['href']
                print(one_house_url)
