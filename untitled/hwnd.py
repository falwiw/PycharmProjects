import win32api
import win32con
import win32gui
import os
from time import sleep

command = 'taskkill /F /IM chrome.exe'
 # 比如这里关闭QQ进程
# os.popen(command)
print(os.popen(command).read())

'''
classname = "Chrome_WidgetWin_1"
titlename = "新标签页 - Google Chrome"
#获取句柄
hwnd = win32gui.FindWindow(classname, titlename)
#获取窗口左上角和右下角坐标
left, top, right, bottom = win32gui.GetWindowRect(hwnd)

def get_child_windows(parent):

#获得parent的所有子窗口句柄
#返回子窗口句柄列表

    if not parent:
        return
    hwndChildList = []
    win32gui.EnumChildWindows(parent, lambda hwnd, param: param.append(hwnd),  hwndChildList)
    return hwndChildList

#获取某个句柄的类名和标题
title = win32gui.GetWindowText(hwnd)
clsname = win32gui.GetClassName(hwnd)

#获取父句柄hwnd类名为clsname的子句柄
hwnd1= win32gui.FindWindowEx(hwnd, None, clsname, None)


#鼠标定位到(30,50)
win32api.SetCursorPos([30,150])
#执行左单键击，若需要双击则延时几毫秒再点击一次即可
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP | win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
#右键单击
win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP | win32con.MOUSEEVENTF_RIGHTDOWN, 0, 0, 0, 0)

win32api.keybd_event(13,0,0,0)
win32api.keybd_event(13,0,win32con.KEYEVENTF_KEYUP,0)

win32gui.PostMessage(hwnd, win32con.WM_CLOSE, 0, 0)

sleep(30)
'''