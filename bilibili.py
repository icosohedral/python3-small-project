import requests, os, json, sys


class Bilibili(object):
    def __init__(self):
        return

    def help(self):
        print('''Usage: bilibili [Option]
       [live]    Get Latest Live Information.
       [video]   Get Latest Video Information.
       [comment] Get Latest Comments.
       [barrage] Get Latest Barrage.
''')
    
    def getJson(self, url):
        headers_live = {'Host': 'api.live.bilibili.com',
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36',
                    'Cookie': 
                        }  
        headers_vc = {'Host': 'api.vc.bilibili.com',
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36',
                    'Cookie': 
                        }  
        headers_member = {'Host': 'member.bilibili.com',
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36',
                    'Cookie': 
                        }  
        headers_api = {'Host': 'api.bilibili.com',
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36',
                    'Cookie': 
                        }  
        try:
            if 'live' in url:
                headers = headers_live
            elif 'member' in url:
                headers = headers_member
            elif 'vc' in url:
                headers = headers_vc
            else:
                headers = headers_api
            res = requests.get(url, headers=headers)
            res.raise_for_status()
        except:
            print('[Error] Get API Failed.')
            os._exit(1)
        res.encoding = 'utf-8'
        js = json.loads(res.content)
        return js

    def getLiveStatus(self):
        url = 'https://api.live.bilibili.com/relation/v1/feed/feed_list?page=1&pagesize=5'
        js = self.getJson(url)
        if js['code'] == 0:
            for liveRoom in js['data']['list']:
                print('''
    Steamer: %s
    Title: %s''' % (liveRoom['uname'], liveRoom['title']))
        else:
            print('[Error] Get API Failed, Error code:[%s], Error message: [%s].' % (str(js['code']), js['message']))

    def getNewVideo(self):
        url = 'https://api.vc.bilibili.com/dynamic_svr/v1/dynamic_svr/dynamic_new?uid=3041876&type_list=8'
        js = self.getJson(url)
        if js['code'] == 0:
            c = 0
            for obj in js['data']['cards']:
                if c == 5:
                    break
                c += 1
                name = obj['desc']['user_profile']['info']['uname']
                contentJs = json.loads(obj['card'])
                title = contentJs['title']
                description = contentJs['desc']
                if len(description) > 75:
                    description = description[:75] + '...'
                print('''
    Title: %s
    UPer: %s
    Description: %s''' % (title, name, description))
        else:
            print('[Error] Get API Failed, Error code:[%s], Error message: [%s].' % (str(js['code']), js['message']))

    def getComment(self):
        url = 'https://member.bilibili.com/x/web/replies?order=ctime&filter=-1&is_hidden=0&type=1&pn=1&ps=10'
        js = self.getJson(url)
        if js['code'] == 0:
            c = 0
            for obj in js['data']:
                if c == 5:
                    break
                c += 1
                name = obj['replier']
                comment = obj['message']
                video = obj['title']
                date = obj['ctime']
                print('''
    Comment: %s
    Name: %s
    Video: %s
    Date: %s''' % (comment, name, video, date))
        else:
            print('[Error] Get API Failed, Error code:[%s], Error message: [%s].' % (str(js['code']), js['message']))

    def getBarrage(self):
        url = 'https://api.bilibili.com/x/v2/dm/recent?pn=1&ps=50'
        js = self.getJson(url)
        if js['code'] == 0:
            c = 0
            for obj in js['data']['result']:
                if c == 5:
                    break
                c += 1
                name = obj['uname']
                message = obj['msg']
                video = obj['title']
                print('''
    Barrage: %s
    Name: %s
    Video: %s''' % (message, name, video))
        else:
            print('[Error] Get API Failed, Error code:[%s], Error message: [%s].' % (str(js['code']), js['message']))

if __name__ == '__main__':
    bili = Bilibili()
    if len(sys.argv) == 1:
        bili.help()
    else:
        if sys.argv[1] == 'live':
            bili.getLiveStatus()
        elif sys.argv[1] == 'video':
            bili.getNewVideo()
        elif sys.argv[1] == 'comment':
            bili.getComment()
        elif sys.argv[1] == 'barrage':
            bili.getBarrage()                      
        else:
            bili.help()
