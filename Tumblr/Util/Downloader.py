import os,sys,math
import time
import requests
from redis import *

redis_db = StrictRedis(host='127.0.0.1', port=6379, db=0)

def progressbar(cur,total):  
    percent = '{:.2%}'.format(cur / total)  
    sys.stdout.write('\r')  
    sys.stdout.write('[%-50s] %s' % ( '=' * int(math.floor(cur * 50 /total)),percent))  
    sys.stdout.flush()  
    if cur == total:  
        sys.stdout.write('\n')  

'''for i in range(0,100):
    progressbar(i+1,100)
    time.sleep(0.5)'''

#I:\tumblr
def download_file(url,filename=None):
    response=requests.get(url)
    if(filename==None):
        filename=os.path.split(url)[1]
    filename='I:/tumblr/{0}'.format(filename)
    with open(filename,'wb+') as File:
        File.write(response.content)
        print('download file:{0} done'.format(filename))

def start_download(type='video'):
    files=redis_db.hgetall(name=type)
    if(files==None or len(files)<=0):
        print('找不到类型为{0}的文件，请检查。'.format(type))
        return
    for (name,value) in files.items():
        download_file(value.decode('gb2312'))

if __name__=='__main__':
    args=sys.argv
    if(len(args)<=1):
        start_download('video')
        print('------------所有视频下载完毕------------')
        start_download('image')
        print('------------所有图片下载完毕------------')
    else:
        start_download(args[1])
