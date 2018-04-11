#!python3
# Get posts on solidot.org

import os, requests, bs4, time

#fileTime = time.strftime('%Y-%m-%d_%H',time.localtime(time.time()))
url = 'https://www.solidot.org/'
res = requests.get(url)
res.raise_for_status()
solidotBS = bs4.BeautifulSoup(res.text, 'html.parser')

elems = solidotBS.select('div[class="p_mainnew"]')
elemsTitle = solidotBS.select("h2 a[href*='/story?sid=']")
print('Totally collect ' + str(len(elemsTitle)) +  ' Titles!')
print('Totally collect ' + str(len(elems)) +  ' posts!')

pwd = '/home/pi/solidot/news/'
if 'solidot.txt' not in ''.join(os.listdir(pwd)):
    solidotFile = open(pwd+'solidot.txt', 'w')
    for i in range(len(elems)):
        title = ' '.join(elemsTitle[i].getText().split())
        post = ' '.join(elems[i].getText().split()) #single post string
        solidotFile.write(title + '\n\n' + post + '\n ----------\n')
        print('New writing in ' + str(i+1) + 'th post...')
else:
    solidotFile = open(pwd+'solidot.txt', 'r')
    solidotText = solidotFile.read()
    for i in range(len(elems)):
        if elemsTitle[i].getText() not in solidotText:
            solidotFile.close()
            solidotFile = open(pwd+'solidot.txt', 'a')
            title = ' '.join(elemsTitle[i].getText().split())
            post = ' '.join(elems[i].getText().split()) #single post string
            solidotFile.write(title + '\n\n' + post + '\n ----------\n')
            print('Add in ' + str(i+1) + 'th post...')            

solidotFile.close()
print('Done!  ', end='')
print('Time is: ' + time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
    

