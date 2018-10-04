from redis import *

class Config(object):
    OriginUrl='https://www.tumblr.com'
    VideoExtensions=['.avi','.rmvb','.rm','.asf','.divx','.mpg','.mpeg','.mpe','.wmv','.mp4','.mkv','.vob']
    OriginVideoUrl='https://vtt.tumblr.com/{0}.mp4'
    Cookies='rxx=18y86swstpn.12mtbl5c&v=1; _ga=GA1.2.948083063.1522484434; yx=7e5yfo9qops8r%26o%3D3%26f%3Dte; __utmz=189990958.1534599679.25.6.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided); pfp=YGwvLBoafCXSl5FmtWikeSxzJAc9iK5038s5ZWU6; pfs=SmriYeuWvUaC4n1KefeWtg5nkw; pfe=1542469045; pfu=253133512; language=%2Czh_CN; logged_in=1; nts=true; devicePixelRatio=1; _gid=GA1.2.484652317.1537712661; __utmc=189990958; capture=E9XykX5gNwRnfYHv8MVpledXk6U; pfg=eb95f8653016f9ac6cb28b1606d3b2c5f35a063f789ebac7483e610921ec18cf%23%7B%22gdpr_is_acceptable_age%22%3A1%2C%22exp%22%3A1569248748%2C%22vc%22%3A%22%22%7D%239169562853; tmgioct=5ba7a26cad42480423704550; documentWidth=1000; __utma=189990958.948083063.1522484434.1537714580.1537717135.38; __utmb=189990958.0.10.1537717135'
    RedisDB = StrictRedis(host='127.0.0.1', port=6379, db=0)

