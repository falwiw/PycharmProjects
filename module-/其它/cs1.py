#!/usr/bin/python
# -*- coding: UTF-8 -*-
from tkinter import *
import tkinter as tk

"""
#Button组件例子
def callback():
    var.set("吹吧你，我才不信呢！")

root = Tk()
frame1 = Frame(root)
frame2 = Frame(root)
var = StringVar()
var.set("您所下载的影片包含未成年人限制内容，\n 请满18岁后再点击观看！")
textLabel = Label(frame1, textvariable=var, justify=LEFT)
textLabel.pack(side=LEFT)

photo = PhotoImage(file="1.png")
imgLabel = Label(frame1, image=photo)
imgLabel.pack(side=RIGHT)

theButton = Button(frame2, text="已满满18岁", command=callback)
theButton.pack()
frame1.pack(padx=10, pady=10)
frame2.pack(padx=10, pady=10)

mainloop()
"""
"""
#Checbutton组件例子
root = Tk()
GIRLS = ["西施", "王昭君", "貂蝉", "杨玉环"]
v = []
for girl in GIRLS:
    v.append(IntVar())
    b = Checkbutton(root, text=girl, variable=v[-1])
    b.pack(side = LEFT)
    l = Label(root, textvariable=v)
    l.pack(side = LEFT)
mainloop()
"""
"""
# LabelFrame组件
root = Tk()
group = LabelFrame(root, text="最好的脚本语言是？", padx=5, pady=5)
group.pack(padx=10, pady=10)
LANGS = [
    ("Python", 1),
    ("Perl", 2),
    ("Ruby", 3),
    ("Lua", 4)]
v = IntVar()
v.set(1)
for lang, num in LANGS:
    b = Radiobutton(group, text=lang, variable=v, value=num)
    b.pack(anchor=W)

mainloop()
"""

"""
# Entry组件
root = Tk()
e = Entry(root)
e.pack(padx=20, pady=20)
e.delete(0, END)
e.insert(0, "默认文本...")
mainloop()
"""
"""
# Entry组件2
root = Tk()
Label(root, text="作品：").grid(row=0)
Label(root, text="作者：").grid(row=1)
e1 = Entry(root)
e2 = Entry(root)
e1.grid(row=0, column=1, padx=10, pady=5)
e2.grid(row=1, column=1, padx=10, pady=5)

def show():
    print("作品：《%s》" % e1.get())
    print("作者：%s" % e2.get())
    e1.delete(0, END)
    e2.delete(0, END)

Button(root, text="获取信息", width=10, command=show).grid(row=3, column=0, sticky=W, padx=10, pady=5)
Button(root, text="退出", width=10, command=root.quit()).grid(row=3, column=1, sticky=E, padx=10, pady=5)
mainloop()

"""
# Entry组件3
root = Tk()
root.title("360 Ssp登陆器")
Label(root, text="帐号：").grid(row=0)
Label(root, text="密码：").grid(row=1)
v1 = StringVar()
v2 = StringVar()
e1 = Entry(root, textvariable=v1)
e2 = Entry(root, textvariable=v2, show="*")
e1.grid(row=0, column=1, padx=10, pady=5)
e2.grid(row=1, column=1, padx=10, pady=5)

def show():
    print("帐号：%s" % v1.get())
    print("密码：%s" % v2.get())
    e1.delete(0, END)
    e2.delete(0, END)

Button(root, text="登陆", width=10, command=show).grid(row=3, column=0, sticky=W, padx=10, pady=5)
Button(root, text="退出", width=10, command=root.quit()).grid(row=3, column=1, sticky=E, padx=10, pady=5)
mainloop()













