import time

from utils.date_time_util import delay
from utils.uiautomator2.view_get import get_view_by_text, get_view_by_id, get_view_by_description, \
    get_view_by_class_name, get_view_by_text_contains, get_view_by_text_match
from utils.uiautomator2.view_info import get_view_info
import uiautomator2 as u2


def click_view_by_text(device: u2.Device, button_text: str, position: int = 0):
    print('点击按钮:', button_text)
    delay(1)
    get_view_by_text(device, button_text, position).click()
    delay(1)


def click_view_by_text_contains(device: u2.Device, button_text: str, position: int = 0):
    print('点击按钮:', button_text)
    delay(1)
    get_view_by_text_contains(device, button_text, position).click()
    delay(1)


def click_view_by_text_match(device: u2.Device, button_text: str, position: int = 0):
    print('点击按钮:', button_text)
    delay(1)
    get_view_by_text_match(device, button_text, position).click()
    delay(1)


def click_view_by_class_name(device: u2.Device, class_name: str, position: int = 0):
    print('点击按钮:', class_name)
    delay(1)
    get_view_by_class_name(device, class_name, position).click()
    delay(1)


def click_view_by_id(device: u2.Device, button_id: str, position: int = 0):
    print('点击按钮:', button_id)
    delay(1)
    get_view_by_id(device, button_id, position).click()
    delay(1)


def click_view_by_description(device: u2.Device, description: str, position: int = 0):
    print('点击按钮:', description)
    delay(1)
    get_view_by_description(device, description, position).click()
    delay(1)


def click_view(view: u2.UiObject):
    print('点击按钮:', get_view_info(view))
    delay(1)
    view.click()
    delay(1)
