import os, requests, re, time

class img(object):
    def __init__(self, url, proxy=False):
        #Get Desktop Path
        self.path =  os.environ['USERPROFILE'] + '\Desktop\\'
        #Check path
        print('[INFO] The Path is: ' + self.path + 'images')
        files = os.listdir(self.path)
        if 'images' not in files:
            os.popen('mkdir ' + self.path + 'images')
            print('[INFO] Folder Created.')
        else:
            print('[INFO] Folder Found.')
        self.path += 'images\\'
        #Check url
        if url == '':
            os._exit(1)
        if 'http://' in url:
            pass
        elif 'https://' in url:
            pass
        else:
            url = 'https://' + url
        self.url = url
        self.website = self.url.replace('https://', '').replace('http://', '').split('/')[0]
        #Proxy
        self.isProxy = proxy
        self.proxies = {
            'https': 'https://127.0.0.1:1080',
            'http': 'http://127.0.0.1:1080'
            }
            
    def getImageList(self):
        if self.isProxy:
            try:
                res = requests.get(self.url, proxies=self.proxies)
                res.raise_for_status()
            except:
                try:
                    res = requests.get(self.url.replace('https://', 'http://'), proxies=self.proxies)
                except:
                    print('[ERROR] Get Res Failed, url is: %s' % self.url)
                    os._exit(1)
        else:
            try:
                res = requests.get(self.url)
                res.raise_for_status()
            except:
                try:
                    res = requests.get(self.url.replace('https://', 'http://'))
                except:
                    print('[ERROR] Get Res Failed, url is: %s' % self.url)
                    os._exit(1)
        res.raise_for_status()
        pattern = re.compile(r'(((https?):\/\/)+(\w+\.)+(\w+)[\w\/\.\-]*\.(jpg|gif|png|jpeg))')
        result = pattern.findall(res.text)
        if result == []:
            print('[ERROR] Image No Found.')
            #print(res.text)
            os._exit(1)
        urls = []
        for item in result:
            urls.append(item[0])
        urls = list(set(urls))
        #print('\n'.join(urls))
        print('[INFO] Found %s image urls.' % str(len(urls)))
        return urls

    def getImg(self):
        urls = self.getImageList()
        imgPath = self.path + self.website
        os.popen('mkdir ' + imgPath)
        for url in urls:
            #print(url)
            try:
                if self.isProxy:
                    res = requests.get(url, proxies=self.proxies)
                else:
                    res = requests.get(url)
                res.raise_for_status()
            except:
                print('[WARNNING] %s/%s Image Collect Failed.' % (str(urls.index(url) + 1),str(len(urls))))
                continue
            imgType = '.' + url.split('.')[-1]
            with open(imgPath + '\\' + str(urls.index(url)) + imgType, 'wb') as file:
                file.write(res.content)
            print('\r'+'[INFO] %s/%s Image Collect Succeed.' % (str(urls.index(url) + 1),str(len(urls))),end='')
        time.sleep(1)
        print('\r'+'[INFO] All of Images have been Collected.')
            

if __name__ == '__main__':
    url = input('[SET]url: ')
    if url == '':
        print('[ERROR] Please enter the url.')
        os._exit(1)
    isProxy = input('[SET]Proxy(default no): ')
    if isProxy == '':
        img(url).getImg()
    else:
        img(url, proxy=True).getImg() 
