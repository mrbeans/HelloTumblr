import scrapy
import os
from ..Util.VideoHelper import ParseVideo,VideoGot
from ..items import TumblrItem
from redis import *

cookies=""
video_extensions=['.avi','.rmvb','.rm','.asf','.divx','.mpg','.mpeg','.mpe','.wmv','.mp4','.mkv','.vob']
origin_url='https://www.tumblr.com'
origin_video_url='https://vtt.tumblr.com/{0}.mp4'
redis_db = StrictRedis(host='127.0.0.1', port=6379, db=0)

class TumblrSpider(scrapy.Spider):
  name='tumblr'
  allowed_domains=['tumblr.com']
  start_url=['https://www.tumblr.com/dashboard']

  def start_requests(self):
    return [scrapy.http.FormRequest(self.start_url[0],cookies=dict([l.split("=", 1) for l in cookies.split("; ")]),callback=self.parse)]

  def parse(self,response):
    videoList=[]
    videos=response.xpath('//div[@class="post_media"]//video/source/@src').extract()
    for video_url in videos:
      video_extension = os.path.splitext(video_url)[1][1:]
      if(video_extension!=None and len(video_extension)>0 and video_extension in video_extensions):
        videoList.append({'url':video_url,'title':os.path.basename(url)[:-4]})
      else:
        params=video_url.split('/')
        result=[param for param in params if param.startswith('tumblr_')][0]
        videoList.append({'url':origin_video_url.format(result),'title':result})

    images=response.xpath('//div[@class="post_media"]//img')
    imageList=[]
    for image in images:
      for i in image:
        url=i.xpath('@src').extract()[0]
        title=i.xpath('@data-pin-description').extract()[0]
        redis_db.hset(name='image',key=title,value=url)

    for video in videoList:
      url=video.get('url')
      title=video.get('title')
      redis_db.hset(name='video',key=title,value=url)

    next_url=response.xpath('//*[@id="next_page_link"]/@href')[0].extract()
    print(next_url)
    yield scrapy.http.FormRequest(origin_url+next_url,cookies=dict([l.split("=", 1) for l in cookies.split("; ")]),callback=self.parse)