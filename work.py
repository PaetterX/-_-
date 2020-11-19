import data_ss,toolss,start,reexception
import uiautomator2 as u2
import os
import time

d = u2.connect()
def dianzan(d):
    toolss.click_per(0.054, 0.975, d)
    list_dianzan = ['guild', 'member', 'agree']
    toolss.action_chain(list_dianzan, d)

def tansuo(d):
    list_tansuo1 = ['adventure', 'explore', 'empiricalvalue']
    toolss.action_chain(list_tansuo1, d)
    time.sleep(5)
    toolss.click_per(0.71875, 0.2759259259259259, d) 
    toolss.click_longer(d, 'add')
    list_tansuo2 = ['use', 'ok_blue', 'skip', 'back_to_explore', 'mana']
    toolss.action_chain(list_tansuo2, d)        
    time.sleep(5)
    toolss.click_per(0.71875, 0.2759259259259259, d) 
    toolss.click_longer(d, 'add')
    list_tansuo3 = ['use', 'ok', 'skip', 'back_to_explore']
    toolss.action_chain(list_tansuo3, d)

def shouxiaowu(d):
    list_xiaowu = ['house', 'receiveall']
    toolss.action_chain(list_xiaowu, d)

def sheng_ji(d):
    list_shengji1 = ['adventure', 'investigation']
    toolss.action_chain(list_shengji1, d)
    time.sleep(5)
    toolss.click_per(0.71875, 0.2759259259259259, d)
    toolss.click_longer(d, 'add')
    list_shengji2 = ['use', 'ok_blue', 'skip', 'ok_white']
    toolss.action_chain(list_shengji2, d)

def niudan(d):
    list_niudan = ['hell', 'commonlottery', 'do_commonlottery']
    toolss.action_chain(list_niudan, d)

def lingrenwu(d):
    list_renwu = ['index', 'to_do', 'receive_gift', 'close_white', 'back']
    toolss.action_chain(list_renwu, d)

def lingliwu(d):
    list_liwu = ['gift', 'receive_gift', 'ok_blue']
    toolss.action_chain(list_liwu, d)

def nei_gui(d):
    list_neigui = ['adventure', 'teamwar', '......']
    toolss.action_chain(list_neigui, d)

