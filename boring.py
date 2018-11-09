#python3

import os, webbrowser

todoList = ['Twitch', 'Reddit', 'Twitter', 'Douban', 'Duowan', 'Steam', 'No, I wanna do anything.']
print('********FUN LIST********')
for i in range(len(todoList)):
    print(str(i+1) + '. ' + todoList[i])
print('************************')
choose = int(input('What you want to do now: ') )

if choose == 7:
    os._exit(0)
elif choose == 1:
    webbrowser.open(todoList[choose - 1] + '.tv')
elif choose == 5:
    webbrowser.open('http://bbs.duowan.com/forum-620-1.html')
elif choose == 6:
    os.popen("E:\steam\steam.exe")
else:
    webbrowser.open(todoList[choose - 1] + '.com')
