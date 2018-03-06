#!/usr/bin/python
# -*- coding: UTF-8 -*-
import os
import win32api
import win32gui
import win32con
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

# 执行前关闭所有谷歌驱动
command = 'taskkill /F /IM chromedriver.exe'
# 比如这里关闭QQ进程
# os.system(command)
print(os.popen(command).read())

driver = webdriver.Chrome()  # 载入浏览器驱动
# 商业广告点击相关代码
url = "https://www.so.com/s?src=lm&ls=sm1972121&q=传奇&lmsid=00306d301210faf8&lm_extend=ctype:7"
driver.get(url)
one_win = driver.current_window_handle
print("首个窗口句柄\n", one_win)
print("等待5s")
sleep(5)
Ads = driver.find_elements_by_css_selector("#e_idea_pp li a[e-landurl]")  # 定位商业广告元素

print('商业广告总数', len(Ads))
AdsList = []
for i in Ads:
    print(i.text)
    AdsList.append(i)  # 生成列表

# 点击3个商业广告
for i in range(0, 3):
    print(i)
    thisAd = AdsList[i]
    print(thisAd)

    print("鼠标悬停1s")
    sleep(1)
    thisAd.click()

    print("等待5s")
    sleep(5)

all_win = driver.window_handles
print("当前所有窗口句柄\n", all_win)
print("等待5s")
sleep(5)

"""
# 点击内页
print(driver.title)
sleep(3)
Tag = driver.find_elements_by_css_selector("a")
print('内页链接数', len(Tag))
Tags = []
for i in Tag:
    # print(i.text)
    Tags.append(i)  # 生成列表
for i in range(1, 3):
    thisA = Tags[i]
    ActionChains(driver).click(this).perform()  # 单击



    sleep(5)
def maxWindow():
    win32api.keybd_event(17, 0, 0, 0)  # 按下Ctrl
    win32api.keybd_event(49, 0, 0, 0)  # 按下1
    win32api.keybd_event(49, 0, win32con.KEYEVENTF_KEYUP, 0)  # 释放1
    win32api.keybd_event(17, 0, win32con.KEYEVENTF_KEYUP, 0)  # 释放Ctrl

"""

"""
command = 'taskkill /F /IM chromedriver.exe'
# 比如这里关闭QQ进程
# os.system(command)
print(os.popen(command).read())



    win32api.keybd_event(40, 0, 0, 0)
    win32api.keybd_event(40, 0, win32con.KEYEVENTF_KEYUP, 0)  # 释放下键
    win32api.keybd_event(13, 0, 0, 0)
    win32api.keybd_event(13, 0, win32con.KEYEVENTF_KEYUP, 0)  # 释放ENTER
    win32api.keybd_event(17, 0, 0, 0)
    win32api.keybd_event(9, 0, 0, 0)
    win32api.keybd_event(17, 0, win32con.KEYEVENTF_KEYUP, 0)  # 释放Ctrl
    win32api.keybd_event(9, 0, win32con.KEYEVENTF_KEYUP, 0)  # Tab
"""
