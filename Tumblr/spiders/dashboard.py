# -*- coding: utf-8 -*-
import scrapy
import os
from ..Util.VideoHelper import ParseVideo,VideoGot
from ..items import TumblrItem
from redis import *
from ..Util.Conf import Config

class DashboardSpider(scrapy.Spider):
    name = 'dashboard'
    allowed_domains = ['tumblr.com']
    start_urls = ['https://www.tumblr.com/following']

    def start_requests(self):
        return [scrapy.http.FormRequest(self.start_urls[0],cookies=dict([l.split("=", 1) for l in Config.Cookies.split("; ")]),callback=self.parse_following_list)]

    def parse_detail(self, response):
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
            Config.RedisDB.hset(name=DashboardSpider.name+'-video',key=v.get('title'),value=v.get('url'))
        
        for i in ImageList:
            Config.RedisDB.hset(name=DashboardSpider.name+'-image',key=i.get('title'),value=i.get('url'))

        next_url=response.xpath('//*[@id="next_page_link"]/@href')[0].extract()
        print(next_url)
        yield scrapy.http.FormRequest(Config.OriginUrl+next_url,cookies=dict([l.split("=", 1) for l in Config.Cookies.split("; ")]),callback=self.parse_detail)
    
    def parse_each_following(self):
        Following_Users=Config.RedisDB.hgetall(name=DashboardSpider.name+'-following')
        if(Following_List==None or len(Following_List)<=0):
            print('can not get any following user from redis')
            return
        for user in Following_Users:
            print('now get resource from following user : '.format(user.key))
            yield scrapy.http.FormRequest(user.value,cookies=dict([l.split("=", 1) for l in Config.Cookies.split("; ")]),callback=self.parse_detail)
            
    def parse_following_list(self,response):
        following_user=response.xpath('//div[@id="left_column"]/div[contains(@class,"follower") and not(@id="invite_someone")]')
        for user in following_user:
            name_link=user.xpath('//a[@class="name-link"]')[0]
            name=name_link.xpath('text()')[0].extract()
            link=name_link.xpath('@href')[0].extract()
            Config.RedisDB.hset(name=DashboardSpider.name+'-following',key=name,value=link)
            print('get new user : {0}'.format(name))
        
        next_url=response.xpath('div[@id="pagination"]/a/@href')[0].extract()
        if(next_url!=None and len(next_url)>0):
            print('next url is : '.format(next_url))
            yield scrapy.http.FormRequest(Config.OriginUrl+next_url,cookies=dict([l.split("=", 1) for l in Config.Cookies.split("; ")]),callback=self.parse_following_list)
        else:
            self.parse_each_following()
