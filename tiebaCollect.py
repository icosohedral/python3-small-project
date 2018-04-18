#!python3

import requests, bs4, time

def getPost(userName):  
    un = str(userName.encode('GBK'))[2:-1].replace(r'\x', '%')#decode Chinese to GBK str
    pageUrl = 'http://tieba.baidu.com/f/search/ures?kw=&qw=&rn=30&un=' + un + '&only_thread=&sm=1&sd=&ed=&pn='
    page = 1
    while True:
        url = pageUrl + str(page)
        res = requests.get(url)
        res.raise_for_status()
        soup = bs4.BeautifulSoup(res.text, 'html.parser')
        elemsTitle = soup.select('[class=p_title]')
        elemsContent = soup.select('[class=p_content]')
        elemsForum = soup.select('a[class="p_forum"]')
        elemsDate = soup.select('font[class*="p_date"]')
        postList= []
        for i in range(len(elemsTitle)):
            try:
                title = elemsTitle[i].getText()
                content = elemsContent[i].getText()
                forum = elemsForum[i].getText()
                date = elemsDate[i].getText()
                postList.append('\n************\n*标题：' + title + '\n*内容：' + content + '\n*贴吧：' + forum + '\n*发帖时间：' + date)
            except:
                print('出错了')
        if len(postList) != 0:
            collectFile = open('TBpost_' + userName + '.txt', 'a', encoding='utf-8')
            collectFile.write(''.join(postList))
            collectFile.close()
        else:#if len(postList)==0, we know that all posts have been collected, so break this loop
            break
        print('Page ' + str(page) + ' done.')
        time.sleep(0.8)
        page += 1
    print('All posts have been collected.')
    print('\nRemoving repeat...')
    removeRepeat(userName)

def removeRepeat(fileName):#remove repeat posts
    file = open('TBpost_' + fileName + '.txt', 'r', encoding='utf-8')
    fileStr = file.read()
    fileStrListR = fileStr.split('\n************\n')
    fileStrListNR = list(set(fileStrListR))
    fileStrListNR.sort(key=fileStrListR.index)
    file.close()
    file = open('TBpost_' + fileName + '.txt', 'w', encoding='utf-8')
    file.write('\n************\n'.join(fileStrListNR))
    print('Remove Repeats Successful!')
    
name = input('User name is: ')
getPost(name)
