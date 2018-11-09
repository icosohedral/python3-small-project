#python3

import requests, os

url_a = 'http://192.168.0.205/raid.cgi'
#url_b = 'http://192.168.0.210/raid.cgi'

def getRaid(url):
	try:
		res = requests.get(url)
	except:
		print('Can not get raid process.')
		return
	print('Url: ' + url[7:20])
	count = 1
	while len(res.text) > 10:
		res = requests.get(url)
		count += 1
		if count >= 15:
			print('Can not get raid process.')
			return
	print('Raid Process: ' + res.text)
	
getRaid(url_a)
#getRaid(url_b)