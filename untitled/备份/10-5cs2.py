#!/usr/bin/python
# -*- coding: UTF-8 -*-
import win32api
import win32con
from selenium import webdriver    #载入selenium模块
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys

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
    print("操作第", j+1, "个网站", nowUrl)
    # 打开网址
    driver = webdriver.Chrome()  # 载入浏览器驱动
    driver.get(nowUrl)
    # 获取当前窗口句柄
    now_handle = driver.current_window_handle
    print(now_handle)
    # 循环遍历所有广告位
    ads = driver.find_elements_by_tag_name("iframe")
    # 创建空列表
    ifrList = []
    for i in ads:
        # get_attribute获取name的值
        ifrnum = (i.get_attribute("name"))
        # 生成列表
        ifrList.append(ifrnum)
    sleep(1)
    print("找到的广告位：", ifrList)
    # 获取列表总数
    listList = len(ifrList)
    print("广告位总数", listList)
    sleep(1)
    for i in range(listList):
        print(i+1)
        # 切回到第i个irame
        driver.switch_to.frame(i)
        # 定位到首个A标签
        link = driver.find_elements_by_css_selector("#container .row a:first-child")
        # get_attribute获取href的值
        href = link[0].get_attribute("href")
        print(href.replace('ctype:4', 'ctype:7'))
        # 在新标签页面打开
        js = "window.open('" + href + "');"
        driver.execute_script(js)
        # 返回到主文档
        driver.switch_to.default_content()  # 返回到主文档

    sleep(1)
    driver.quit()
    sleep(1)




