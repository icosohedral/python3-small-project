#python3

import hashlib, sys, bs4, requests, json
 
def makeMD5(transText):
    appKey =                       					 #appkey
    salt = '3'                                       #salt
    secretKey =		 								 #密匙

    hashStr = appKey + transText + salt + secretKey
    sign = hashlib.md5(hashStr.encode(encoding='UTF-8')).hexdigest()
    sign = sign.upper()
    url = 'http://openapi.youdao.com/api?q=' + transText+ '&from=EN&to=zh_CHS&appKey=' + appKey + '&salt=' + salt + '&sign=' + sign
    return url

def wordGetTranslation(transText):
    url = makeMD5(transText)
    res = requests.get(url)
    res.raise_for_status()
    resultList = json.loads(res.content)['web'][0]['value']
    print('********TRANSLATION********')
    for i in range(len(resultList)):
        print(str(i+1) + '. ' + resultList[i])
    print('********END********')
    
def sentenceGetTranslation(transText):
    url = makeMD5(transText)
    res = requests.get(url)
    res.raise_for_status()
    resultList = json.loads(res.content)['translation']
    print('********TRANSLATION********')
    print(resultList[0])
    print('************END************')

if len(sys.argv) == 1:
	transText = input('What you wanna to translate: ')
	print('Translating...')
	try:
		sentenceGetTranslation(transText)
	except:
		print('出错了')
elif len(sys.argv) == 2:
	transText = sys.argv[1]
	print('Translating...')
	try:
		wordGetTranslation(transText)
	except:
		print('出错了')
else:
	transText = ' '.join(sys.argv[1:])
	print('Translating...')
	try:
		sentenceGetTranslation(transText)
	except:
		print('出错了')