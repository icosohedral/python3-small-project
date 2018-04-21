#!python3

import requests, bs4, re

def mebookCollect():
    pageUrl = 'http://mebook.cc/page/'
    page = 1
    while True:
        url = pageUrl + str(page)
        res = requests.get(url)
        res.raise_for_status()
        soup = bs4.BeautifulSoup(res.text, 'html.parser')
        elemsTitle = soup.select('.list h2 a')
        elemsIntro = soup.select('.info + p')
        if len(elemsTitle) != 0:
            bookInfo = []
            for i in range(len(elemsIntro)):
                try:
                    titleText = elemsTitle[i].get('title')
                    bookLink = elemsTitle[i].get('href')
                except:
                    titleText = 'None'
                    bookLink = 'None'
                try:
                    title = titleText.split('》')[0][1:]
                except:
                    title = 'None'
                try:
                    authorName = titleText.split('》')[1].split('（')[0]
                except:
                    try:
                        authorName = authorName = titleText.split('》')[1].split('(')[0]
                    except:
                        authorName = 'None'
                try:
                    intro = ''.join(elemsIntro[i].getText().strip().replace('&', '').replace('内容简介', '').split())
                except:
                    intro = 'None'
                if bookLink != 'None':
                    try:
                        dlLink = 'http://mebook.cc/download.php?id=' + bookLink[17:-5]
                        res = requests.get(dlLink)
                        res.raise_for_status()
                        soup = bs4.BeautifulSoup(res.text, 'html.parser')

                        panPWD = soup.find(text=re.compile('百度网盘密码'))[12:16]
                        panLink = soup.select('a[href*="https://pan.baidu.com/"]')[0].get('href')
                    except:
                        panPWD = 'None'
                        panLink = 'None'
                else:
                    panPWD = 'None'
                    panLink = 'None'
                bookInfo.append('\n*****\n*书名：' + title + '\n*作者：' +  authorName + '\n*简介：' + intro + '\n*下载：<' + panPWD + '>' + panLink)
            print('Page ' + str(page) + ' has done.')
            page += 1
            with open('mebookCollect.txt', 'a', encoding = 'utf-8') as file:
                file.write(''.join(bookInfo))
            
        else:
            print('All books have been collected!')
            return
        

mebookCollect()
