# -*- coding: utf-8 -*-
import scrapy
from bs4 import BeautifulSoup as bs

def get_id(filename):
    with open(filename,'r') as f:
        ids = f.readlines()
    return ids

class TsSpider(scrapy.Spider):
    name = 'ts'
    allowed_domains = ['www.twitter.com']
    start_urls = ['https://www.twitter.com/']

    cookies_string = 'guest_id=v1%3A156290337013189180; _ga=GA1.2.51702724.1562903376; eu_cn=1; kdt=l0Wdd3uBhCIh5bDOMx57SECi9XTp8vB5Fz1eD7YR; remember_checked_on=0; csrf_same_site_set=1; lang=zh-cn; csrf_same_site=1; tfw_exp=0; _gid=GA1.2.659432508.1565665438; ct0=0482726f11533e526b074dc6262b8511; dnt=1; _sl=1; _twitter_sess=BAh7CSIKZmxhc2hJQzonQWN0aW9uQ29udHJvbGxlcjo6Rmxhc2g6OkZsYXNo%250ASGFzaHsABjoKQHVzZWR7ADoPY3JlYXRlZF9hdGwrCM1Ob4psAToMY3NyZl9p%250AZCIlZWIyZmMzMDJjYmYyYzYxMWRlYWY1YWY2YjMxYTg2MTA6B2lkIiU4OGU3%250AODhmYWI2ZmFlNWIzZDM4YTkzZjg3ODI4MjM2ZQ%253D%253D--2d142d6b3bd086594c025d1fe7d07d64a2f93f8c; personalization_id="v1_S7J8KtDCmVCvz4+wOJFf8Q=="; rweb_optin=side_no_out; _gat=1; gt=1161216930415632384'
    custom_settings = {
        "DEFAULT_REQUEST_HEADERS": {
            'authority': 'twitter.com',
            'method': 'GET',
            'scheme': 'https',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
            'Sec-Fetch-Mode': 'navigate',
            'sec - fetch - site': 'none',
            'Sec-Fetch-User': '?1',
        }
    }

    def __init__(self):
        cookies = {}
        for line in self.cookies_string.split(';'):
            key, value = line.split('=', 1)
            cookies[key] = value
        self.cookies = cookies

    def start_requests(self):
        #get_id将你要爬取的ID读出来，参数是你的文件路径
        # ids = get_id('put in you filepath')
        ids = ['0792z']
        for i in ids:
            url = 'https://www.twitter.com/' + i
            print(url)
            yield scrapy.Request(url, cookies=self.cookies, callback=self.parse, dont_filter=True)

    def parse(self,response):
        content = bs(response.text, 'lxml')
        blocks = content.find_all(class_='css-1dbjc4n')
        print(blocks)
