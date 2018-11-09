import os, sys

print('*****WORK LIST*****')
try:
	if sys.argv[1] == 'update':
		pyPath = 'E:\Cmder\config\python scripts\Evernote Worklist\\'
		os.system('python ' + '"' + pyPath + 'WorkArr AutoSave.py' + '"' )
	else:
		raise argvError('argvError')
except:
	path = 'E:\\Cmder\\config\\python scripts\\Evernote Worklist\\worklist'
	os.system('cat ' + '"' + path + '"')
	print('\n*Enter ' + '"work update"' + ' to update the list.')
print('*******************')