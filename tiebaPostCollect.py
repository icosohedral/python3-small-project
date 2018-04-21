#!python3

import requests, bs4, re, time, sys
non_bmp_map = dict.fromkeys(range(0x10000, sys.maxunicode + 1), 0xfffd)
#x.translate(non_bmp_map)

def tiebaPostCollect(name):
    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'
        }
    tbName = str(name.encode('GBK'))[2:-1].replace(r'\x', '%')
    pageUrl = 'http://tieba.baidu.com/f?kw=' + tbName + '&ie=utf-8&pn='
    
    indexUrl = pageUrl + str(0)
    res = requests.get(indexUrl)
    #res.encoding = ('utf8')
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    titleCount = int(soup.select('span[class="red_text"]')[0].getText())
    pageCount = 0
    while pageCount < titleCount:
        url = pageUrl + str(pageCount)
        res = requests.get(url)
        res.raise_for_status()
        soup = bs4.BeautifulSoup(res.text, 'html.parser')
        elemsTitle = soup.select('a[href*="/p/"]')
        elemsAuthor = soup.select('[class=frs-author-name-wrap]')
        elemsDate = soup.select('[class*=is_show_create_time]')
        tl = len(elemsTitle)
        al = len(elemsAuthor)
        dl = len(elemsDate)
        if tl <= al:
            if tl <= dl:
                lenth = tl
            else:
                lenth = dl
        else:
            if al <= dl:
                lenth = al
            else:
                lenth =dl
        if lenth != 0:
            file = open('tiebaPost_' + name + '.txt','a', encoding='utf-8')
            postList = []
            for i in range(lenth):                
                title = '*****\n*标题：' + elemsTitle[i].getText() + '\n'
                author = '*作者：' + elemsAuthor[i].getText() + '\n'
                date = '*时间：' + elemsDate[i].getText() + '\n'
                postList.append(title + author + date)
                print((title + author + date).translate(non_bmp_map))
            file.write(''.join(postList))
            file.close()
            pageCount += 50
            print('Page ' + str(int(pageCount / 50)) + ' done. There are ' + str(len(postList)) +' posts in this page.') 
            #time.sleep(0.3)
        else:
            break
    print('All titles have been collected!')



while True:
    tiebaName = input('输入贴吧名：')
    tiebaPostCollect(tiebaName)
