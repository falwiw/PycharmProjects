#!/usr/bin/python
# -*- coding: UTF-8 -*-
import win32api
import win32con
from selenium import webdriver    #载入selenium模块
from time import sleep
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome()   #载入浏览器驱动
adsUrl ="text/links.txt"
links=[]    #定义空列表
with open(adsUrl, 'r') as f:        #循环读取文件
    adsUrlList = (f.readlines())
    for link in adsUrlList:
        link=link.strip()
        links.append(link)  # 生成列表

while '' in links:
    links.remove('')
print('网址总数',len(links))

for i in range(len(links)):
    driver = webdriver.Chrome()  # 载入浏览器驱动
    print(i)
    driver.get(links[i])
    sleep(3)
    driver.quit()
    sleep(3)