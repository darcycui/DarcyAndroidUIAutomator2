import sys
import time

import uiautomator2 as u2

from utils.date_time_util import delay
from utils.uiautomator2.swipe import swip_from_view_up
from utils.uiautomator2.view_click import click_view_by_id, click_screen_by_x_y
from utils.uiautomator2.view_get import get_view_by_id
from utils.uiautomator2.view_wait import wait_view_appear_by_view_id, wait_view_gone_by_view_id


def call_signal(device: u2.Device, package_name: str) -> bool:
    try:
        print(f'开始拨打电话')
        # 点击电话按钮
        click_view_by_id(device, f'{package_name}:id/menu_call_secure')
        # 等待"响铃中"出现
        b = wait_view_appear_by_view_id(device, f'{package_name}:id/callStateLabel')
        if b:
            print(f'拨打电话成功')
            # 点击静音按钮
            click_view_by_id(device, f'{package_name}:id/muteButton')
            return True
        else:
            print(f'拨打电话失败')
            sys.exit(-1)
    except Exception as e:
        print(f'拨打电话失败: {e}')
        sys.exit(-1)


def call_answer_signal(device: u2.Device, package_name: str) -> bool:
    try:
        print(f'开始接听电话')
        # 等待"接听"出现
        appear_answer = wait_view_appear_by_view_id(device, f'{package_name}:id/swipe_up_text')
        if not appear_answer:
            print(f'接听 按钮未出现')
            sys.exit(-1)
        # 向上滑动接听按钮
        answer_view = get_view_by_id(device, f'{package_name}:id/answer')
        # 向上滑动接听按钮(多次尝试)
        for _ in range(3):
            try:
                swip_from_view_up(device, answer_view, length_px=500, duration=0.1)
            except Exception as e:
                print(f"滚动尝试失败: {e}")
                time.sleep(0.5)  # 等待后重试
        # 等待"挂断"出现
        appear_finish = wait_view_appear_by_view_id(device, f'{package_name}:id/hangup_fab')
        if not appear_finish:
            print(f'挂断 按钮未出现')
            sys.exit(-1)
        # 点击静音按钮
        click_view_by_id(device, f'{package_name}:id/muteButton')
        print(f'接听电话成功')
        return True
    except Exception as e:
        print(f'接听电话失败: {e}')
        sys.exit(-1)


def start_video_call_signal(device: u2.Device, package_name: str) -> bool:
    try:
        print(f'开启视频')
        # 点击一下屏幕中央
        click_screen_by_x_y(device, device.window_size()[0] / 2, device.window_size()[1] / 2)
        time.sleep(0.5)
        # 点击开启视频按钮
        click_view_by_id(device, f'{package_name}:id/video_mute_button')
        # 等待"切换摄像头"按钮出现
        b = wait_view_appear_by_view_id(device, f'{package_name}:id/camera_flip_button')
        if b:
            print(f'开启视频成功')
            return True
        else:
            print(f'开启视频失败')
            sys.exit(-1)
    except Exception as e:
        print(f'开启视频失败: {e}')
        sys.exit(-1)


def call_end_signal(device: u2.Device, package_name: str) -> bool:
    try:
        print(f'挂断电话')
        # 点击一下屏幕中央
        click_screen_by_x_y(device, device.window_size()[0] / 2, device.window_size()[1] / 2)
        time.sleep(0.5)
        # 点击挂断电话按钮
        click_view_by_id(device, f'{package_name}:id/hangup_fab')
        # 等待"挂断电话"按钮消失
        b = wait_view_gone_by_view_id(device, f'{package_name}:id/hangup_fab')
        if b:
            print(f'挂断电话成功')
            return True
        else:
            print(f'挂断电话失败')
            sys.exit(-1)
    except Exception as e:
        print(f'挂断电话失败: {e}')
        sys.exit(-1)
