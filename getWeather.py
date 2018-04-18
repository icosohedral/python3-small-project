#!python3

import requests, json, bs4, time, pprint

def citySearch(city):
    searchUrl = 'http://open.weather.sina.com.cn/api/location/getSuggestion/' + city
    res = requests.get(searchUrl)
    res.raise_for_status()
    cityJson = json.loads(res.content)['result']['data']['data']
    city = cityJson[0]['url']
    url = 'http://weather.sina.com.cn/' + city
    return url

def getWeather(city):
    url = citySearch(city)
    res = requests.get(url)
    res.raise_for_status()
    res.encoding='utf-8'
    soup = bs4.BeautifulSoup(res.text, 'html.parser')

    try:
        cityName = soup.select('[class=slider_ct_enname]')[0].getText()
        localTime = soup.select('[class=slider_ct_info]')[1].getText()[16:]
    except:
        cityName = soup.select('[class=slider_ct_name]')[0].getText()
        localTime = time.strftime('%m-%d %H:%M:%S', time.localtime())
    
    
    tempList = soup.select('[class=wt_fc_c0_i_temp]')
    tempNow = tempList[0].getText()
    if '/' in tempNow:
        tempNow = tempList[0].getText().split(' / ')[1] + '到' + tempList[0].getText().split(' / ')[0]
    tempNext = tempList[1].getText().split(' / ')[1] + '到' + tempList[1].getText().split(' / ')[0]

    weatherList = soup.select('[class^=icons0_wt]')
    weatherNow = weatherList[0].get('alt')
    weatherNextDay = weatherList[1].get('alt')
    weatherNextNight = weatherList[2].get('alt')

    print('城市：' + cityName)
    print('当地时间：' + localTime)
    print('当前天气：' + weatherNow + '  ' + tempNow)
    #print('当前温度：' + tempNow)
    print('明日天气：' + weatherNextDay + '  ' + tempNext)
    #print('明日温度：' + tempNext)
    

while True:
    print('************')
    City = input('City Name: ')
    print('******')
    try:
        getWeather(City)
    except:
        print('出错了！')
