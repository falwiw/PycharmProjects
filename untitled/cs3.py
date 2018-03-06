#!/usr/bin/python
# -*- coding: UTF-8 -*-
import webbrowser
import win32api
import win32con
import win32gui
import time

#Define the url address
url_baidu_home = "http://www.baidu.com/"
url_baiduNews_tags = "http://news.baidu.com/"
odw_baiduMusic_tags = "http://play.baidu.com/"
odw_baiduXueshu_tags = "http://xueshu.baidu.com/"

def maxWindow():
    win32api.keybd_event(122,0,0,0) #F11
    win32api.keybd_event(122,0,win32con.KEYEVENT_KEYUP,0) #Realize the F11 button

def switchTab():
    win32api.keybd_event(17,0,0,0) #Ctrl
    win32api.keybd_event(9,0,0,0) #Tab
    win32api.keybd_event(17,0,KEYEVENT_KEYUP,0) #Realize the Ctrl button
    win32api.keybd_event(19,0,KEYEVENT_KEYUP,0) #Realize the Tab button

hwnd = win32gui.GetForegroundWindow() #Get the 句柄
win32gui.MoveWindow(hwnd,1980,0,1980,1080,False) #Move Window to the second screen
maxWindow()
count = 0
while (count<1000):
    switchTab()
    time.sleep(3)
    count=count+1