#!python3

import re, requests, bs4

#bing search
def linkCollect(searchType,Name):#base on cn.bing, searchType = 读书/音乐/电影
    #Name = input('Please enter the book name you wanna search:')
    print('\n********\nSearching...')
    url = 'https://cn.bing.com/search?q=' + Name + '+豆瓣' + searchType
    res = requests.get(url)
    res.raise_for_status()
    linkSoup = bs4.BeautifulSoup(res.text, 'html.parser')
    elems = linkSoup.select('.b_caption')
    
    url = elems[0].cite.getText()#get res from target website
    res = requests.get(url)
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    print('********\n')
    return soup
    

#book
def bookCollect(Name):
    soup = linkCollect('读书',Name)
    #get author
    author = soup.select('span.pl + a[href]')[0].getText()#[0]author, [1]translator
    #get rate
    rate = soup.select('strong.rating_num')[0].getText().strip()#strip() for remove space
    #get intro
    intro = soup.select('div.intro')[0].getText()
    #return
    print('书名：' + Name)
    print('作者：' + "".join(author.split()))# "".join(str.split()) del \n and space
    print('评分：' + rate)
    print('简介：' + "".join(intro.split()))

#movie
def movieCollect(Name):
    soup = linkCollect('电影',Name)
    #get director
    directorList = soup.select('a[rel="v:directedBy"]')
    director = ''
    for i in range(len(directorList)):#if there are more than one director
        director = director + directorList[i].getText() + '/'
    director = director[:-1]#remove the last '/'
    #get rate
    rate = float(soup.select('strong[property="v:average"]')[0].getText())
    #get type
    movieTypeList = soup.select('span[property="v:genre"]')
    movieType = ''
    for i in range(len(movieTypeList)):
        movieType = movieType + movieTypeList[i].getText() + '/'
    movieType = movieType[:-1]
    #get intro
    intro = ''.join(soup.select('span[property="v:summary"]')[0].getText().split())
    #return
    print('电影名：' + Name)
    print('导演：' + director)
    print('类型：' + movieType)
    print('评分：' + str(rate))
    print('简介：' + intro)

#music
def musicCollect(Name):
    soup = linkCollect('音乐',Name)
    #get performer
    performerRegex = re.compile(r'又名.*')
    if performerRegex.search(soup.select('span.pl')[0].getText()) != None:
        performer = soup.select('span.pl')[1].getText()
    else:
        performer = soup.select('span.pl')[0].getText()
    performer = ' '.join(performer.split()[1:])
    if ' / ' in performer:
        performer = performer.replace(' / ', '/')
    #get musicStyle
    info = soup.select('div#info')
    infoList = info[0].getText().split('\n')
    for i in range(len(infoList)):
        if '流派' in infoList[i]:
            musicStyle = infoList[i].replace('流派:\xa0', '')
    #get rate
    rate = float(soup.select('strong[property="v:average"]')[0].getText())
    #get intro
    intro = soup.select('span[property="v:summary"]')[0].getText().strip()
    #return
    print('专辑名：' + Name)
    print('表演者：' + performer)
    print('流派：' + musicStyle)
    print('评分：' + str(rate))
    print('简介：' + intro)
        

def collect():
    searchType = input('What type you wanna search(读书/电影/音乐): ')
    while True:
        while searchType != '读书' and searchType != '电影' and searchType != '音乐':
            searchType = input('Please enter the right type!(读书/电影/音乐/[e] to EXIT)')
            if searchType == 'e':
                break
        if searchType == '读书':
            Name = input('What is the book\'s name: ')
            try:
                bookCollect(Name)
            except:
                print('There is something wrong')
        elif searchType == '电影':
            Name = input('What is the movie\'s name: ')
            try:
                movieCollect(Name)
            except:
                print('There is something wrong')
        elif searchType == '音乐':
            Name = input('What is the CD\'s name: ')
            try:
                musicCollect(Name)
            except:
                print('There is something wrong')
        elif searchType == 'e':
            break
        else:
            continue
        print('\n**********\n')

        action = input('Enter [c] to CONTINUE/[t] to CHOOSE TYPE/[e] to EXIT: ')
        while action != 'c' and action != 't' and action != 'e':
            action = input('Enter [c] to CONTINUE/[t] to CHOOSE TYPE/[e] to EXIT: ')
        if action == 'c':
            pass
        elif action == 'e':
            break
        else:
            searchType = input('What type you wanna search(读书/电影/音乐): ')
                                
#let's run this script now
collect()
