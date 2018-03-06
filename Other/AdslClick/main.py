#!/usr/bin/python
# -*- coding: UTF-8 -*-
from tkinter import *
import hashlib
import time
import pymysql
from tkinter import messagebox
LOG_LINE_NUM = 0
class MY_GUI():
    def __init__(self,init_window_name):
        self.init_window_name = init_window_name

    #获取PC分辨率，计算取窗口位置
    def center_window(self, root_wondow, width, height):
        self.screenwidth = self.init_window_name.winfo_screenwidth()
        self.screenheight = self.init_window_name.winfo_screenheight()
        self.size = '%dx%d+%d+%d' % (width, height, (self.screenwidth - width) / 2, (self.screenheight - height) / 2)
        print(self.size)

        root_wondow.geometry(self.size)

    # 设置窗口
    def set_init_window(self):
        self.init_window_name.title("登陆器测试")
        # self.init_window_name.geometry("550x340")
        self.center_window(self.init_window_name, 550, 340)


        #LabelFrame 1 登陆及帐户信息
        self.lf1 = LabelFrame(self.init_window_name, text="登陆信息", width=240, height=150)
        self.lf1.place(x=10, y=10)
        self.var_usr_name = StringVar()
        self.var_usr_name.set("admin")
        self.var_usr_pwd = StringVar()
        self.var_usr_pwd.set("1")
        self.user_label = Label(self.lf1, text="用户名：").place(x=5, y=5)
        self.pwd_Label = Label(self.lf1, text="密   码：").place(x=5, y=40)
        self.user_entry = Entry(self.lf1, textvariable=self.var_usr_name, width=20).place(x=75, y=5)
        self.pwd_entry = Entry(self.lf1, textvariable=self.var_usr_pwd, width=20, show="*").place(x=75, y=40)
        self.land_button = Button(self.lf1, text="登陆", width=8, command=self.usr_login).place(x=30, y=80)
        self.register_utton = Button(self.lf1, text="注册", width=8, command=self.sign_up).place(x=140, y=80)


        #LabelFrame 2 日志信息显示
        self.lf2 = LabelFrame(self.init_window_name, text="日志信息", width=240, height=155)
        self.lf2.place(x=10, y=170)
        self.log_data_Text = Text(self.lf2, width=32, height=10)  # 日志框
        self.log_data_Text.place(x=3, y=0)


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
        
    #注册模块
    def sign_up(self):
        self.window_sign_up = Toplevel(self.init_window_name)
        # self.window_sign_up.geometry('300x200')
        self.center_window(self.window_sign_up, 300, 200)
        self.window_sign_up.title('注册窗口')
        self.sign_up_lf = LabelFrame(self.window_sign_up, text="填写注册信息", width=272, height=170)
        self.sign_up_lf.place(x=15, y=10)
        self.new_name = StringVar()  # 将输入的注册名赋值给变量
        self.new_name.set('example@python.com')  # 将最初显示定为'example@python.com'
        self.init_window_name = Label(self.sign_up_lf, text='用户名：').place(x=20, y=10)  # 将`User name:`放置在坐标（10,10）。
        self.entry_new_name = Entry(self.sign_up_lf, textvariable=self.new_name, width="23")  # 创建一个注册名的`entry`，变量为`new_name`
        self.entry_new_name.place(x=80, y=10)  # `entry`放置在坐标（150,10）.

        self.new_pwd = StringVar()
        Label(self.sign_up_lf, text='密   码：').place(x=20, y=40)
        self.entry_usr_pwd = Entry(self.sign_up_lf, textvariable=self.new_pwd, show='*', width="23")
        self.entry_usr_pwd.place(x=80, y=40)

        self.new_pwd_confirm = StringVar()
        Label(self.sign_up_lf, text='确   认：').place(x=20, y=70)
        self.entry_usr_pwd_confirm = Entry(self.sign_up_lf, textvariable=self.new_pwd_confirm, show='*', width="23")
        self.entry_usr_pwd_confirm.place(x=80, y=70)
        self.btn_comfirm_sign_up = Button(self.sign_up_lf, text='提   交', width="8")
        self.btn_comfirm_sign_up.place(x=102, y=110)





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

    # 登陆功能函数
    def usr_login(self):
        usr_name = self.var_usr_name.get()
        usr_pwd = self.var_usr_pwd.get()
        m2 = hashlib.md5()
        m2.update(("++"+usr_pwd+"--").encode("utf-8"))
        usr_pwd = m2.hexdigest()
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
        sql = "SELECT * FROM python_user WHERE user='%s'"

        try:
            cursor.execute(sql % usr_name)
            # 使用execute()方法执行SQL语句
            data = cursor.fetchall()

            sql_user = data[0][1]
            sql_pwd = data[0][2]

            if sql_user == usr_name and sql_pwd == usr_pwd:
                self.write_log_to_Text("INFO:登陆成功") #登陆成功，在日志窗口显示
                messagebox.showinfo('登陆成功', '尊敬的 [%s] 您好，欢迎使用360广告点击器！' % usr_name)
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

def gui_start():
    init_window = Tk()  # 实例化出一个父窗口
    ZMJ_PORTAL = MY_GUI(init_window)
    # 设置根窗口默认属性
    ZMJ_PORTAL.set_init_window()

    init_window.mainloop()  # 父窗口进入事件循环，可以理解为保持窗口运行，否则界面不展示

gui_start()