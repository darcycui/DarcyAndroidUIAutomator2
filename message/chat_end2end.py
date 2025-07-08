import uiautomator2 as u2

from message.goback import go_back
from utils.date_time_util import delay
from utils.uiautomator2.press_key import press_back
from utils.uiautomator2.view_click import click_view_by_text, click_view_by_class_name, click_view_by_description
from utils.uiautomator2.view_exists import exists_by_text


def start_end2end_chat(device: u2.Device, contact_name: str) -> bool:
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
            print(f'开始End2End聊天失败-1 {contact_name}')
            raise Exception(f'开始End2End聊天失败-1 {contact_name}')
        # 点击返回箭头
        go_back(device)
        # 点击聊天列表 第一个item
        click_view_by_class_name(device, 'android.view.ViewGroup', position=0)
        # 点击头像
        click_view_by_text(device, contact_name)
        # 点击更多按钮
        click_view_by_description(device, 'More options')
        # 点击 Start-Secret-Chat
        if not exists_by_text(device, 'Start Secret Chat'):
            print(f'开始End2End聊天成功 {contact_name}')
            press_back(device)
            go_back(device)
            return True
        else:
            print(f'开始End2End聊天失败-2 {contact_name}')
            raise Exception(f'开始End2End聊天失败-2 {contact_name}')
    except Exception as e:
        print(f'开始End2End聊天失败: {e}')
        return False
