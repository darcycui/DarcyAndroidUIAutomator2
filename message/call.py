import sys

import uiautomator2 as u2

from utils.date_time_util import delay
from utils.uiautomator2.press_key import press_back
from utils.uiautomator2.view_click import click_view_by_description, click_view_by_text, click_view_by_class_name, \
    click_view, click_x_y
from utils.uiautomator2.view_exists import exists_by_text, exists_by_description
from utils.uiautomator2.view_get import get_view_by_text
from utils.uiautomator2.view_get_relative import get_view_up_by_class_name
from utils.uiautomator2.view_wait import wait_view_appear_by_text, wait_view_gone_by_text, \
    wait_view_appear_by_class_name


def call_voice(device: u2.Device) -> bool:
    print('拨打语音电话 start+++')
    click_view_by_description(device, 'Call')
    b = wait_view_appear_by_text(device, 'End Call')
    if not b:
        print('End Call 按钮未出现')
        sys.exit(-1)
    print('点击 静音 按钮')
    bb = click_view_by_class_name(device, 'android.view.View', 5, waite=False)
    if bb:
        print('拨打语音电话成功')
    else:
        print('拨打语音电话失败')
    return bb


def call_video(device: u2.Device) -> bool:
    print('拨打视频电话 start+++')
    click_view_by_description(device, 'More options')
    click_view_by_text(device, 'Video Call')
    b = wait_view_appear_by_text(device, 'End Call')
    if not b:
        print('End Call 按钮未出现')
        sys.exit(-1)
    print('点击 静音 按钮')
    bb = click_view_by_class_name(device, 'android.view.View', 10, waite=False)
    if bb:
        print('拨打视频电话成功')
    else:
        print('拨打视频电话失败')
    return bb


def call_end(device: u2.Device, wait_time: int = 10) -> bool:
    print('结束通话 start+++')
    print(f'等待 {wait_time}s 结束通话')
    delay(wait_time)
    if exists_by_text(device, 'End Call'):
        b = click_view_by_text(device, 'End Call', waite=False)
        if not b:
            print('End Call 按钮点击失败')
            sys.exit(-1)
    else:
        click_x_y(device, 500, 500)
        delay(0.5)
        b = click_view_by_text(device, 'End Call', waite=False)
        if not b:
            print('End Call 按钮点击失败')
            sys.exit(-1)
    bb = wait_view_gone_by_text(device, 'microphone is off')
    if bb:
        print('结束通话成功')
    else:
        print('结束通话失败')
    return bb


def call_answer_voice(device: u2.Device) -> bool:
    print('接听 start+++')
    appear = wait_view_appear_by_text(device, '接听')
    if not appear:
        print('接听 按钮未出现')
        sys.exit(-1)
    # 授予必要权限
    # device.shell("pm grant com.android.systemui android.permission.INJECT_EVENTS")
    answer_view = device(text="接听")
    click_view(answer_view)
    delay(2)
    b = wait_view_appear_by_text(device, 'End Call')
    if not b:
        print('End Call 按钮未出现')
        sys.exit(-1)
    print('点击 静音 按钮')
    bb = click_view_by_description(device, 'Mute', waite=False)
    if bb:
        print('接听成功')
    else:
        print('接听失败')
    return bb


def call_answer_video(device: u2.Device) -> bool:
    print('接听 start+++')
    appear = wait_view_appear_by_text(device, '接听')
    if not appear:
        print('接听 按钮未出现')
        sys.exit(-1)
    # 授予必要权限
    # device.shell("pm grant com.android.systemui android.permission.INJECT_EVENTS")
    answer_view = device(text="接听")
    click_view(answer_view)
    b = wait_view_appear_by_text(device, 'End Call')
    if not b:
        print('End Call 按钮未出现')
        sys.exit(-1)
    print('点击 静音 按钮')
    bb = click_view_by_description(device, 'Mute', waite=False)
    if bb:
        print('接听成功')
    else:
        print('接听失败')
    return bb


def call_rate_close(device: u2.Device) -> bool:
    print('关闭评分 start+++')
    delay(2)
    if exists_by_text(device, 'Rate this call'):
        print('存在 Rate this call 关闭它')
        press_back(device)
    print('不存在 Rate this call 无需关闭')
    return True
