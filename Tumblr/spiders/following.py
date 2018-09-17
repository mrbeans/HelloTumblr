# -*- coding: utf-8 -*-
import scrapy
import os
from ..Util.VideoHelper import ParseVideo,VideoGot
from ..items import TumblrItem
from redis import *
from ..Util.Conf import Config

origin_url='https://www.tumblr.com'
origin_video_url='https://vtt.tumblr.com/{0}.mp4'
redis_db = StrictRedis(host='127.0.0.1', port=6379, db=0)

class FollowingSpider(scrapy.Spider):
    name = 'following'
    allowed_domains = ['tumblr.com']
    start_urls = ['http://tumblr.com/']
    
    def start_requests(self):
        return [scrapy.http.FormRequest(self.start_url[0],cookies=dict([l.split("=", 1) for l in Config.Cookies.split("; ")]),callback=self.parse)]

    def parse(self, response):
        pass
