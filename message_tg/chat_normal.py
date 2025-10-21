import sys

import uiautomator2 as u2

from message_tg.bean.UserBean import UserBean
from utils.date_time_util import delay
from utils.uiautomator2.input import input_text
from utils.uiautomator2.view_click import click_view_by_text, click_view_by_class_name, click_view_by_description
from utils.uiautomator2.view_exists import exists_by_description, exists_by_text
from utils.uiautomator2.view_get import get_view_by_text


def start_chat(device: u2.Device, user_bean: UserBean) -> bool:
    try:
        contact_name: str = user_bean.chat_user_name
        # 定位左上角设置按钮
        click_view_by_description(device, 'Open navigation menu')
        delay(2)
        # 点击联系人按钮
        click_view_by_text(device, 'Contacts')
        # 如果存在联系人则直接点击
        if exists_by_text(device, contact_name):
            print(f'存在联系人:{contact_name} 直接点击')
            click_view_by_text(device, contact_name)
        else:
            # 不存在联系人 点击搜索按钮
            print(f'不存在联系人:{contact_name} 点击搜索')
            click_view_by_description(device, 'Search')
            delay(3)
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
        sys.exit(-1)
