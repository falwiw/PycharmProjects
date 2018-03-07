#!/usr/bin/python
# -*- coding: UTF-8 -*-
#引入窗口模块
from Other.window import *
#引入广告点击模块
from Other.click import *
# 实例化GUI
def gui_start():
    init_window = Tk()  # 实例化出一个父窗口
    ZMJ_PORTAL = MY_GUI(init_window)
    # 设置根窗口默认属性
    ZMJ_PORTAL.set_init_window()

    init_window.mainloop()  # 父窗口进入事件循环，可以理解为保持窗口运行，否则界面不展示

gui_start()