import sys

import uiautomator2 as u2

from message.goback import go_back
from utils.date_time_util import delay
from utils.uiautomator2.view_click import click_view_by_text
from utils.uiautomator2.view_get import get_view_by_class_name
from utils.uiautomator2.view_info import is_view_checked


def secure_chat_on(device: u2.Device, contact_name: str) -> bool:
    # 点击头像
    click_view_by_text(device, contact_name)
    delay(3)
    switch_view = get_view_by_class_name(device, 'android.widget.Switch', 3)
    if is_view_checked(switch_view):
        print('密聊已开启,无需点击')
        go_back(device)
        return True
    print('点击密聊开关')
    click_view_by_text(device, 'Secure')
    delay(2)
    if is_view_checked(switch_view):
        go_back(device)
        print('密聊开启成功')
        return True
    else:
        go_back(device)
        print('密聊开启失败')
        sys.exit(-1)


def secure_chat_off(device: u2.Device, contact_name: str) -> bool:
    # 点击头像
    click_view_by_text(device, contact_name)
    delay(3)
    switch_view = get_view_by_class_name(device, 'android.widget.Switch', 3)
    if not is_view_checked(switch_view):
        print('密聊已关闭,无需点击')
        go_back(device)
        return True
    print('点击密聊开关')
    click_view_by_text(device, 'Secure')
    if not is_view_checked(switch_view):
        go_back(device)
        print('密聊关闭成功')
        return True
    else:
        go_back(device)
        print('密聊关闭失败')
        sys.exit(-1)


