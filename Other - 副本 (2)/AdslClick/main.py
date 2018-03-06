#!/usr/bin/python
# -*- coding: UTF-8 -*-
from tkinter import *
import hashlib
import time
import pymysql
from tkinter import messagebox
import os
import random       #随机数生成模块
import re
from selenium import webdriver    #载入selenium模块
from time import sleep
from module.method import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from urllib import request       #载入urllib模块,用来获取代理IP
chrome_Options = webdriver.ChromeOptions()  # 浏览器参数

# GUI界面
LOG_LINE_NUM = 0
class MY_GUI():
    def __init__(self,init_window_name):
        self.init_window_name = init_window_name
        self.screenwidth = self.init_window_name.winfo_screenwidth()
        self.screenheight = self.init_window_name.winfo_screenheight()

    #获取PC分辨率，计算取窗口位置
    def center_window(self, root_wondow, width, height):
        self.size = '%dx%d+%d+%d' % (width, height, (self.screenwidth - width) / 2, (self.screenheight - height) / 2)
        print(self.size)
        root_wondow.geometry(self.size)

    # 设置窗口
    def set_init_window(self):
        self.init_window_name.title("360广告自动点击器 v1.0 吉吉")
        self.init_window_name.iconbitmap('logo.ico')
        # self.init_window_name.geometry("550x340")
        self.screenwidth = self.init_window_name.winfo_screenwidth()
        self.screenheight = self.init_window_name.winfo_screenheight()
        self.window_size = ("550x340+%d+%d" % (((self.screenwidth-550)/2), ((self.screenheight)-340)/2))
        self.init_window_name.geometry(self.window_size)



        #LabelFrame 1 登陆及帐户信息
        self.lf1 = LabelFrame(self.init_window_name, text="登陆信息", width=240, height=150)
        self.lf1.place(x=10, y=10)
        self.var_usr_name = StringVar()
        self.var_usr_name.set("")
        self.var_usr_pwd = StringVar()
        self.var_usr_pwd.set("")
        self.user_label = Label(self.lf1, text="用户名：").place(x=5, y=5)
        self.pwd_Label = Label(self.lf1, text="密   码：").place(x=5, y=40)
        self.user_entry = Entry(self.lf1, textvariable=self.var_usr_name, width=20).place(x=75, y=5)
        self.pwd_entry = Entry(self.lf1, textvariable=self.var_usr_pwd, width=20, show="*").place(x=75, y=40)
        self.land_button = Button(self.lf1, text="登陆", width=8, command=self.usr_login).place(x=30, y=80)
        self.register_utton = Button(self.lf1, text="注册", width=8, command=self.sign_up).place(x=140, y=80)

        # LabelFrame 1a 登陆及帐户信息，默认隐藏状态
        self.lf1a = LabelFrame(self.init_window_name, text="会员信息", width=240, height=150)


        self.var_welcome = StringVar()
        self.var_welcome.set("欢迎您使用我们的产品")
        self.welcome_label = Label(self.lf1a, textvariable=self.var_welcome, font=("", 11, "normal"), fg="#ee7b00").place(x=38, y=3)


        self.var_id = StringVar()
        # self.var_id.set("帐号：")
        self.id_label = Label(self.lf1a, textvariable=self.var_id, fg="green").place(x=30, y=33)

        self.var_jf = StringVar()
        # self.var_jf.set("积分：")
        self.jf_label = Label(self.lf1a, textvariable=self.var_jf, fg="green").place(x=30, y=63)

        self.recharge_button = Button(self.lf1a, text="充值", width=8).place(x=30, y=93)
        self.refresh_utton = Button(self.lf1a, text="刷新", width=8).place(x=140, y=93)


        #LabelFrame 2 日志信息显示
        self.lf2 = LabelFrame(self.init_window_name, text="日志信息", width=240, height=155)
        self.lf2.place(x=10, y=170)
        self.log_data_Text = Text(self.lf2, width=37, height=11, font=("", 8, "normal"), fg="#ee7b00")  # 日志框
        self.log_data_Text.place(x=5, y=0)


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




    # 获取当前时间
    def get_current_time(self):
        current_time = time.strftime('%m-%d %H:%M:%S', time.localtime(time.time()))
        return current_time

    # 日志动态打印
    def write_log_to_Text(self, logmsg):
        global LOG_LINE_NUM
        current_time = self.get_current_time()
        logmsg_in = str(current_time) + " " + str(logmsg) + "\n"  # 换行
        if LOG_LINE_NUM <= 9:
            self.log_data_Text.insert(END, logmsg_in)
            LOG_LINE_NUM = LOG_LINE_NUM + 1
        else:
            self.log_data_Text.delete(1.0, 2.0)
            self.log_data_Text.insert(END, logmsg_in)

    #注册模块
    def sign_up(self):
        self.window_sign_up = Toplevel(self.init_window_name)
        # self.window_sign_up.geometry('300x200')
        self.window_size = ("300x220+%d+%d" % (((self.screenwidth - 550) / 2+552), ((self.screenheight) - 220) / 2))
        self.window_sign_up.geometry(self.window_size)
        self.window_sign_up.title('注册窗口')

        self.sign_up_lf = LabelFrame(self.window_sign_up, text="填写注册信息", width=272, height=200)
        self.sign_up_lf.place(x=15, y=10)
        self.new_name = StringVar()  # 将输入的注册名赋值给变量
        self.new_name.set("admin")  # 将最初显示定为'example@python.com'
        self.init_window_name = Label(self.sign_up_lf, text='用户名：', fg="red").place(x=20, y=10)  # 将`User name:`放置在坐标（10,10）。
        self.entry_new_name = Entry(self.sign_up_lf, textvariable=self.new_name, width="23")  # 创建一个注册名的`entry`，变量为`new_name`
        self.entry_new_name.place(x=80, y=10)  # `entry`放置在坐标（150,10）.

        self.new_pwd = StringVar()
        Label(self.sign_up_lf, text='密   码：', fg="red").place(x=20, y=40)
        self.entry_usr_pwd = Entry(self.sign_up_lf, textvariable=self.new_pwd, show='*', width="23")
        self.entry_usr_pwd.place(x=80, y=40)

        self.new_pwd_confirm = StringVar()
        Label(self.sign_up_lf, text='确   认：', fg="red").place(x=20, y=70)
        self.entry_usr_pwd_confirm = Entry(self.sign_up_lf, textvariable=self.new_pwd_confirm, show='*', width="23")
        self.entry_usr_pwd_confirm.place(x=80, y=70)

        self.new_mail_confirm = StringVar()
        Label(self.sign_up_lf, text='邮   件：').place(x=20, y=100)
        self.entry_new_mail = Entry(self.sign_up_lf, textvariable=self.new_mail_confirm, width="23")
        self.entry_new_mail.place(x=80, y=100)

        self.btn_comfirm_sign_up = Button(self.sign_up_lf, text='提   交', width="8", command=self.sign_in)
        self.btn_comfirm_sign_up.place(x=102, y=140)

    #MD5加密函数
    def md5(self, string):
        m2 = hashlib.md5()
        m2.update(("++" + string + "--").encode("utf-8"))
        return m2.hexdigest()

    # 注册功能功能函数
    def sign_in(self):
        sign_in_name = self.entry_new_name.get()
        sign_in_pwd = self.entry_usr_pwd.get()
        sign_in_pwd_confirm = self.entry_usr_pwd_confirm.get()
        # sign_in_time = int(time.time())
        sign_in_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        sign_in_mail = self.entry_new_mail.get()
        print("您提交的注册信息为：帐号：%s, 密码：%s, 确认密码：%s, 邮件：%s, 时间：%s" % (sign_in_name, sign_in_pwd, sign_in_pwd_confirm, sign_in_mail, sign_in_time))
        print(len(sign_in_name))
        sign_in_name_len = len(sign_in_name)
        print(sign_in_name_len)
        if sign_in_name_len < 5:
            self.write_log_to_Text("INFO:用户名<5位！")  # 登陆成功，在日志窗口显示
            messagebox.showerror('错误', "用户名不能小于5位！")
            return
        elif sign_in_name_len > 15:
            self.write_log_to_Text("INFO:用户名>15位！")  # 登陆成功，在日志窗口显示
            messagebox.showerror('错误', "用户名不能大于15位！")
            return
        elif sign_in_pwd != sign_in_pwd_confirm:
            self.write_log_to_Text("INFO:密码和确认密码必需一致！")  # 在日志窗口显示
            messagebox.showinfo('错误', '密码和确认密码必需一致！')
            return

        # 打开数据库连接
        db = pymysql.connect("122.114.13.199", "360Click", "LOVElove12354", "360Click", charset='utf8')
        # 使用cursor()方法获取操作游标
        cursor = db.cursor()
        try:
            # 使用execute()方法执行SQL语句
            sql1 = "SELECT * FROM python_user WHERE USER_A='%s'"
            cursor.execute(sql1 % sign_in_name)
            # 使用execute()方法执行SQL语句
            data = cursor.fetchall()
            print(data)
            sql_user = data[0][1]
            print("数据库查询结果：", sql_user)
            if sign_in_name == sql_user:    #判断用户输入用户是否存在
                self.write_log_to_Text("INFO:“%s”该用户已存在，请重新输入！" % sign_in_name)  # 登陆成功，在日志窗口显示
                messagebox.showerror('错误', "“%s”该用户已存在，请重新输入！" % sign_in_name)
                return
        except:
            print(sign_in_name, sign_in_pwd, sign_in_mail, sign_in_time)
            self.write_log_to_Text("INFO:“%s”帐号符合规定，继续注册！" % sign_in_name)  # 登陆成功，在日志窗口显示
            #使用execute()方法执行SQL语句
            sql2 = """INSERT INTO python_user(USER_A,PWD, EMAIL, INTEGRAL, SIGNTIME, LOGINTIME)VALUES ('%s', '%s', '%s', '%s', '%s', '%s')"""
            cursor.execute(sql2 % (sign_in_name, self.md5(sign_in_pwd), sign_in_mail, 10, sign_in_time, '0000-00-00 00:00:00'))
        finally:
            # 关闭游标和数据库的连接
            cursor.close()
            db.close()



    # 登陆功能函数
    def usr_login(self):
        usr_name = self.var_usr_name.get()
        usr_pwd = self.var_usr_pwd.get()
        usr_pwd = self.md5(usr_pwd) #调用MD5函数
        # print("您输入的帐号是:%s ，密码是：%s" % (usr_name, usr_pwd))
        if len(usr_name) == 0 or len(usr_pwd) == 0:
            # return messagebox.showerror('错误', '您还没有输入帐号或密码！')
            self.write_log_to_Text("INFO:您还没有输入帐号或密码！")  # 在日志窗口显示
            return
        # 打开数据库连接
        db = pymysql.connect("122.114.13.199", "360Click", "LOVElove12354", "360Click", charset='utf8')

        # 使用cursor()方法创建一个游标对象
        cursor = db.cursor()
        # 使用execute()方法执行SQL语句
        sql = "SELECT * FROM python_user WHERE USER_A='%s'"

        try:
            cursor.execute(sql % usr_name)
            # 使用execute()方法执行SQL语句
            data = cursor.fetchall()

            sql_user = data[0][1]
            sql_pwd = data[0][2]
            sql_jf = data[0][4]

            if sql_user == usr_name and sql_pwd == usr_pwd:
                self.write_log_to_Text("INFO:登陆成功") #登陆成功，在日志窗口显示
                messagebox.showinfo('登陆成功', '尊敬的 [%s] 您好，欢迎使用360广告点击器！' % usr_name)
                #登陆成功，登陆组件隐藏
                self.lf1.place_forget()
                # 登陆成功，用户信息组件显示
                self.lf1a.place(x=10, y=10)
                self.var_id.set("帐号：%s" % usr_name)
                self.var_jf.set("积分：%s" % sql_jf)
                return
            elif sql_user == usr_name and sql_pwd != usr_pwd:
                self.write_log_to_Text("INFO:帐号密码错误")  # 登陆成功，在日志窗口显示
                messagebox.showerror('密码错误', '您输入的密码不正确，请重新输入！')
                return

        except IndexError:
            self.write_log_to_Text("INFO:帐号不存在")  # 在日志窗口显示
            self.is_sign_up = messagebox.askyesno('帐号不存在', '您要现在注册吗？')
            # 提示需不需要注册新用户
            if self.is_sign_up:
                self.sign_up()
        finally:
            # 关闭游标和数据库的连接
            cursor.close()
            db.close()


#广告点击类
class ADS_CLICK():
    def __init__(self, start_click):
        self.start_click = start_click







# 实例化GUI
def gui_start():
    init_window = Tk()  # 实例化出一个父窗口
    ZMJ_PORTAL = MY_GUI(init_window)
    # 设置根窗口默认属性
    ZMJ_PORTAL.set_init_window()

    init_window.mainloop()  # 父窗口进入事件循环，可以理解为保持窗口运行，否则界面不展示

gui_start()



# 实例化点击类
def click_start():
    adsUrl = "text/links.txt"
    click_words = "text/words.txt"
    open_text = OpenText(adsUrl, 'links')


click_start()