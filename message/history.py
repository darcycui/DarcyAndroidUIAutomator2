import sys

import uiautomator2 as u2

from utils.date_time_util import delay
from utils.uiautomator2.view_click import click_view_by_description, click_view_by_text, click_view_by_class_name
from utils.uiautomator2.view_exists import exists_by_id, exists_by_text


def clear_history(device: u2.Device) -> bool:
    """清空聊天记录"""
    try:
        click_view_by_description(device, 'More options')
        click_view_by_text(device, 'Clear History')
        # 同时删除对方的聊天记录
        # click_view_by_class_name(device, 'android.view.View')
        click_view_by_text(device, 'Delete')
        delay(1)
        if exists_by_text(device, 'Delete All'):
            click_view_by_text(device, 'Delete All')
            delay(1)
        print(f'清空聊天记录成功:')
        # b = exists_by_text(device, 'History cleared')
        # print(f'清空聊天记录: {b}')
        # if b:
        #     print(f'清空聊天记录成功: {b}')
        #     return True
        # else:
        #     print(f'清空聊天记录失败')
        #     sys.exit(-1)
    except Exception as e:
        print(f'清空聊天记录失败: {e}')
        sys.exit(-1)
