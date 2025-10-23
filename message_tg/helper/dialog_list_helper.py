import sys

import uiautomator2 as u2

from message_tg.helper.goback_helper import go_back
from utils.date_time_util import delay
from utils.uiautomator2.view_click import click_view
from utils.uiautomator2.view_get import get_view_by_class_name
from utils.uiautomator2.view_list_get import get_child_view_list_by_class_name


def click_dialog_list(device: u2.Device, position: int = -1) -> bool:
    """
    点击对话列表全部
    """
    try:
        recycler_view = get_view_by_class_name(device, 'androidx.recyclerview.widget.RecyclerView')
        dialogs = get_child_view_list_by_class_name(recycler_view, 'android.view.ViewGroup')
        for item in dialogs:
            click_dialog_item(item)
            go_back(device)
        print('点击对话列表成功')
        return True
    except Exception as e:
        print(f'点击对话列表失败:{e}')
        sys.exit(-1)

def click_dialog_list_with_position(device: u2.Device, position: int) -> bool:
    """
    点击对话列表指定位置
    """
    try:
        recycler_view = get_view_by_class_name(device, 'androidx.recyclerview.widget.RecyclerView')
        dialogs = get_child_view_list_by_class_name(recycler_view, 'android.view.ViewGroup')
        item = dialogs[position]
        click_dialog_item(item)
        print(f'点击对话列表 position:{position} 成功')
        return True
    except Exception as e:
        print(f'点击对话列表 position:{position} 失败:{e}')
        sys.exit(-1)


def click_dialog_item(item: u2.UiObject) -> bool:
    """
    点击列表 item
    """
    try:
        click_view(item)
        delay(3)
        print('点击列表 item 成功')
        return True
    except Exception as e:
        print(f'点击列表 item 失败:{e}')
        sys.exit(-1)
