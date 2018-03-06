#!/usr/bin/python
# -*- coding: UTF-8 -*-
# import win32api
# import win32con
# import win32gui
# import os
# import random       #随机数生成模块
# import re


from selenium import webdriver    #载入selenium模块
from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from urllib import request       #载入urllib模块,用来获取代理IP
chrome_Options = webdriver.ChromeOptions()  # 浏览器参数


class OpenText (object):
    """
        获取txt内容为列表
        path 为文件地址路径
        listname 为列表名称
        """
    def __init__(self, path, listname):
        self.path = path
        self.listname = listname

    # @staticmethod
    def txtlist(self):
        self.listname = []  # 定义空列表
        with open(self.path, 'r') as f:        #循环读取文件
            adsUrlList = (f.readlines())
            for link in adsUrlList:
                link=link.strip()
                self.listname.append(link)  # 生成列表

        while '' in self.listname:
            self.listname.remove('')    #遍历列表 删除空元素
        return self.listname

    def total(self):
        return len(self.listname)    #获取总数

class Elements(object):
    """
    定位元素，获取所有匹配值
    elements 为一组元素,如：ads = driver.find_elements_by_tag_name("iframe")
    listname 为列表名称
    """
    def __init__(self, elements, listname):
        self.elements = elements
        self.listname = listname

    def elementslist(self): #获取到一个列表
        self.listname = []  # 定义空列表
        for i in self.elements:
            element = (i.get_attribute("name")) # get_attribute获取name的值
            self.listname.append(element) # 生成列表
        return self.listname


class WaitOpen(object):
    """
        等待页面加载成功
        1、首次5s内异常，执行刷新一次
        2、刷新后异常，执行关闭当前标签
        3、重新打开页面异常，执行关闭当前标签
        4、再次重新打开页面异常，执行关闭当前标签
        """
    def __init__(self, url, e, dr):
        self.url = url
        self.e = e
        self.dr = dr
    def open(self):
        try:
            self.dr = webdriver.Chrome(chrome_options=chrome_Options)
            self.dr.get(self.url)
            WebDriverWait(self.dr, 5).until(EC.presence_of_element_located((By.XPATH, self.e)))
        except Exception:
            now_handle = self.dr.current_window_handle  # 获取当前窗口句柄
            print('当前窗口句柄是：', now_handle)
            print("刷新第一次！5s钟内未加载完成,即将刷新当前窗口！")
            self.dr.refresh()
            try:
                WebDriverWait(self.dr, 5).until(EC.presence_of_element_located((By.XPATH, self.e)))
            except Exception:
                now_handle = self.dr.current_window_handle  # 获取当前窗口句柄
                print('当前窗口句柄是：', now_handle)
                print("关闭第1次！5s钟内未加载完成,即将关闭当前窗口！")
                self.dr.close()
                try:
                    self.dr = webdriver.Chrome(chrome_options=chrome_Options)
                    self.dr.get(self.url)
                    WebDriverWait(self.dr, 5).until(EC.presence_of_element_located((By.XPATH, self.e)))
                except Exception:
                    now_handle = self.dr.current_window_handle  # 获取当前窗口句柄
                    print('当前窗口句柄是：', now_handle)
                    print("关闭第2次！5s钟内未加载完成,即将关闭当前窗口！")
                    self.dr.close()
"""
                    try:
                        driver = webdriver.Chrome(chrome_options=chrome_Options)
                        driver.get(url)
                        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, e)))
                    except Exception:
                        now_handle = driver.current_window_handle  # 获取当前窗口句柄
                        print('当前窗口句柄是：', now_handle)
                        print("关闭第3次！5s钟内未加载完成,即将关闭当前窗口！")
                        driver.close()
                        try:
                            driver = webdriver.Chrome(chrome_options=chrome_Options)
                            driver.get(url)
                            WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, e)))
                        except Exception:
                            now_handle = driver.current_window_handle  # 获取当前窗口句柄
                            print('当前窗口句柄是：', now_handle)
                            print("关闭第4次！5s钟内未加载完成,即将关闭当前窗口！")
                            driver.close()
                            try:
                                driver = webdriver.Chrome(chrome_options=chrome_Options)
                                driver.get(url)
                                WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, e)))
                            except Exception:
                                now_handle = driver.current_window_handle  # 获取当前窗口句柄
                                print('当前窗口句柄是：', now_handle)
                                print("关闭第5次！5s钟内未加载完成,即将关闭当前窗口！")
                                print('该页面未正常打开', url)
                                driver.close()
"""

if __name__ == '__main__':
    adsUrl = "text/links.txt"
    clickWords = "text/words.txt"
    OpenText = OpenText(adsUrl, 'links')
    # print(OpenText.txtlist())
    print(OpenText.total())
    chrome_Options = webdriver.ChromeOptions()  # 浏览器参数
    driver = webdriver.Chrome(chrome_options=chrome_Options)
    driver.get('http://www.iqly.cn')
    ads = driver.find_elements_by_tag_name("iframe")
    a =Elements(ads, 'ls')
    print(a.elementslist())

