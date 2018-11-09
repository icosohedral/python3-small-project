#python3

import webbrowser, sys, os

if len(sys.argv) == 1:#with no argv
    keyword = input('What you wanna search: ')
else:#with argv
    keyword = ' '.join(sys.argv[1:])
    
url = 'es: ' + str(keyword)
webbrowser.open(url)
