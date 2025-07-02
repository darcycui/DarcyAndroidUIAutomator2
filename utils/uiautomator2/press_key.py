import time
import uiautomator2 as u2

from utils.date_time_util import delay

'''
支持的按键
home
back
left
right
up
down
center
menu
search
enter
delete ( or del)
recent (recent apps)
volume_up
volume_down
volume_mute
camera
power
'''


def press_back(device: u2.Device):
    print('点击返回键')
    delay(3)
    device.press('back')


def press_home(device: u2.Device):
    print('点击Home键')
    delay(1)
    device.press('home')


def press_menu(device: u2.Device):
    print('点击Menu键')
    delay(1)
    device.press('menu')


def press_recent(device: u2.Device):
    print('点击最近任务键')
    delay(1)
    device.press('recent')


def press_search(device: u2.Device):
    print('点击搜索键')
    delay(1)
    device.press('search')
