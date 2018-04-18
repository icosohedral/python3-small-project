#!python3

import requests, json

UID = ''
KEY = ''
API = 'https://api.seniverse.com/v3/weather/now.json?'

def getUrl(location):
    url = API + 'key=' + KEY + '&location=' + location
    return url

def getWeather(location):
    url = getUrl(location)
    weatherJson = json.loads(requests.get(url).content)
    city = weatherJson['results'][0]['location']['name']
    weather = weatherJson['results'][0]['now']['text']
    temperature = weatherJson['results'][0]['now']['temperature']
    updateTime = weatherJson['results'][0]['last_update']
    updateTime = updateTime[:16].replace('T', ' ')
    print('城市：' + city)
    print('天气：' + weather)
    print('温度：' + temperature + '°C')
    print('更新时间：' + updateTime)
    
while True:
    print('******')
    Location = input('The city is: ')
    print('******')
    try:
        getWeather(Location)
    except:
        print('city date no found')
