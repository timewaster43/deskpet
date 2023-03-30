# -*- coding: gb18030 -*-
from tkinter import Tk, Label, messagebox
import tkinter
from PIL import Image, ImageTk
from pystray import Icon, MenuItem
import random
import sys

sentence = ['好好学习','不要摸鱼','快去打球','快！帮我刷一下','快上号！','请我吃饭','关我什么事','啊？']#导入的引用句
def show_window(icon):# 显示窗口
    root.deiconify()

def quit_app(icon):# 退出
    icon.stop()
    root.destroy()

def move_window(event):# 拖动窗口函数
    root.geometry(f'+{event.x_root}+{event.y_root}')

def talk():# 对话框
    messagebox.showinfo("眼罩说", sentence[random.randint(1,8)-1])

def kill():# 退出程序
    sys.exit()



root = Tk()# 创建叫做root的tk窗口
root.title("deskpet")# 标题
root.overrideredirect(True)
root.attributes("-topmost", True)# 窗口置顶
root.configure(bg='white')# 将背景设置成白色
root.attributes('-transparentcolor', 'white')# 将白色透明
# root.withdraw()

image = Image.open("assets/icon.png")# 加载托盘图标
icon = Icon("zyz Icon", image)
icon.menu = (MenuItem("Show Window", show_window), MenuItem("Quit", quit_app))# 托盘菜单
# icon.run()

image = Image.open("assets/zyz.png")# 加载主要图片
photo = ImageTk.PhotoImage(image)
label = Label(root, image=photo)# 标出图片
label.pack(side="right")# 将图片放在右侧
root.bind('<B1-Motion>', move_window)# 按住鼠标左键执行移动窗口函数

# show_window(icon)

# 使用按钮控件调用函数
appearance = tkinter.Button(root, text="眼罩说", command=talk, width=4, height=2)
appearance.pack(anchor="ne")

quiting = tkinter.Button(root, text="退出", command=kill, width=4, height=2)
quiting.pack(anchor="ne")

root.mainloop()
