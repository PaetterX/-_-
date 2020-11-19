import data_ss,reexception
import uiautomator2 as u2
import os,sys
import json
import time
import pytz
import pytesseract
import shutil
import getpass
from PIL import Image
from datetime import datetime
from io import StringIO
import win32gui,win32con

def get_wmsize():
    text = os.popen('adb shell wm size').read()
    seq = ':'
    rest = text.split(seq, 1)[-1]
    e = rest.strip()
    seq2 = 'x'
    global wmsize_x
    wmsize_x = int(e.split(seq2, 1)[0])
    global wmsize_y
    wmsize_y = int(e.split(seq2, 1)[-1])


mark_1 = StringIO()
mark_1.write('0')
mark_2 = StringIO()
mark_2.write('0')
mark_3 = StringIO()
mark_3.write('0')
mark_4 = StringIO()
mark_4.write('0')

get_wmsize()
path_root = os.path.abspath('.')

def click_to(d, image_name):

    value = data_ss.data_ss(image_name)
    value_se = value.search()

    click_swi(value_se)
    d.click(value_se_x,value_se_y)

def click_swi(value_se):
    global value_se_x
    value_se_x = value_se[0] * wmsize_x

    global value_se_y
    value_se_y = value_se[-1] * wmsize_y

def click_per(px, py, d):
    px2 = px * wmsize_x
    py2 = py * wmsize_y
    d.click(px2, py2)

def click_match(d, image_name):
    value = data_ss.data_ss(image_name)
    value_se = value.search()
    dispatch_images(image_name, d)
    if value_se[0] > test_x + 0.05 or value_se[0] < test_x - 0.05:
        return False
    elif value_se[-1] > test_y + 0.05 or value_se[-1] < test_y -0.05:
        return False
    else:
        return True

    
def dispatch_images(image_name, d):
    imdata_pic = get_path(image_name)
    test_image = d.image.match(imdata_pic)
    global sim
    sim = test_image['similarity']
    global test_x
    test_x = test_image['point'][0] / wmsize_x
    global test_y
    test_y = test_image['point'][1] / wmsize_y

def data_has_key(image_name):
    if data_ss.data_ss(image_name).search():
        return True
    else:
        return False

def get_path(image_name):
    path_root = os.path.abspath('.')
    return path_root + '\\img\\' + image_name + '.png'

def sim_match(d, image_name):
    dispatch_images(image_name, d)
    if sim > 0.99:
        return True
    else:
        return False

def match_select(d, image_name):
    if data_has_key(image_name):
        return True
    else:
        return False

def guess_to_do(image_name, d):
    if match_select(d, image_name):
        loop_num_data(d, image_name)
    else:
        loop_num_sim(d, image_name)

def loop_num_data(d, image_name):
    global error_mark
    error_mark = 12
    while error_mark:        
        if click_match(d, image_name):
            time.sleep(2)
            click_to(d, image_name)
            break
        else:
            time.sleep(1)
            error_mark -= 1
    if error_mark == 0:
        #reexception.justclick2(d)
        mark_1.write('1')


def loop_num_sim(d, image_name):
    global error_mark
    error_mark = 10
    while error_mark:
        if sim_match(d, image_name):
            time.sleep(1)
            d.image.click(get_path(image_name))
            break
        else:
            time.sleep(1)
            error_mark -= 1
    if error_mark == 0:
        mark_2.write('1')

def action_chain(list, d):
    if int(mark_4.getvalue()) - 1:
        if int(mark_3.getvalue()) - 2:
            tran(list, d)
        else:
            reexception.clickall(d)
            mark_3.write('0')
            mark_4.write(str(int(mark_4.getvalue()) + 1))
    else:
        reexception.restart_app(d)
        mark_4.write('0')
        

def tran(list, d):
    if int(mark_2.getvalue()):
        reexception.justclick2(d)
        mark_2.write('0')
    else:
        for item in list:
            if not click_match(d, item):
                mark_1.write('1')
            if int(mark_1.getvalue()):
                reexception.justclick2(d)
                mark_1.write('0')
                mark_3.write(str(int(mark_3.getvalue()) + 1))
            else:
                guess_to_do(item,d)
                mark_3.write('0')
                mark_4.write('0')
                time.sleep(1)

def click_longer(d, image_name):
    dispatch_images(image_name, d)
    px = test_x * wmsize_x
    py = test_y * wmsize_y
    most_wait = 10
    while most_wait:
        if click_match(d, image_name):
            time.sleep(1.5)
            d.long_click(px, py, 8)
            break
        time.sleep(1)
        most_wait -= 1

