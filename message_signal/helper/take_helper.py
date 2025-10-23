import sys
import time

import uiautomator2 as u2

from utils.uiautomator2.view_click import click_view_by_id
from utils.uiautomator2.view_get import get_view_by_id
from utils.uiautomator2.view_long_click import long_click_by_swipe


def send_take_image_signal(device: u2.Device, package_name: str) -> bool:
    try:
        print(f'开始拍照')
        # 点击拍照按钮
        click_view_by_id(device, f'{package_name}:id/quick_camera_toggle')
        time.sleep(5)
        # 点击拍照
        click_view_by_id(device, f'{package_name}:id/shutter_button')
        time.sleep(1)
        # 点击发送
        click_view_by_id(device, f'{package_name}:id/button_toggle')
        print(f'拍照成功')
        return True
    except Exception as e:
        print(f'拍照失败 {e}')
        sys.exit(-1)


def send_take_audio_signal(device: u2.Device, package_name: str) -> bool:
    try:
        print(f'开始录音')
        # 找到录音按钮 recorder_view
        recorder_view = get_view_by_id(device, f'{package_name}:id/recorder_view')
        # 长按录音按钮
        long_click_by_swipe(device, recorder_view, 1.0)
        print(f'录音成功')
        return True
    except Exception as e:
        print(f'拍照失败 {e}')
        sys.exit(-1)
