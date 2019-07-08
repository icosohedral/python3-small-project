#python3

import RPi.GPIO as GPIO
from picamera import PiCamera
import time, os, sys, timeout_decorator, pymysql

class Sensor(object):
  def __init__(self):
    '''
    if len(sys.argv) == 2 and sys.argv[1] == '-t':
      info = self.thermometer()
      print(info)
    elif len(sys.argv) == 3 and sys.argv[1] == '-c':
      file = sys.argv[2]
      self.camera(file)
    else:
      self.help()'''
    return

  def help(self):
    print('''Usage:
  -t               --thermometer
  -c [filepath]    --camera''')
  
  def thermometer(self):
    tempinfo = {'temperature':'None', 'humidity':'None', 'check':False}
    @timeout_decorator.timeout(5)
    def work(info):
      #GPIO working
      channel =4 #GPIO4 for data trans
      data = []
      j = 0
      GPIO.setmode(GPIO.BCM)
      time.sleep(1)
      GPIO.setup(channel, GPIO.OUT)
      GPIO.output(channel, GPIO.LOW)
      time.sleep(0.02)
      GPIO.output(channel, GPIO.HIGH)
      GPIO.setup(channel, GPIO.IN)
      while GPIO.input(channel) == GPIO.LOW:
        continue
      while GPIO.input(channel) == GPIO.HIGH:
        continue
      while j < 40:
        k = 0
        while GPIO.input(channel) == GPIO.LOW:
          continue
        while GPIO.input(channel) == GPIO.HIGH:
          k += 1
          if k > 100:
            break
        if k < 8:
          data.append(0)
        else:
          data.append(1)
        j += 1
      GPIO.cleanup()
      #calculate and check data
      humidity_bit = data[0:8]
      humidity_point_bit = data[8:16]
      temperature_bit = data[16:24]
      temperature_point_bit = data[24:32]
      check_bit = data[32:40]
      humidity = 0
      humidity_point = 0
      temperature = 0
      temperature_point = 0
      check = 0
      for i in range(8):
        humidity += humidity_bit[i] * 2 ** (7-i)
        humidity_point += humidity_point_bit[i] * 2 ** (7-i)
        temperature += temperature_bit[i] * 2 ** (7-i)
        temperature_point += temperature_point_bit[i] * 2 ** (7-i)
        check += check_bit[i] * 2 ** (7-i)
      tmp = humidity + humidity_point + temperature + temperature_point
      if check == tmp:
        info['check'] = True
      else:
        info['check'] = False
      info['temperature'] = str(temperature)
      info['humidity'] = str(humidity)
      return info
    #return
    i = 0
    while i <3:
      try:
        tempinfo = work(tempinfo)
      except:
        pass
      if tempinfo['check']:
        break
      i += 1
    tempinfo['retry'] = str(i)
    return tempinfo

  def camera(self, saveAs):
    try:
      theCamera = PiCamera()
      theCamera.start_preview()
      time.sleep(3) #time for sensitive
      theCamera.capture(saveAs)
      theCamera.stop_preview()
      return True
    except:
      return False
      
class Web(object):
  def __init__(self):
    self.timeNow = time.strftime("%Y%m%d-%H%M", time.localtime())
    return

  def image(self):
    savePath = '/var/www/res/img/camera/'
    file = savePath + self.timeNow + '.jpg'
    result = Sensor().camera(file)
    if result:
      print('[Successed][Sensor] Take photo OK')
      img = self.timeNow
    else:
      img = 'noimg'
      print('[Error][Sensor] Take photo Failed')
    return img

  def temp(self):
    info = Sensor().thermometer()
    if info['check']:
      print('[Successed][Sensor] Get thermometer\'s info OK')
    else:
      print('[Error][Sensor] Get thermometer\'s info Failed')
    return info

  def sql(self, info):
    datenow = time.strftime("%Y-%m-%d", time.localtime())
    timenow = time.strftime("%H:%M", time.localtime())
    temperature = info['temperature']
    humidity =  info['humidity']
    commend = "INSERT INTO thermometer (date, time, temperature, humidity) values ('%s', '%s', '%s', '%s');" % (datenow, timenow, temperature, humidity)
    #连接数据库
    db = pymysql.connect('localhost', 'root', 'password', 'pi')
    #创建游标对象
    cursor = db.cursor()
    #执行查询命令
    cursor.execute(commend)
    try:
      cursor.execute(commend)
      db.commit()
      print('[Successed][SQL] Information insert OK')
    except:
      db.rollback()
      print('[Error][SQL] Information insert Failed')
    #关闭连接
    db.close()

  def page(self):
    pagefile = '/var/www/sensor.html'
    timenow = time.strftime("%Y-%m-%d %H:%M", time.localtime())
    img = self.image()
    tempInfo = self.temp()
    self.sql(tempInfo) #mysql insert
    content = '''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0, minimum-scale=1.0, maximum-scale=1.0, user-scalable=0">
<title>Sensor</title>
<link rel="stylesheet" type="text/css" href="./res/layui/css/layui.css">
<link rel="stylesheet" type="text/css" href="./res/css/main.css">
</head>
<body>
<div class="content whisper-content">    
<div class="cont">
  <div class="whisper-list">
    <div class="item-box">
      <div class="item">
        <div class="whisper-title">
			<p class="data"><font color="orange"><strong>Temperature&nbsp;&nbsp;&nbsp;%s ℃</strong></p></font><br>
			<p class="data"><font color="orange"><strong>Humidity&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;%s %%</strong></p></font><br>
			<p class="data"><font color="orange"><strong>Gauge Time&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;%s</strong></p></font><br>
        </div><br><br><br><br><br>
		<center><img src="./res/img/camera/%s.jpg"  alt="camera" /></center>  
		</div><br><br><br>
    </div>
  </div>
</div>
</div>
<script type="text/javascript" src="./res/layui/layui.js"></script>
</body>
</html>''' % (tempInfo['temperature'], tempInfo['humidity'], timenow, img)
    with open(pagefile, 'w') as file:
      file.write(content)
    print('[INFO][Web] Sensor.html generate OK')

if __name__ == '__main__':
  Web().page()
  
