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
driver = webdriver.Chrome(chrome_options=chrome_Options)
driver.set_page_load_timeout(5)
driver.set_script_timeout(5)

adsUrl ="text/links.txt"
clickWords ="text/words.txt"



class AdsClick:
    '广告点击基类'

    def NewIp(self):
        response = request.urlopen(r'http://api.xdaili.cn/xdaili-api//greatRecharge/getGreatIp?spiderId=ba5166e719064e22ab658f46ae642a49&orderno=YZ20171056915nbG83C&returnType=1&count=1')  #
        ip = response.read()
        ip = ip.decode('utf-8')
        chrome_Options.add_argument('--incognito')  # 浏览器增加参数
        return ip

    # 函数用来读取txt并生成列表
    def openTxt(self, path, list):  # openTet(文件路径，列表名称)
        list = []  # 定义空列表
        with open(path, 'r') as f:  # 循环读取文件
            adsUrlList = (f.readlines())
            for link in adsUrlList:
                link = link.strip()
                list.append(link)  # 生成列表

        # 遍历列表 删除空元素
        while '' in list:
            list.remove('')
        return list

adslclick1 = AdsClick()
ip = adslclick1.NewIp()
links = adslclick1.openTxt(adsUrl, 'links')  #访问openTxt()函数
linksNum = len(links)

print('IP', ip)
print('网址总数', linksNum)