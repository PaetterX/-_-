import start
import toolss
import os
import time

def letsgo():
    
    os.system(toolss.settings_read('位置'))
    time.sleep(2)
    d = start.startproject_d()
    time.sleep(5)
    start.startapp(d)
    









    toolss.kill_and()

    toolss.set_time()


if __name__ == '__main__':
    letsgo()