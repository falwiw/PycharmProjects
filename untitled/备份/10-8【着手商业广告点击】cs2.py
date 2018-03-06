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
    chrome_Options.add_argument('--proxy-server=http://'+(ip))     #浏览器增加参数
    return


adsUrl ="text/links.txt"
clickWords ="text/words.txt"
#函数用来读取txt并生成列表
def openTxt(path, list):       #openTet(文件路径，列表名称)
    list = []  # 定义空列表
    with open(path, 'r') as f:        #循环读取文件
        adsUrlList = (f.readlines())
        for link in adsUrlList:
            link=link.strip()
            list.append(link)  # 生成列表

    #遍历列表 删除空元素
    while '' in list:
        list.remove('')
    return list
links = openTxt(adsUrl, 'links')  #访问openTxt()函数
linksNum = len(links)

print('网址总数', linksNum)

for j in range(linksNum):
    nowUrl = links[j]

    if (j + 1) > 1:
        print("程序将在180s后关闭所有窗口")
        sleep(180)
        command = 'taskkill /F /IM chrome.exe'
        # 比如这里关闭QQ进程
        # os.system(command)
        print(os.popen(command).read())
    print("操作第", j + 1, "个网站", nowUrl)
    # 打开网址
    dr = webdriver.Chrome()  # 载入浏览器驱动
    dr.get(nowUrl)
    # 获取当前窗口句柄
    now_handle = dr.current_window_handle
    print(now_handle)
    # 循环遍历所有广告位
    ads = dr.find_elements_by_tag_name("iframe")
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
        separate = i+1
        # print(separate)

        # 切回到第i个irame

        dr.switch_to.frame(i)
        # 定位到首个A标签
        link = dr.find_elements_by_css_selector("#container .row a:first-child")
        # get_attribute获取href的值
        href = link[0].get_attribute("href")
        href = (href.replace('ctype:4', 'ctype:7'))
        href = (href.replace('ctype:6', 'ctype:7'))
        print("打开第",separate, "个广告位", href)
        # 在新标签页面打开
        # NewIp()     #获取一个IP
        driver = webdriver.Chrome(chrome_options=chrome_Options)
        # driver = webdriver.Chrome()  # 载入浏览器驱动
        # js = "window.open('" + href + "');"
        # driver.execute_script(js)


        words = openTxt(clickWords,"words")     #读取关键词txt
        wordsNum = len(words)   #获取关键词总数
        print('关键词总数', wordsNum)
        Num2 = random.randint(0,wordsNum)
        wordsRand = words[Num2]
        print("随机词为", wordsRand)
        sleep(2)
        Num1 = random.randint(0,1)       #随机输出0或1
        print('Num1值为',Num1)
        sleep(2)
        if Num1 == 0:
            driver.get(href)
            element = driver.find_element_by_id("keyword")
            element.clear()
            element.send_keys(wordsRand)
            element.send_keys(Keys.ENTER)
            # driver.find_element_by_id("keyword").send_keys(wordsRand)
            sleep(1)
        else:
            # 替换字符串中的关键词
            href = re.sub(r'&q=(.*)&lmsid', '&q=' + wordsRand + '&lmsid', href)
            print("更改后的链接: ", href)
            driver.get(href)

        #商业广告点击相关代码
        Ads = driver.find_elements_by_css_selector("#e_idea_pp li a[e-landurl]")
        print('商业广告总数',len(Ads))

        if len(Ads) > 7:
            print("商业广告数大于7")
            for i in Ads:
                AdsList = []
                AdsList.append(i)  # 生成列表
                print(i.text)
        else:
            print("商业广告数小于7")
            # 返回到主文档
        dr.switch_to.default_content()  # 返回到主文档


    print('延迟5s')
    sleep(5)
    # driver.quit()
    # sleep(5)




