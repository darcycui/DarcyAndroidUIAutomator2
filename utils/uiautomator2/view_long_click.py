import uiautomator2 as u2

from utils.date_time_util import delay
from utils.uiautomator2.swipe import swipe_duration
from utils.uiautomator2.touch import touch_down_x_y, touch_up_x_y, touch_sleep
from utils.uiautomator2.view_get import get_view_by_text, get_view_by_id, get_view_by_description, \
    get_view_by_class_name, get_view_by_text_contains, get_view_by_text_match
from utils.uiautomator2.view_info import get_view_info, get_view_center_x, get_view_center_y


def long_click_view_by_text(device: u2.Device, button_text: str, duration: float, position: int = 0):
    print('长按按钮:', button_text)
    delay(1)
    get_view_by_text(device, button_text, position).long_click(duration=duration)
    delay(1)


def long_click_view_by_text_contains(device: u2.Device, button_text: str, duration: float, position: int = 0):
    print('长按按钮:', button_text)
    delay(1)
    get_view_by_text_contains(device, button_text, position).long_click(duration=duration)
    delay(1)


def long_click_view_by_text_match(device: u2.Device, button_text: str, duration: float, position: int = 0):
    print('长按按钮:', button_text)
    delay(1)
    get_view_by_text_match(device, button_text, position).long_click(duration=duration)
    delay(1)


def long_click_view_by_class_name(device: u2.Device, class_name: str, duration: float, position: int = 0):
    print('长按按钮:', class_name)
    delay(1)
    get_view_by_class_name(device, class_name, position).long_click(duration=duration)
    delay(1)


def long_click_view_by_id(device: u2.Device, button_id: str, duration: float, position: int = 0):
    print('长按按钮:', button_id)
    delay(1)
    get_view_by_id(device, button_id, position).long_click(duration=duration)
    delay(1)


def long_click_view_by_description(device: u2.Device, description: str, duration: float, position: int = 0):
    print('长按按钮:', description)
    delay(1)
    get_view_by_description(device, description, position).long_click(duration=duration)
    delay(1)


def long_click_view(view: u2.UiObject, duration: float):
    print('长按按钮:', get_view_info(view))
    delay(1)
    view.long_click(duration=duration)
    delay(1)


def long_click_by_touch(device: u2.Device, view: u2.UiObject, duration=3.0):
    x = get_view_center_x(view)
    y = get_view_center_y(view)
    print('长按坐标:', x, y)
    touch_down_x_y(device, x, y)
    touch_sleep(device, duration)
    touch_up_x_y(device, x, y)


def long_click_by_swipe(device: u2.Device, view: u2.UiObject, duration: float = 1.0):
    center_x = get_view_center_x(view)
    center_y = get_view_center_y(view)
    swipe_duration(device, center_x, center_y, center_x, center_y, duration)
