#!python3

import os, requests, bs4, time


print('\n************************************\n')
def domainCheck():
    if c == '':
        domain = input('Please enter domain you wanna to check: ')
        print('\n---\n')
    else:
        domain = c
    url = 'http://tool.chinaz.com/DomainDel/?wd=' + domain
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
            print('Retry ' + str(count) + 'th time')
            count += 1
            if '该域名可注册' in res.text:
                elems.append('该域名可注册')      
        else:
            break

    print('\n---\n')
    if len(elems) == 0:
        print('Fail to find')
    else:
        if elems[0] == '该域名可注册':
            print('域名可注册！！！')
        elif elems[0].getText() == 'pendingDelete':
            print('域名处于删除期')
        else:
            print('域名已被注册，注册信息如下：')
            print(elems[0].getText())


c = ''
while True:
    domainCheck()
    print('\n************************************\n')
    c = input('Check another domain (press n to exit): ')
    if c == 'n':
        break
    print('\n---\n')
        
    

