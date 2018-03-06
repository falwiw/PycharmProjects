#!/usr/bin/python
# -*- coding: UTF-8 -*-
import tkinter as tk

root = tk.Tk()
root.title("登陆器测试")
root.geometry("550x340")

#LabelFrame 1 登陆及帐户信息
lf1 = tk.LabelFrame(root, text="登陆信息", width=240, height=150)
lf1.place(x=10, y=10)

tk.Label(lf1, text="用户名：").place(x=5, y=5)
tk.Label(lf1, text="密   码：").place(x=5, y=40)
tk.Entry(lf1, text="", width=20).place(x=75, y=5)
tk.Entry(lf1, text="", width=20, show="*").place(x=75, y=40)
tk.Button(lf1, text="登陆", width=8).place(x=30, y=80)
tk.Button(lf1, text="注册", width=8).place(x=140, y=80)

#LabelFrame 2 日志信息显示
lf2 = tk.LabelFrame(root, text="日志信息", width=240, height=155)
lf2.place(x=10, y=170)

#LabelFrame 3
lf3 = tk.LabelFrame(root, text="设置1", width=270, height=150)
lf3.place(x=270, y=10)
tk.Label(lf3, text="联盟选择：", width=8, fg="blue").place(x=5, y=5)
ssp = tk.IntVar()
ssp.set(3)
tk.Radiobutton(lf3, text="搜狗联盟", variable=ssp, value=1).place(x=5, y=30)
tk.Radiobutton(lf3, text="百度联盟", variable=ssp, value=2).place(x=98, y=30)
tk.Radiobutton(lf3, text="360联盟", variable=ssp, value=3).place(x=188, y=30)

tk.Label(lf3, text="词库选择：", width=8, fg="blue").place(x=5, y=70)
keyword = tk.IntVar()
keyword.set(3)
tk.Radiobutton(lf3, text="词库3", variable=keyword, value=1).place(x=5, y=95)
tk.Radiobutton(lf3, text="词库2", variable=keyword, value=2).place(x=98, y=95)
tk.Radiobutton(lf3, text="词库1", variable=keyword, value=3).place(x=188, y=95)

#LabelFrame 4
lf4 = tk.LabelFrame(root, text="设置2", width=270, height=120)
lf4.place(x=270, y=170)

adsclick1 = tk.IntVar()  #推广链接点击个数1
adsclick1.set("3")
adsclick2 = tk.IntVar()  #推广链接点击个数2
adsclick2.set("3")
tk.Label(lf4, text="推广链接点击个数：").place(x=5, y=0)
tk.Entry(lf4, textvariable=adsclick1, width=3).place(x=120, y=0)
tk.Label(lf4, text="~         (随机)").place(x=145, y=0)
tk.Entry(lf4, textvariable=adsclick2, width=3).place(x=160, y=0)

searchclick1 = tk.IntVar()  #搜索结果点击个数1
searchclick1.set("1")
searchclick2 = tk.IntVar()  #搜索结果点击个数2
searchclick2.set("3")
tk.Label(lf4, text="搜索结果点击个数：").place(x=5, y=25)
tk.Entry(lf4, textvariable=searchclick1, width=3).place(x=120, y=25)
tk.Label(lf4, text="~         (随机)").place(x=145, y=25)
tk.Entry(lf4, textvariable=searchclick2, width=3).place(x=160, y=25)

delaytime1 = tk.IntVar()  #浏览窗口停留时间1
delaytime1.set("60")
delaytime2 = tk.IntVar()  #浏览窗口停留时间2
delaytime2.set("300")
tk.Label(lf4, text="浏览窗口停留时间：").place(x=5, y=50)
tk.Entry(lf4, textvariable=delaytime1, width=3).place(x=120, y=50)
tk.Label(lf4, text="~         (秒)").place(x=145, y=50)
tk.Entry(lf4, textvariable=delaytime2, width=3).place(x=160, y=50)

timeryear = tk.IntVar()  #定时 年
timeryear.set("2018")
timermonth = tk.IntVar()  #定时 月
timermonth.set("3")
timerday = tk.IntVar()  #定时 日
timerday.set("4")
timerhour = tk.IntVar()  #定时 时
timerhour.set("8")
timerbranch = tk.IntVar()  #定时 分
timerbranch.set("0")
tk.Label(lf4, text="定时时间：           -      -            :       (定时)").place(x=5, y=75)
tk.Entry(lf4, textvariable=timeryear, width=4).place(x=79, y=75)
tk.Entry(lf4, textvariable=timermonth, width=2).place(x=120, y=75)
tk.Entry(lf4, textvariable=timerday, width=2).place(x=148, y=75)
tk.Entry(lf4, textvariable=timerhour, width=2).place(x=172, y=75)
tk.Entry(lf4, textvariable=timerhour, width=2).place(x=200, y=75)
# 保存
tk.Button(root, text="保存", width=6).place(x=270, y=295)
tk.Button(root, text="开始", width=6).place(x=344, y=295)
tk.Button(root, text="暂停", width=6).place(x=415, y=295)
tk.Button(root, text="停止", width=6).place(x=487, y=295)
# 组件隐藏
# lf1.pack_forget()
root.mainloop()