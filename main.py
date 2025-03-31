from tkinter import Tk, Label, messagebox, Button
from PIL import Image, ImageTk
from pystray import Icon, MenuItem
import random
import threading
import sys
import os

root_size = 96

script_dir = os.path.dirname(os.path.abspath(__file__)) #获取当前脚本路径
new_dir = script_dir.replace('\\', '/') #替换路径符号
pic1_path = new_dir+"/img/pic1.png" #定义图片1路径
pic2_path = new_dir+"/img/pic2.png" #定义图片2路径

sentence = ['走去小卖部','快去打球','我没带饭卡，帮我刷一下','快上号！','请我吃饭','关我什么事', '去码头整点薯条', '去占场', '一般吧', '蠢猪坐后面']#导入的引用句
def show_window(icon):# 显示窗口
    root.deiconify()

def quit_app(icon):# 退出
    icon.stop()
    root.destroy()

def move_window(event):# 拖动窗口函数
    win_x = root.winfo_x()
    win_y = root.winfo_y()
    mouse_x, mouse_y = event.widget.winfo_pointerxy()
    print("%f, %f, %f, %f" % (win_x, win_y, mouse_x, mouse_y))
    root.geometry(f'+{mouse_x-int(root_size/2)}+{mouse_y-int(root_size/2)}')

def talk(event):# 对话框
    global icon
    messagebox.showinfo("海鸥说", sentence[random.randint(0, len(sentence)-1)])

def image_sit(event):
    new_image = Image.open(pic1_path)  # 加载新图片
    resized_new_img = new_image.resize((root_size, root_size))
    new_image = ImageTk.PhotoImage(resized_new_img)  # 转换为 Tkinter 格式
    label.config(image=new_image)  # 更新图片
    label.image = new_image  # 避免垃圾回收


def image_stand(event):
    new_image = Image.open(pic2_path)  # 加载新图片
    resized_new_img = new_image.resize((root_size, root_size))
    new_image = ImageTk.PhotoImage(resized_new_img)  # 转换为 Tkinter 格式
    label.config(image=new_image)  # 更新图片
    label.image = new_image  # 避免垃圾回收

def run_tray():
    global menu, icon_img
    icon = Icon("去码头整点薯条", icon_img, "一只可以rua的海鸥桌宠", menu)
    icon.run()


print("脚本所在目录:", script_dir)

root = Tk()# 创建叫做root的tk窗口
root.title("deskpet")# 标题
root.overrideredirect(True)
root.attributes("-topmost", True)# 窗口置顶
root.configure(bg='white')# 将背景设置成白色
root.attributes('-transparentcolor', 'white')# 将白色透明
# root.withdraw()

# image = Image.open("d:/SystemPath/Documents/Programming/Python/deskpet/img/icon.png")# 加载托盘图标
# icon = Icon("zyz Icon", image)
# icon.menu = (MenuItem("Show Window", show_window), MenuItem("Quit", quit_app))# 托盘菜单
# icon.run()

menu = (MenuItem(text='退出', action=quit_app),
)
icon_img = Image.open(pic1_path)


image = Image.open(pic1_path)# 加载主要图片
resized_img = image.resize((root_size, root_size))
photo = ImageTk.PhotoImage(resized_img)
label = Label(root, image=photo, bg="#ffffff", fg="#000000")# 标出图片
label.pack(side="right")# 将图片放在右侧
root.bind('<ButtonRelease-1>', talk)
root.bind('<Enter>', image_stand)
root.bind('<Leave>', image_sit)
root.bind('<B3-Motion>', move_window)# 按住鼠标右键执行移动窗口函数


# menu = (MenuItem(text='菜单1', action=click_menu), MenuItem(text='菜单2', action=click_menu),
#         MenuItem(text='菜单3', action=click_menu, enabled=False),
#         MenuItem(text='发送通知', action=notify),
#         MenuItem(text='我是点击图标的菜单', action=click_menu, default=True, visible=False),
#         MenuItem(text='退出', action=on_exit),
#         )



# show_window(icon)

# 使用按钮控件调用函数

# appearance = tkinter.Button(root, text="眼罩说", command=talk, width=4, height=2)
# appearance.pack(anchor="ne")

# quiting = Button(root, text="退出", command=kill, width=4, height=2)
# quiting.pack(anchor="ne")

# 启动托盘图标线程
tray_thread = threading.Thread(target=run_tray, daemon=True)
tray_thread.start()

root.mainloop()
