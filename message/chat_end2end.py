import sys

import uiautomator2 as u2

from message.dialog_list import click_dialog_list_with_position
from message.goback import go_back
from utils.date_time_util import delay
from utils.uiautomator2.view_click import click_view_by_text, click_view_by_description
from utils.uiautomator2.view_exists import exists_by_text, exists_by_text_contains


def start_end2end_chat_in(device: u2.Device, contact_name: str) -> bool:
    try:
        # 点击头像
        click_view_by_text(device, contact_name)
        # 点击更多按钮
        click_view_by_description(device, 'More options')
        delay(2)
        # 点击 Start-Secret-Chat
        if exists_by_text(device, 'Start Secret Chat'):
            click_view_by_text(device, 'Start Secret Chat')
            # 点击 Start
            click_view_by_text(device, 'Start')
            delay(3)
        else:
            print(f'in: 开始End2End聊天失败-1 {contact_name}')
            raise Exception(f'in: 开始End2End聊天失败-1 {contact_name}')
        # 点击返回箭头
        go_back(device)
        # 点击聊天列表 第一个item
        click_dialog_list_with_position(device, 0)

        if exists_by_text_contains(device, f'Secret chats:'):
            print(f'in: 开始End2End聊天成功 {contact_name}')
            return True
        else:
            print(f'in: 开始End2End聊天失败-2 {contact_name}')
            raise Exception(f'in: 开始End2End聊天失败-2 {contact_name}')
    except Exception as e:
        print(f'in: 开始End2End聊天失败: {e}')
        sys.exit(-1)

def start_end2end_chat_out(device: u2.Device) -> bool:
    try:
        click_dialog_list_with_position(device, 0)
        if exists_by_text_contains(device, 'Secret chats:'):
            print(f'out: 开始End2End聊天成功')
            return True
        else:
            print(f'out: 开始End2End聊天失败')
            raise Exception(f'out: 开始End2End聊天失败')
    except Exception as e:
        print(f'out: 开始End2End聊天失败: {e}')
        sys.exit(-1)
