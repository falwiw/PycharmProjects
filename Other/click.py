#!/usr/bin/python
# -*- coding: UTF-8 -*-
import os
import sys
import random       #随机数生成模块
import re
from selenium import webdriver    #载入selenium模块
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from urllib import request       #载入urllib模块,用来获取代理IP
chrome_Options = webdriver.ChromeOptions()  # 浏览器参数
from Other.method import *

#广告点击类
SSP_1 = 1
KEW_WORD = 1
class StartClick():
    def __init__(self,init_window_name):
        self.init_window_name = init_window_name




def ads_start():
    adsUrl = "text/links.txt"
    clickWords = "text/words.txt"
    opentext = OpenText(adsUrl, 'links')
    print(opentext.txtlist())
    print(opentext.total())
    chrome_Options = webdriver.ChromeOptions()  # 浏览器参数
    driver = webdriver.Chrome(chrome_options=chrome_Options)
    driver.get('http://www.iqly.cn')
    ads = driver.find_elements_by_tag_name("iframe")
    a =Elements(ads, 'ls')
    print(a.elementslist())

