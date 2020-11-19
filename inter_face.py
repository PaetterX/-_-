import tkinter as tk
from tkinter.filedialog import askopenfilename
import toolss
import json
import os
import threading
import time
import redive
import webbrowser
from multiprocessing import Process
from datetime import datetime

welcome_png = toolss.get_path('welcome')


window = tk.Tk()
window.title('我的圣光啊')
window.geometry('960x540')

window.resizable(0,0)

def click_lin(event):
    webbrowser.open('www.baidu.com')

image_file = tk.PhotoImage(file=welcome_png)


tk.Label(window, image = image_file).pack(side='top')



def open_job():
    file_path=askopenfilename(title='选择模拟器的位置', filetypes=[('EXE', '*.exe'), ('All Files', '*')],initialdir='C:\\')
    sett[0]["位置"] = file_path
    write_json(sett)

def hide_and_show_gen():
    while True:
        toolss.show_and()
        a = yield 0
        toolss.hide_and()
        a = yield 0
gen_hs = hide_and_show_gen()
def hide_and_show():
    next(gen_hs)

menubar = tk.Menu(window)
filemenu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label='---点击这里来告诉我，你把模拟器放在哪了？---', menu=filemenu)
filemenu.add_command(label='选择模拟器的位置', command=open_job)

filemenu.add_separator()
filemenu.add_command(label='显示/隐藏模拟器窗口', command=hide_and_show)
filemenu.add_command(label='添加到开机启动项', command=toolss.start_auto)
# filemenu.add_command(label='退出', command=window.quit)

# editmenu = tk.Menu(menubar, tearoff=0)
# menubar.add_cascade(label='Edit', menu=editmenu)
# editmenu.add_command(label='Cut', command=do_job)
# editmenu.add_command(label='Copy', command=do_job)
# editmenu.add_command(label='Paste', command=do_job)

# submenu = tk.Menu(filemenu)
# filemenu.add_cascade(label='Import', menu=submenu, underline=0)
# submenu.add_command(label="Submenu1", command=do_job)

tk.Label(window, text='(需通关)扫荡主线最新28张\n某装备数量<40的图').place(x=20, y= 150)
tk.Label(window, text='呼出编组一(需事先设置队伍)清竞技场\n公主竞技场次数').place(x=230, y= 150)
tk.Label(window, text='呼出编组二(需事先设置)每日打\n一次沧海的孤塔').place(x=500, y= 150)
tk.Label(window, text='R11及以上角色自动\n穿装备并提升角色等级').place(x=710, y= 150)
tk.Label(window, text='每日自动抽无料十连\n（如果有的话）').place(x=30, y= 250)
tk.Label(window, text='每天复活，呼出编组二(需事先设置)\n推露娜塔普层及EX').place(x=230, y= 250)
tk.Label(window, text='(需通关)扫荡活动H图与困难boss\n然后抽券并领活动奖励').place(x=490, y= 250)
tk.Label(window, text='呼出编组三(需事先设置)使用自动\n出会长血压三刀').place(x=690, y= 250)
tk.Label(window, text='未写明的功能： 探索,点赞,领小屋,领任务,领礼物,\n打最新6张h图,n2n3自动三管且不打圣迹\n距离上一次正常结束八小时后再次上线清日常\n\n推荐使用win10与蓝叠模拟器(readme.txt内附链接)\n必须把头像改成全兰德索尔最可爱(头最大)的初音\nbug反馈请发邮件至1459903181@qq.com\n项目开源于github。MIT').place(x=20, y= 380)

path_root = os.path.abspath('.')
def open_json_i():
    global sett
    with open(path_root + r'\settings.json','r') as file:
        str = file.read()
        sett = json.loads(str)
open_json_i()

def write_json(str):
    with open(path_root +r'\settings.json','w') as file:
        file.write(json.dumps(str,indent=2,ensure_ascii=False))

var = tk.StringVar()
var.set(sett[0].get('主线'))
var2 = tk.StringVar()
var2.set(sett[0].get('竞技场'))
var3 = tk.StringVar()
var3.set(sett[0].get('地下城'))
var4 = tk.StringVar()
var4.set(sett[0].get('穿装备'))
var5 = tk.StringVar()
var5.set(sett[0].get('无料十连'))
var6 = tk.StringVar()
var6.set(sett[0].get('露娜塔'))
var7 = tk.StringVar()
var7.set(sett[0].get('活动'))
var8 = tk.StringVar()
var8.set(sett[0].get('会战'))



