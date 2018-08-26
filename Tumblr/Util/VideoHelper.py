import requests
import json

class VideoGot(object):
  @staticmethod
  def get_tumblr_video_origin_url(url):
    api_url='https://videogot.net/'
    postdata={
      'url':url
    }
    proxy={
      'http':'115.159.143.108:80',
      'https':'43.239.178.78:8888'
    }
    response=requests.post(api_url,data=postdata,proxies=proxy)
    responseList=json.loads(response.content.decode('gbk'))
    if(responseList==None or len(responseList)<=0 and isinstance(responseList,list)==False):
      return []
    print(url)
    return [video.get('videoUrl') for video in responseList]

#Video.get_tumblr_video_origin_url('https://saner-1100.tumblr.com/video_file/t:OlATVEOd6rT-topwEdom4g/177125555410/tumblr_p4y4a7sQfE1x58rtg')

class ParseVideo(object):
  @staticmethod
  def get_tumblr_video_origin_url(url):
    api_url='https://www.parsevideo.com/api.php'
    postdata={
      'url':url,
      'hash': 'f62bb240eec1ac36738b9e2ccb31400d'
    }
    response=requests.post(api_url,data=postdata)
    responseList=json.loads(response.content.decode('utf-8'))
    if(responseList==None or len(responseList)<=0 or responseList.get('total')<=0):
      return []
    videos=responseList.get('video')
    return [{'url':video.get('url'),'title':video.get('desc')} for video in videos]

class Test(object):
  @staticmethod
  def test_func():
    url='https://trungtranxx.tumblr.com/video_file/t:n3Xv3MR-_2HEFIKEeeAU4A/177352989301/tumblr_pdbbfvWLgv1v3fnbt/480'
    params=url.split('/')
    result=[param for param in params if param.startswith('tumblr_')][0]
    print(result[0])

Test.test_func()
#ParseVideo.get_tumblr_video_origin_url('https://minhchau11.tumblr.com/video_file/t:lj7eVPvsH8sFc51p_CTBaw/177370462165/tumblr_p38v8pEBFJ1w7a5n2')