def read_json(event_name):
    with open('data.json', 'r') as file:
        str = file.read()
        data = json.loads(str)
        value_jud = data[0].get(event_name)
    return value_jud

def write_json(event_name, para):
    with open('data.json', 'w+', encoding='utf-8') as file:
        str = file.read()
        data = json.loads(str)
        time_str = time_refresh()
        data[0][event_name] = [time_str, para]
        file.write(json.dumps(data, indent=2, ensure_ascii=False))

def time_refresh():
    tz = pytz.timezone('Europe/Moscow')
    time_str = datetime.now(tz).strftime("%Y-%m-%d")
    return time_str

def jud_json(event_name):
    #今天做过这个动作吗？
    jud_list = read_json(event_name)
    time_str_jud = time_refresh()
    if jud_list[0] == time_str_jud and jud_list[1] == 1:
        return True
    else:
        return False

def scr_ocr(screen_shot):
    #没用了
    path_root = os.path.abspath('.')
    image = Image.open(path_root + '/img/' + screen_shot + '.png')
    text = pytesseract.image_to_string(image, lang='eng', config='--psm 6 --psm 13')
    text = text.strip().replace(' ','')
    return text

def scr_shot(screen_shot = 'screenshot'):
    scr_pic = get_path(screen_shot)  
    os.popen('uiautomator2 screenshot ' + scr_pic)
    #迷之OSError不影响运行


def cut_scr(x1, y1, x2, y2, cut_pic):
    path_root = os.path.abspath('.')
    image = Image.open(path_root + '/img/' + cut_pic + '.png')
    region = image.crop((x1, y1, x2, y2))
    return region

def cut_ocr(region):
    text = pytesseract.image_to_string(region, lang='eng', config='--psm 6 --psm 13')
    text = text.strip().replace(' ','')
    return text

def jud_pht_shi(text):
    scr_shot()
    region = cut_scr(0.618, 0.028, 0.636, 0.049, 'screenshot')
    text = cut_ocr(region)
    try:
        if int(text) > 75:
            return True
        else:
            return False
    except:
        return False


def jud_pht_hard(text):
    scr_shot()
    region = cut_scr(0.618, 0.028, 0.636, 0.049, 'screenshot')
    text = cut_ocr(region)
    try:
        if int(text) > 60:
            return True
        else:
            return False
    except:
        return False

def jud_pht_norm(text):
    scr_shot()
    region = cut_scr(0.618, 0.028, 0.636, 0.049, 'screenshot')
    text = cut_ocr(region)
    try:
        if int(text) > 10:
            return True
        else:
            return False
    except:
        return False

def settings_read(set_name):
    with open(path_root + r'\settings.json','r') as file:
        str = file.read()
        sett = json.loads(str)
        back_value = sett[0][set_name]
    return back_value

# def data_read(set_name):
#     with open(path_root + r'\settings.json','r') as file:
#         str = file.read()
#         data_str = json.loads(str)
#     return data_str[0][set_name]


def set_time():
    with open(path_root + r'\settings.json','r+') as file:
        str = file.read()
        str = json.loads(str)
        str[0]["时间"] = datetime.now().timestamp()
        file.write(json.dumps(str,indent=2,ensure_ascii=False))

def kill_and():
    pr_name = settings_read("位置")
    seq = '/'
    pr_name = pr_name.split(seq)[-1]
    os.system('%s%s' % ("taskkill /F /IM ",pr_name))


def hide_and():
    pr_name = settings_read("位置")
    seq = '/'
    pr_name = pr_name.split(seq)[-1]
    seq2 ='.'
    pr_name = pr_name.split(seq2)[0]
    ANDR = win32gui.FindWindow(None, pr_name)
    win32gui.ShowWindow(ANDR,win32con.SW_HIDE)

def show_and():
    pr_name = settings_read("位置")
    seq = '/'
    pr_name = pr_name.split(seq)[-1]
    seq2 ='.'
    pr_name = pr_name.split(seq2)[0]
    ANDR = win32gui.FindWindow(None, pr_name)
    win32gui.ShowWindow(ANDR,win32con.SW_SHOW)

def start_auto():
    user_name_0 = getpass.getuser()
    with open(path_root + r'\start_auto.bat','w') as file:
        file.write('python ' + path_root + r'\inter_face.py')
    with open(path_root + r'\start_auto.vbs','w') as file:
        file.write('set ws=wscript.createobject("wscript.shell")' + '\n' + 'ws.run "' + path_root + '\start_auto.bat' + ' /start",0')
    shutil.move(path_root + '/start_auto.vbs', 'c:/users/' + user_name_0 + '/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Startup')
    



