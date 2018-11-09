#python3

import os

recheck = input('Do you really wanna shutdown PC in 10 sec?(y/n) ')

if recheck == 'y':
	os.system("shutdown -s -t 10")
else:
	pass