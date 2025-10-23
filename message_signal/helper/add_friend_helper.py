import sys

import uiautomator2 as u2

from message_signal.bean import SignalBean
from utils.uiautomator2.input import input_text
from utils.uiautomator2.view_click import click_view_by_id
from utils.uiautomator2.view_exists import exists_by_text, exists_by_id
from utils.uiautomator2.view_get import get_view_by_id


def add_friend_signal(device: u2.Device, user_bean: SignalBean) -> bool:
    try:
        package_name: str = user_bean.package_name
        chat_user_name: str = user_bean.chat_user_name
        # 点击添加按钮
        click_view_by_id(device, f'{package_name}:id/fab')
        # 输入用户名
        name_edit_view = get_view_by_id(device, f'{package_name}:id/search_view')
        input_text(device, name_edit_view, chat_user_name)
        # 点击第一条item
        click_view_by_id(device, f'{package_name}:id/name')
        if exists_by_id(device, f'{package_name}:id/menu_call_secure'):
            print('添加好友成功')
            return True
        else:
            print('添加好友失败')
            sys.exit(-1)
    except Exception as e:
        print(f'添加好友失败: {e}')
        sys.exit(-1)
