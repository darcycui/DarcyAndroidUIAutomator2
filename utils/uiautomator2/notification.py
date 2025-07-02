import uiautomator2 as u2

from utils.date_time_util import delay
from utils.uiautomator2.press_key import press_back


def open_notification(device: u2.Device):
    print('打开通知栏')
    delay(1)
    device.open_notification()


def close_notification(device: u2.Device):
    print('关闭通知栏')
    delay(1)
    press_back(device)
