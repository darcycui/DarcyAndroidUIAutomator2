import uiautomator2 as u2

from utils.date_time_util import delay
from utils.uiautomator2.click_view import click_button_by_text
from utils.uiautomator2.press_key import press_back


def secret_chat_on_off(device: u2.Device):
    # 点击头像
    click_button_by_text(device, 'Ciii Home 5786')
    print('点击密聊开关')
    click_button_by_text(device, 'Secure')
    # 返回聊天页
    press_back(device)
    delay(3)
