from redis import *

class Config(object):
    VideoExtensions=['.avi','.rmvb','.rm','.asf','.divx','.mpg','.mpeg','.mpe','.wmv','.mp4','.mkv','.vob']
    OriginVideoUrl='https://vtt.tumblr.com/{0}.mp4'
    Cookies='rxx=18y86swstpn.12mtbl5c&v=1; _ga=GA1.2.948083063.1522484434; yx=7e5yfo9qops8r%26o%3D3%26f%3Dte; __utmz=189990958.1534599679.25.6.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided); pfp=YGwvLBoafCXSl5FmtWikeSxzJAc9iK5038s5ZWU6; pfs=SmriYeuWvUaC4n1KefeWtg5nkw; pfe=1542469045; pfu=253133512; language=%2Czh_CN; logged_in=1; pfx=0146f73198a7712e5a17352822771acd7e1fb6c9d9df089ee7cb99eb8b346e32%230%231125946963; _gid=GA1.2.366437559.1536943636; __utmc=189990958; nts=true; devicePixelRatio=1; capture=E9XykX5gNwRnfYHv8MVpledXk6U; documentWidth=1008; pfg=4edf4225061304d71817ff1ece17ff206b8c92558cb7817ab8468ea6b1963113%23%7B%22gdpr_is_acceptable_age%22%3A1%2C%22exp%22%3A1568482912%2C%22vc%22%3A%22%22%7D%237105893171; tmgioct=5b9bf2e0495a560578983360; __utma=189990958.948083063.1522484434.1536943637.1537028225.34; __utmb=189990958.0.10.1537028225'
    RedisDB = StrictRedis(host='127.0.0.1', port=6379, db=0)

