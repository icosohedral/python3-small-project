#python3

import os, sys

if len(sys.argv) == 1:
	url = input('Url or IP address: ')
else:
	url = str(sys.argv[1])
url = str(url)

#transfer dirsearch.py
scanPyPath = 'E:\Cmder\config\python scripts\webScan\dirsearch.py'
print('********SCANING********')
os.system('python ' + '"' + scanPyPath + '"' + ' -u ' + url + ' -e *')
print('********REPORT*********')

#rename and cat  report
folderName = url.replace('https://', '').replace(':443', '').replace(':80', '').replace('http://', '')
reportPath = 'E:\\Cmder\\config\\python scripts\\webScan\\reports\\' + folderName + '\\' 
os.listdir(reportPath)
dirs = os.listdir(reportPath)
if 'report' in dirs:
	os.remove(reportPath + 'report')
dirs = os.listdir(reportPath)
for file in dirs:
	try:
		os.rename(reportPath + file, reportPath + 'report')
	except:
		break
size = os.path.getsize(reportPath + 'report')
if size == 0:
	print('Nothing scaned)')
else:
	os.system('cat ' + '"' + reportPath + 'report' + '"')
print('\n***********************')