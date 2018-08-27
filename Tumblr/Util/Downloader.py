import os,sys,math
import time
import requests

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

def download_file(url):
    response=requests.get(url)
    filename=os.path.split(url)[1]
    with open(filename,'wb') as File:
        File.write(response.content)
        print('download file:{0} done'.format(filename))

download_file('https://vt.media.tumblr.com/tumblr_p7ebpghMs71wy46rb.mp4')
download_file('http://a.hiphotos.baidu.com/image/pic/item/adaf2edda3cc7cd90df1ede83401213fb80e9127.jpg')
