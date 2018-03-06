#!/usr/bin/python
# -*- coding: UTF-8 -*-

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


a = openTxt(adsUrl,"links")
print(a)


b = openTxt(clickWords,"Words")
print(b)
# #获取网址总数
# linksNum = len(links)
# print('网址总数', linksNum)