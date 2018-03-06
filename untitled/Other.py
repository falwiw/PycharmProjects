#!/usr/bin/python
# -*- coding: UTF-8 -*-
from selenium import webdriver    #载入selenium模块
from urllib import request       #载入urllib模块
driver = webdriver.Chrome()  # 载入浏览器驱动

def aa(link) :
    driver.get(link)
    return

aa("http://www.baidu.com")


