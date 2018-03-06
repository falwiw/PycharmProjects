#!/usr/bin/python
# -*- coding: UTF-8 -*-
from tkinter import *
import hashlib
import time

class MY_GUI():
    def __init__(self,init_window_name):
        self.init_window_name = init_window_name

    # 设置窗口
    def set_init_window(self):
        self.init_window_name.title("登陆器测试")
        self.init_window_name.geometry("550x340")

        #LabelFrame 1 登陆及帐户信息
        self.lf1 = LabelFrame(self.init_window_name, text="登陆信息", width=240, height=150)
        self.lf1.place(x=10, y=10)

        self.user_label = Label(self.lf1, text="用户名：").place(x=5, y=5)
        self.pwd_Label = Label(self.lf1, text="密   码：").place(x=5, y=40)
        self.user_entry = Entry(self.lf1, text="", width=20).place(x=75, y=5)
        self.pwd_entry = Entry(self.lf1, text="", width=20, show="*").place(x=75, y=40)
        self.land_button = Button(self.lf1, text="登陆", width=8).place(x=30, y=80)
        self.register_utton = Button(self.lf1, text="注册", width=8).place(x=140, y=80)


        #LabelFrame 2 日志信息显示
        self.lf2 = LabelFrame(self.init_window_name, text="日志信息", width=240, height=155)
        self.lf2.place(x=10, y=170)



        # LabelFrame 3
        self.lf3 = LabelFrame(self.init_window_name, text="设置1", width=270, height=150)
        self.lf3.place(x=270, y=10)
        self.sspxz_label = Label(self.lf3, text="联盟选择：", width=8, fg="blue").place(x=5, y=5)
        self.ssp = IntVar()
        self.ssp.set(3)
        self.sougou_rb = Radiobutton(self.lf3, text="搜狗联盟", variable=self.ssp, value=1).place(x=5, y=30)
        self.baidu_rb = Radiobutton(self.lf3, text="百度联盟", variable=self.ssp, value=2).place(x=98, y=30)
        self.qihu_rb = Radiobutton(self.lf3, text="360联盟", variable=self.ssp, value=3).place(x=188, y=30)

        self.ckxz_label = Label(self.lf3, text="词库选择：", width=8, fg="blue").place(x=5, y=70)
        self.keyword = IntVar()
        self.keyword.set(3)
        self.ck3_rb = Radiobutton(self.lf3, text="词库3", variable=self.keyword, value=1).place(x=5, y=95)
        self.ck2_rb = Radiobutton(self.lf3, text="词库2", variable=self.keyword, value=2).place(x=98, y=95)
        self.ck1_rb = Radiobutton(self.lf3, text="词库1", variable=self.keyword, value=3).place(x=188, y=95)

        #LabelFrame 4
        self.lf4 = LabelFrame(self.init_window_name, text="设置2", width=270, height=120)
        self.lf4.place(x=270, y=170)

        self.adsclick1 = IntVar()  #推广链接点击个数1
        self.adsclick1.set("3")
        self.adsclick2 = IntVar()  #推广链接点击个数2
        self.adsclick2.set("3")
        self.tg_num_label = Label(self.lf4, text="推广链接点击个数：").place(x=5, y=0)
        self.tg_num_entry1 = Entry(self.lf4, textvariable=self.adsclick1, width=3).place(x=120, y=0)
        self.txt_label = Label(self.lf4, text="~         (随机)").place(x=145, y=0)
        self.tg_num_entry2 = Entry(self.lf4, textvariable=self.adsclick2, width=3).place(x=160, y=0)

        self.searchclick1 = IntVar()  #搜索结果点击个数1
        self.searchclick1.set("1")
        self.searchclick2 = IntVar()  #搜索结果点击个数2
        self.searchclick2.set("3")
        self.ss_num_label = Label(self.lf4, text="搜索结果点击个数：").place(x=5, y=25)
        self.ss_num_entry1 = Entry(self.lf4, textvariable=self.searchclick1, width=3).place(x=120, y=25)
        self.txt_label = Label(self.lf4, text="~         (随机)").place(x=145, y=25)
        self.ss_num_entry2 = Entry(self.lf4, textvariable=self.searchclick2, width=3).place(x=160, y=25)

        self.delaytime1 = IntVar()  #浏览窗口停留时间1
        self.delaytime1.set("60")
        self.delaytime2 = IntVar()  #浏览窗口停留时间2
        self.delaytime2.set("300")
        self.tl_sj_label = Label(self.lf4, text="浏览窗口停留时间：").place(x=5, y=50)
        self.txt_entry = Entry(self.lf4, textvariable=self.delaytime1, width=3).place(x=120, y=50)
        self.txt_label = Label(self.lf4, text="~         (秒)").place(x=145, y=50)
        self.txt_entry = Entry(self.lf4, textvariable=self.delaytime2, width=3).place(x=160, y=50)

        self.timeryear = IntVar()  #定时 年
        self.timeryear.set("2018")
        self.timermonth = IntVar()  #定时 月
        self.timermonth.set("3")
        self.timerday = IntVar()  #定时 日
        self.timerday.set("4")
        self.timerhour = IntVar()  #定时 时
        self.timerhour.set("8")
        self.timermin = IntVar()  #定时 分
        self.timermin.set("0")
        self.txt_label = Label(self.lf4, text="定时时间：           -      -            :       (定时)").place(x=5, y=75)
        self.year_entry = Entry(self.lf4, textvariable=self.timeryear, width=4).place(x=79, y=75)
        self.month_entry = Entry(self.lf4, textvariable=self.timermonth, width=2).place(x=120, y=75)
        self.day_entry = Entry(self.lf4, textvariable=self.timerday, width=2).place(x=148, y=75)
        self.hour_entry = Entry(self.lf4, textvariable=self.timerhour, width=2).place(x=172, y=75)
        self.min_entry = Entry(self.lf4, textvariable=self.timermin, width=2).place(x=200, y=75)
        # 保存
        self.save_button = Button(self.init_window_name, text="保存", width=6).place(x=270, y=295)
        self.start_button = Button(self.init_window_name, text="开始", width=6).place(x=344, y=295)
        self.pause_button = Button(self.init_window_name, text="暂停", width=6).place(x=415, y=295)
        self.stop_button = Button(self.init_window_name, text="停止", width=6).place(x=487, y=295)
        # 组件隐藏
        # lf1.pack_forget()
        # self.init_window_name.mainloop()

        # 日志动态打印
        def write_log_to_Text(self, logmsg):
            global LOG_LINE_NUM
            current_time = self.get_current_time()
            logmsg_in = str(current_time) + " " + str(logmsg) + "\n"  # 换行
            if LOG_LINE_NUM <= 7:
                self.log_data_Text.insert(END, logmsg_in)
                LOG_LINE_NUM = LOG_LINE_NUM + 1
            else:
                self.log_data_Text.delete(1.0, 2.0)
                self.log_data_Text.insert(END, logmsg_in)

def gui_start():
    init_window = Tk()  # 实例化出一个父窗口
    ZMJ_PORTAL = MY_GUI(init_window)
    # 设置根窗口默认属性
    ZMJ_PORTAL.set_init_window()

    init_window.mainloop()  # 父窗口进入事件循环，可以理解为保持窗口运行，否则界面不展示

gui_start()