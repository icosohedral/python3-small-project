#python3

import os, pyautogui, time, pyperclip
timeNow = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

print('*COLLECTING WORKLIST')

os.popen("E:\Evernote\Evernote\evernote.exe")

time.sleep(0.5)
pyautogui.size()
#window maximize
pyautogui.hotkey('winleft', 'up')
time.sleep(0.3)
#quick link     270,69
pyautogui.click(x=270, y=69, button='left')
time.sleep(0.4)
#move to work list text area      922,410
pyautogui.click(x=922, y=410, button='left')
time.sleep(0.2)
#select and copy CTRL_A&CTRL_C
pyautogui.hotkey('ctrlleft', 'a')
time.sleep(0.1)
pyautogui.hotkey('ctrlleft', 'c')
time.sleep(0.1)
pyautogui.click(x=922, y=410, button='left')
#text in clipboard
worklist = pyperclip.paste()
textPath = 'E:\\Cmder\\config\\python scripts\\Evernote Worklist\\'
with open(textPath + 'worklist', 'w', encoding='utf-8') as content:
        content.write(worklist + '\n\n****UPDATE TIME****\n' + timeNow + '\n*******************')
#close the window
pyautogui.hotkey('altleft', 'f4')
print('*DONE')
