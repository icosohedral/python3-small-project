#python3

import os

recheck = input('Do you really wanna reboot in 10 sec?(y/n) ')

if recheck == 'y':
	os.system("shutdown -r -t 10")
else:
	pass