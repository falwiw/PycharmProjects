#!/usr/bin/python
# -*- coding: UTF-8 -*-
import win32api
import win32con
import win32gui
import os
import random       #随机数生成模块
import re

from selenium import webdriver    #载入selenium模块
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from  selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from urllib import request       #载入urllib模块,用来获取代理IP
chrome_Options = webdriver.ChromeOptions()  #浏览器参数

# 定义函数:获取IP
# def GetIp():
#     response = request.urlopen(r'http://api.xdaili.cn/xdaili-api//greatRecharge/getGreatIp?spiderId=ba5166e719064e22ab658f46ae642a49&orderno=YZ20171056915nbG83C&returnType=1&count=1')  #
#     ip = response.read()
#     ip = ip.decode('utf-8')
#     return ip



def NewIp():
    response = request.urlopen(r'http://api.xdaili.cn/xdaili-api//greatRecharge/getGreatIp?spiderId=ba5166e719064e22ab658f46ae642a49&orderno=YZ20171056915nbG83C&returnType=1&count=1')  #
    ip = response.read()
    ip = ip.decode('utf-8')
    chrome_Options.add_argument('--incognito --proxy-server=http://'+(ip))     #浏览器增加参数
    return



NewIp()     #获取一个IPy
driver = webdriver.Chrome(chrome_options=chrome_Options)
driver.get("http://service.spiritsoft.cn/ua.html")