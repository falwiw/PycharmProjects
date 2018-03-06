#!/usr/bin/python
# -*- coding: UTF-8 -*-
import win32api
import win32con
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium import webdriver    #载入selenium模块
from urllib import request       #载入urllib模块
# driver = webdriver.Chrome()  # 载入浏览器驱动

response = request.urlopen(r'http://api.xdaili.cn/xdaili-api//greatRecharge/getGreatIp?spiderId=ba5166e719064e22ab658f46ae642a49&orderno=YZ20171056915nbG83C&returnType=1&count=1') #
page = response.read()
page = page.decode('utf-8')

print("获取到的ip", page)

chromeOptions = webdriver.ChromeOptions()
chromeOptions.add_argument('--proxy-server=http://'+page)
driver = webdriver.Chrome(chrome_options=chromeOptions)
driver.get("http://0.0.0.0")


