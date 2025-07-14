import sys

import uiautomator2 as u2

from utils.date_time_util import delay
from utils.uiautomator2.view_click import click_view_by_description, click_view
from utils.uiautomator2.view_exists import exists_by_description
from utils.uiautomator2.view_get import get_view_by_description
from utils.uiautomator2.view_get_relative import get_view_down_by_class_name
from utils.uiautomator2.view_long_click import long_click_view_by_description, long_click_by_swipe


def send_take_image(device: u2.Device):
    try:
        for i in range(1):
            print('take image')
            # 点击附件按钮
            print('点击附件按钮')
            click_view_by_description(device, 'Attach media')
            delay(3)
            # 点击拍摄按钮
            print('点击拍摄按钮')
            top_view = get_view_by_description(device, 'Instant camera')
            camera_view = get_view_down_by_class_name(top_view,'android.widget.FrameLayout')
            print(f'camera_view type: {type(camera_view)}')
            click_view(camera_view)
            # 点击切换摄像头按钮
            click_view_by_description(device, 'Switch camera')
            # 点击拍照按钮
            print('点击拍照按钮')
            click_view_by_description(device, 'Shutter')
            # 点击发送按钮
            print('点击发送按钮')
            click_view_by_description(device, 'Send')
            delay(3)
        print(f'take image success')
        return True
    except Exception as e:
        print(f'take image failed:{e}')
        sys.exit(-1)


def send_take_video(device: u2.Device):
    try:
        for i in range(1):
            print('take video')
            # 点击附件按钮
            print('点击附件按钮')
            click_view_by_description(device, 'Attach media')
            delay(3)
            # 点击拍摄按钮
            print('点击拍摄按钮')
            # 获取拍摄按钮 使用相对关系定位 view
            top_view = get_view_by_description(device, 'Instant camera')
            camera_view = get_view_down_by_class_name(top_view, 'android.widget.FrameLayout')
            print(f'camera_view type: {type(camera_view)}')
            click_view(camera_view)
            # 点击切换摄像头按钮
            click_view_by_description(device, 'Switch camera')
            # 长按录制按钮
            print('长按录制按钮')
            long_click_view_by_description(device, 'Shutter', 3.5)
            # 点击发送按钮
            print('点击发送按钮')
            click_view_by_description(device, 'Send')
            delay(3)
        print(f'take video success')
        return True
    except Exception as e:
        print(f'take video failed:{e}')
        sys.exit(-1)

def send_take_audio(device: u2.Device):
    try:
        for i in range(1):
            print('take audio')
            # 切换到录音
            if not exists_by_description(device, 'Record voice message'):
                click_view_by_description(device,'Record video message')
            # 长按录音按钮
            print('长按录音按钮')
            # long_click_view_by_description(device, 'Record voice message', 3.0)
            # long_click_by_touch(device, get_view_by_description(device, 'Record voice message'), 3.0)
            long_click_by_swipe(device, get_view_by_description(device, 'Record voice message'), 1.0)
            delay(3)
        print(f'take audio success')
        return True
    except Exception as e:
        print(f'take audio failed:{e}')
        sys.exit(-1)

def send_take_round_video(device: u2.Device):
    try:
        for i in range(1):
            print('take round video')
            # 切换到录音
            if not exists_by_description(device, 'Record video message'):
                click_view_by_description(device,'Record voice message')
            # 长按录像按钮
            print('长按录像按钮')
            # long_click_view_by_description(device, 'Record video message', 3.5)
            # long_click_by_touch(device, get_view_by_description(device, 'Record voice message'), 3.0)
            long_click_by_swipe(device, get_view_by_description(device, 'Record video message'), 1.0)
            delay(3)
        print(f'take round video success')
        return True
    except Exception as e:
        print(f'take round video failed:{e}')
        sys.exit(-1)