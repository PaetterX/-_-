import data_ss,toolss
import uiautomator2 as u2
import time

def justclick(d, self=False):
    if self:
        for i in range(5):
            toolss.click_per(0.016, 0.049, d)
            time.sleep(0.2)
            toolss.click_per(0.054, 0.975, d)
            time.sleep(0.2)

def justclick2(d):
    for i in range(8):
        toolss.click_per(0.99, 0.99, d)
        time.sleep(0.4)


def clickall(d):
    for y in range(0, 100, 5):
        for x in range(0, 100, 5):
            if not toolss.click_match(d, 'story'):
                toolss.click_per(x / 100, y / 100, d)
                time.sleep(0.15)


def click_upgrade(d, self=False):
    pass

def restart_app(d):
    d.app_stop("com.bilibili.priconne")
    time.sleep(4)
    d.app_start("com.bilibili.priconne")

def restart_android(d, self=False):
    pass

def skip_nonsense(d, self=False):
    pass