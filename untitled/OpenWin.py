#!/usr/bin/python
# -*- coding: UTF-8 -*-
import win32api
import win32con
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium import webdriver    #载入selenium模块
from urllib import request       #载入urllib模块




adsUrl ="text/links.txt"
links=[]    #定义空列表
with open(adsUrl, 'r') as f:        #循环读取文件
    adsUrlList = (f.readlines())
    for link in adsUrlList:
        link=link.strip()
        links.append(link)  # 生成列表

#遍历列表 删除空元素
while '' in links:
    links.remove('')
#获取网址总数

linksNum = len(links)

print('网址总数', linksNum)

for j in range(linksNum):
    nowUrl = links[j]
    driver = webdriver.Chrome()  # 载入浏览器驱动
    driver.get(nowUrl)




sleep(60)