l = tk.Label(window, bg='yellow', width=25, text='empty')
l.place(x=380, y= 500)
l.config(text='离下次上线还有 ' + '')


def hit_me():
    sett[0]["时间"] = datetime.now().timestamp() - 28790

b = tk.Button(window, text='砸瓦鲁多', width=10,
              height=1, command=hit_me)
b.place(x = 425, y = 460)

def test_mul2():
    while True:
        walk_time = datetime.now().timestamp() - sett[0]["时间"]
        if 28800 - walk_time > 0:
            rest_time = 28800 - walk_time
            m, s = divmod(rest_time, 60)
            h, m = divmod(m, 60)
            l.config(text='离下次上线还有 ' + '%02d:%02d:%02d' % (h, m, s))
        else:
            l.config(text='计时结束，开始运行')
            #redive.letsgo()
            open_json_i()
        time.sleep(1)
            

# def print_selection():
#     l.config(text='you have selected ' + var.get())



def print_selection():
    sett[0]['主线'] = var.get()
    write_json(sett)
def print_selection2():
    sett[0]['竞技场'] = var2.get()
    write_json(sett)
def print_selection3():
    sett[0]['地下城'] = var3.get()
    write_json(sett)
def print_selection4():
    sett[0]['穿装备'] = var4.get()
    write_json(sett)
def print_selection5():
    sett[0]['无料十连'] = var5.get()
    write_json(sett)
def print_selection6():
    sett[0]['露娜塔'] = var6.get()
    write_json(sett)   
def print_selection7():
    sett[0]['活动'] = var7.get()
    write_json(sett)
def print_selection8():
    sett[0]['会战'] = var8.get()
    write_json(sett)
#r1.pack()

a1 = tk.Radiobutton(window, text='是',
                    variable=var, value=1,
                    command=print_selection)
a1.place(x=20, y= 200)
a2 = tk.Radiobutton(window, text='否',
                    variable=var, value=0,
                    command=print_selection)
a2.place(x=80, y= 200)
b1 = tk.Radiobutton(window, text='是',
                    variable=var2, value=1,
                    command=print_selection2)
b1.place(x=260, y= 200)
b2 = tk.Radiobutton(window, text='否',
                    variable=var2, value=0,
                    command=print_selection2)
b2.place(x=320, y= 200)
c1 = tk.Radiobutton(window, text='是',
                    variable=var3, value=1,
                    command=print_selection3)
c1.place(x=530, y= 200)
c2 = tk.Radiobutton(window, text='否',
                    variable=var3, value=0,
                    command=print_selection3)
c2.place(x=590, y= 200)
d1 = tk.Radiobutton(window, text='是',
                    variable=var4, value=1,
                    command=print_selection4)
d1.place(x=710, y= 200)
d2 = tk.Radiobutton(window, text='否',
                    variable=var4, value=0,
                    command=print_selection4)
d2.place(x=770, y= 200)


e1 = tk.Radiobutton(window, text='是',
                    variable=var5, value=1,
                    command=print_selection5)
e1.place(x=20, y= 300)
e2 = tk.Radiobutton(window, text='否',
                    variable=var5, value=0,
                    command=print_selection5)
e2.place(x=80, y= 300)
f1 = tk.Radiobutton(window, text='是',
                    variable=var6, value=1,
                    command=print_selection6)
f1.place(x=260, y= 300)
f2 = tk.Radiobutton(window, text='否',
                    variable=var6, value=0,
                    command=print_selection6)
f2.place(x=320, y= 300)
g1 = tk.Radiobutton(window, text='是',
                    variable=var7, value=1,
                    command=print_selection7)
g1.place(x=530, y= 300)
g2 = tk.Radiobutton(window, text='否',
                    variable=var7, value=0,
                    command=print_selection7)
g2.place(x=590, y= 300)
h1 = tk.Radiobutton(window, text='是',
                    variable=var8, value=1,
                    command=print_selection8)
h1.place(x=710, y= 300)
h2 = tk.Radiobutton(window, text='否',
                    variable=var8, value=0,
                    command=print_selection8)
h2.place(x=770, y= 300)

window.config(menu=menubar)




# def test_mul():
#     while True:  
#         print('OK')
#         time.sleep(1)


if __name__ == '__main__':
    # th = threading.Thread(target=test_mul)
    th2 = threading.Thread(target=test_mul2)
    # th.setDaemon(1)
    th2.setDaemon(1)
    # th.start()
    th2.start()
    window.mainloop()