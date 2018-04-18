# raspberrypi-projects
some simple projects on raspberry pi with python

#domainSearch.py
 <br>查询域名的注册状态，返回“已注册”/“未注册”/“删除期”/“查询失败”。
 <br>可以结合树莓派GPIO，通过LED小灯输出定时查询结果。


#solidotSave.py
<br>搜集solidot.org上面的文章，并且往存档末尾添加新搜集到的文章。丢在树莓派上定时运行。

#doubanSearch.py
<br>一个用于搜索豆瓣书影音的小脚本。
<br>基于cn.bing搜索条目链接（豆瓣自己的搜索引擎好像抓不到-。-），再进入链接获取具体信息。

#TwitterAPI.py
<br>t站真的是超良心，api简单易用，顺手记录几个简单的应用。
<br>用的是tweepy模块，文档在此：http://docs.tweepy.org/en/v3.5.0/api.html 。
<br>由于特殊需求，需要socks代理。然后到Twitter开发者网站上申请一个app，得到 consumer_key, consumer_secret, access_token, access_token_secret。设置好api对象（ api = tweepy.API(auth) ）后，就可以按照tweepy文档实现自己的需求了。

#getWeather.py 
<br>获取各地天气，基于新浪天气网页。首先利用 http://open.weather.sina.com.cn/api/location/getSuggestion/[CityName] 获得目标城市的链接，要是有多个匹配的话就取第一个，之后进入该链接获取各种天气数据。
<br>其实是可以获得未来10天内的天气和气温数据的，感觉太麻烦了，我就get了当前的和第二天的数据。还有，国内外的城市名和时间类名不太一样，需要不同处理（国内时间我直接用time()模块获取了~）。
