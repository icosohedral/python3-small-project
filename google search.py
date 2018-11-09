#python3

import webbrowser, sys

if len(sys.argv) == 1:
    keyword = input('What you wanna search: ')
else:
	keyword = ' '.join(sys.argv[1:])
	
url = 'https://www.google.com/search?q=' + str(keyword)
webbrowser.open(url)