import sys

import uiautomator2 as u2

from utils.date_time_util import delay
from utils.uiautomator2.view_get import get_view_by_text, get_view_by_id, get_view_by_description, \
    get_view_by_class_name, get_view_by_text_contains, get_view_by_text_match
from utils.uiautomator2.view_info import get_view_info, get_view_center_x, get_view_center_y


def click_view_by_text(device: u2.Device, button_text: str, position: int = 0, waite: bool = True) -> bool:
    try:
        print('点击按钮:', button_text)
        if waite:
            delay(1)
        get_view_by_text(device, button_text, position).click()
        delay(1)
        return True
    except Exception as e:
        print(f'点击按钮失败:{e}')
        sys.exit(-1)


def click_view_by_text_contains(device: u2.Device, button_text: str, position: int = 0):
    try:
        print('点击按钮:', button_text)
        delay(1)
        get_view_by_text_contains(device, button_text, position).click()
        delay(1)
        return True
    except Exception as e:
        print(f'点击按钮失败:{e}')
        sys.exit(-1)


def click_view_by_text_match(device: u2.Device, button_text: str, position: int = 0):
    try:
        print('点击按钮:', button_text)
        delay(1)
        get_view_by_text_match(device, button_text, position).click()
        delay(1)
        return True
    except Exception as e:
        print(f'点击按钮失败:{e}')
        sys.exit(-1)


def click_view_by_class_name(device: u2.Device, class_name: str, position: int = 0, waite: bool = True):
    try:
        print('点击按钮:', class_name)
        if waite:
            delay(1)
        get_view_by_class_name(device, class_name, position).click()
        delay(1)
        return True
    except Exception as e:
        print(f'点击按钮失败:{e}')
        sys.exit(-1)


def click_view_by_id(device: u2.Device, button_id: str, position: int = 0):
    try:
        print('点击按钮:', button_id)
        delay(1)
        get_view_by_id(device, button_id, position).click()
        delay(1)
        return True
    except Exception as e:
        print(f'点击按钮失败:{e}')
        sys.exit(-1)


def click_view_by_description(device: u2.Device, description: str, position: int = 0, waite: bool = True):
    try:
        print('点击按钮:', description)
        if waite:
            delay(1)
        get_view_by_description(device, description, position).click()
        delay(1)
        return True
    except Exception as e:
        print(f'点击按钮失败:{e}')
        sys.exit(-1)


def click_view(view: u2.UiObject):
    try:
        print('点击按钮:', get_view_info(view))
        delay(1)
        view.click()
        delay(1)
        return True
    except Exception as e:
        print(f'点击按钮失败:{e}')
        sys.exit(-1)


def click_view_by_x_y(device: u2.Device, x: int, y: int):
    try:
        print('点击坐标:', x, y)
        delay(1)
        device.click(x, y)
        delay(1)
        return True
    except Exception as e:
        print(f'点击坐标失败:{e}')
        sys.exit(-1)


def click_view_by_touch(device: u2.Device, view: u2.UiObject, duration=0.01):
    x = get_view_center_x(view)
    y = get_view_center_y(view)
    click_x_y(device, x, y)


def click_x_y(device: u2.Device, x: int, y: int, duration=0.01):
    print('点击坐标:', x, y)
    device.click(x, y)
    return True
