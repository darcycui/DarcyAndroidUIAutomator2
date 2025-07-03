import sys

import uiautomator2 as u2

from utils.date_time_util import delay
from utils.uiautomator2.view_click import click_view_by_text, click_view_by_class_name, click_view_by_description
from utils.uiautomator2.view_exists import exists_by_description
from utils.uiautomator2.view_get import get_view_by_text
from utils.uiautomator2.input import input_text
from utils.uiautomator2.press_key import press_menu, press_search
from utils.uiautomator2.view_wait import wait_view_text_by_text


def start_chat(device: u2.Device, contact_name: str) -> bool:
    try:
        # 定位左上角设置按钮
        press_menu(device)
        # 点击联系人按钮
        click_view_by_text(device, 'Contacts')
        # 点击搜索按钮
        press_search(device)
        click_view_by_description(device, 'Search')
        # 输入文本
        search_view = get_view_by_text(device, 'Search')
        input_text(device, search_view, contact_name)
        # 点击联系人 开始聊天
        click_view_by_class_name(device, 'android.widget.Switch')
        delay(3)
        b = exists_by_description(device, 'Call')
        if b:
            print(f'开始聊天成功: {b}')
            return True
        else:
            raise Exception(f'开始聊天失败 {contact_name}')
    except Exception as e:
        print(f'开始聊天失败: {e}')
        return False
