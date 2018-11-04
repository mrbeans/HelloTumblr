# -*- coding: utf-8 -*-
import scrapy
import os
from ..Util.VideoHelper import ParseVideo,VideoGot
from ..items import TumblrItem
from redis import *
from ..Util.Conf import Config

class LikeSpider(scrapy.Spider):
    name = 'like'
    allowed_domains = ['tumblr.com']
    start_urls = ['https://www.tumblr.com/likes']
#test
    def start_requests(self):
        return [scrapy.http.FormRequest(self.start_urls[0],cookies=dict([l.split("=", 1) for l in Config.Cookies.split("; ")]),callback=self.parse)]

    def parse(self, response):
        ImageList,VideoList=[],[]
        videos=response.xpath('//div[@class="post_media"]//video/source/@src').extract()
        for video_url in videos:
            video_extension = os.path.splitext(video_url)[1][1:]
            
            if(video_extension!=None and len(video_extension)>0 and video_extension in Config.VideoExtensions):
                VideoList.append({'url':video_url,'title':os.path.basename(url)[:-4]})
            else:
                params=video_url.split('/')
                result=[param for param in params if param.startswith('tumblr_')][0]
                VideoList.append({'url':Config.OriginVideoUrl.format(result),'title':result})

        images=response.xpath('//div[@class="post_media"]//div[@class="photoset"]')
        for image in images:
            image_title=os.path.basename(image.xpath('//img/@data-pin-url').extract()[0])
            image_urls=image.xpath('//a[contains(@class,"photoset_photo")]/img/@src').extract()
            for (index,url) in enumerate(image_urls):
                ImageList.append({'url':url,'title':image_title+'-'+str(index+1)})

        print(VideoList)
        print(ImageList)

        for v in VideoList:
            Config.RedisDB.hset(name=LikeSpider.name+'-video',key=v.get('title'),value=v.get('url'))
        
        for i in ImageList:
            Config.RedisDB.hset(name=LikeSpider.name+'-image',key=i.get('title'),value=i.get('url'))

        next_url=response.xpath('//*[@id="next_page_link"]/@href')[0].extract()
        if(next_url!=None and len(next_url)>0):
            print(next_url)
            yield scrapy.http.FormRequest(Config.OriginUrl+next_url,cookies=dict([l.split("=", 1) for l in Config.Cookies.split("; ")]),callback=self.parse)

