import uiautomator2 as u2
import os
import start,reexception
import win32api,win32con
import time

def startapp(d):
    d.app_start("com.bilibili.priconne")


#emulator-5554          device product:OnePlus5 model:ONEPLUS_A5000 device:OnePlus5 transport_id:1
def startproject_d():
    def Adb_ini():
        adb_ini = os.popen('adb devices -l').read()
        return True if adb_ini.find('ist of devices attached') else False

    def Adb_check():
        os.popen('adb kill-server')
        adb_check = os.popen('adb devices -l').read()
        return True if adb_check.find('device product') else False


    ini_count_try = 3
    connect_count_try = 7
    ini_mark = False
    connect_mark = False

    while ini_count_try:
        if not Adb_ini():
            ini_count_try -= 1
            time.sleep(5)
        else:
            ini_mark = True
            break

    if ini_mark == True:
        while connect_count_try:
            if not Adb_check():
                connect_count_try -= 1
                time.sleep(5)
            else:
                connect_mark = True
                break

    if connect_mark == True:
        try:
            d = u2.connect('emulator-5554')
        except RuntimeError:
            try:
                d = u2.connect()
            except Exception as e:
                with open('error.txt','a') as f:
                    f.write(str(e) + '\n')
                win32api.MessageBox(0, "异常写入error.txt", "意外错误",win32con.MB_OK)
    else:
        win32api.MessageBox(0, "没有发现打开adb调试的安卓模拟器", "Error",win32con.MB_OK)
        d = None
    
    return d