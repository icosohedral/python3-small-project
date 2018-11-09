#python3

import bs4, requests, sys

if len(sys.argv) == 1:
    keyword = str(input('What you wanna search: '))
else:
    textList = sys.argv[1:]
    keyword = ' '.join(textList)

url = 'https://cn.bing.com/search?q=' + keyword
res = requests.get(url)
res.raise_for_status()
linkSoup = bs4.BeautifulSoup(res.text, 'html.parser')
elems = linkSoup.select('.b_caption')

print('\n********RESULT********\n')
for i in range(len(elems)):
    print('*' + str(i+1) + '. ' + elems[i].getText() + '\n')
print('********END********')
