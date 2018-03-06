#!/usr/bin/python
# -*- coding: UTF-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
chrome_Options = webdriver.ChromeOptions()  #浏览器参数
chrome_Options.add_argument('--incognito')     #浏览器增加参数


class WaitOpen(object):

    def open(self, url, e):
        try:
            driver = webdriver.Chrome(chrome_options=chrome_Options)
            driver.get(url)
            WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, e)))
        except Exception:
            now_handle = driver.current_window_handle  # 获取当前窗口句柄
            print('当前窗口句柄是：', now_handle)
            print("刷新第一次！5s钟内未加载完成,即将刷新当前窗口！")
            driver.refresh()
            try:
                WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, e)))
            except Exception:
                now_handle = driver.current_window_handle  # 获取当前窗口句柄
                print('当前窗口句柄是：', now_handle)
                print("关闭第1次！5s钟内未加载完成,即将关闭当前窗口！")
                driver.close()

urllist = ['http://www.ksource.com.cn', 'http://www.yoosv.com', 'http://www.qq.com']

for i in urllist:
    print(i)
    waitopen = WaitOpen()
    waitopen.open(i, "/html/body/script[1]")








"""
class tt:
    def fa(self):
        return 'aa'
    def fb(self):
        return self.fa()
上面代码中的self.fa()调用如果不加self，直接fa()调用会报错找不到fa定义，用惯了c#等语言的要注意这一点
"""