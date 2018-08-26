# HelloTumblr(使用scrapy构建的Tumblr爬虫)，抓取首页为：https://www.tumblr.com/dashboard，目前只支持图片和视频。

* 在tumblrSpider.py中的cookies字段中配置登陆后的cookies
* 在tumblrSpider.py中redis_db配置对应的redis地址和端口号以及DB
* 在tumblr上关闭“启用无限滚动”状态，路径为：我的-->设置-->首页-->启用无限滚动，因为爬虫要抓取“下一页”的按钮来循环抓取

* 此爬虫纯属学习使用，请控制抓取频率等，如果因个人因素导致账号被封等问题，我将不负任何责任

