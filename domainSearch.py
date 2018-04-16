#!python3

import requests, bs4, time
import RPi.GPIO as GPIO#For LED

#Domain check def
def domainCheck(url):
    url = 'http://tool.chinaz.com/DomainDel/?wd=' + url
    res = requests.get(url)
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text, 'html.parser')

    elems = soup.select('a[href*="http://www.icann.org"]')


    count = 1
    while count < 11:#Try 10 times at most
        if len(elems) == 0:
            time.sleep(1)
            res = requests.get(url)
            res.raise_for_status()
            soup = bs4.BeautifulSoup(res.text, 'html.parser')
            elems = soup.select('a[href*="http://www.icann.org"]')
            #print('Retry ' + str(count) + 'th time')
            count += 1
            if '该域名可注册' in res.text:
                elems.append('该域名可注册')      
        else:
            break

    #print('\n***\n')
    if len(elems) == 0:
        #print('Fail to find')
        return 0
    else:
        if elems[0] == '该域名可注册':
            #print('域名可注册！！！')
            return 1
        elif elems[0].getText() == 'pendingDelete':
            #print('域名处于删除期')
            return 2
        else:
            #print('域名已被注册')
            return 3

#LED defs
        
#All led off
#checkNum == 0, '检查失败！', white led on, GPIO4(7)&GND(9)
def whiteLED_on():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(4, GPIO.OUT)
    LEDcount = 0
    while LEDcount < 60:
        GPIO.output(4, GPIO.HIGH)
        time.sleep(1)
        GPIO.output(4, GPIO.LOW)
        time.sleep(1)
        LEDcount += 2
        
#checkNum == 1, '域名可注册！', green led on, GPIO18(12)&GND(14)
def greenLED_on():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(18, GPIO.OUT)
    LEDcount = 0
    while LEDcount < 60:
        GPIO.output(18, GPIO.HIGH)
        time.sleep(1)
        GPIO.output(18, GPIO.LOW)
        time.sleep(1)
        LEDcount += 2     
        
#checkNum == 2, '域名处于删除期！', blue led on, GPIO24(18)&GND(20)
def blueLED_on():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(24, GPIO.OUT)
    LEDcount = 0
    while LEDcount < 60:
        GPIO.output(24, GPIO.HIGH)
        time.sleep(1)
        GPIO.output(24, GPIO.LOW)
        time.sleep(1)
        LEDcount += 2
        
#checkNum == 3, '域名已被注册！', red led on, GPIO12(32)&GND(34)
def redLED_on():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(12, GPIO.OUT)
    LEDcount = 0
    while LEDcount < 60:
        GPIO.output(12, GPIO.HIGH)
        time.sleep(1)
        GPIO.output(12, GPIO.LOW)
        time.sleep(1)
        LEDcount += 2

        
urlInput = 'douban.com' #example domain
checkNum = domainCheck(urlInput)

if checkNum == 0:
    whiteLED_on()
    #print('whiteLED_on')
elif checkNum == 1:
    greenLED_on()
    #print('greenLED_on')
elif checkNum == 2:
    blueLED_on()
    #print('blueLED_on')
elif checkNum == 3:
    redLED_on()
    #print('redLED_on')

GPIO.cleanup()





    
