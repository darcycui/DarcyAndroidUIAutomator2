import time

from utils.date_time_util import delay
from utils.uiautomator2.get_view import get_view_by_text, get_view_by_id, get_view_by_description, \
    get_view_by_class_name
from utils.uiautomator2.view_info import get_view_info
import uiautomator2 as u2


def click_button_by_text(device: u2.Device, button_text: str):
    print('点击按钮:', button_text)
    delay(3)
    get_view_by_text(device, button_text).click()


def click_button_by_class_name(device: u2.Device, class_name: str):
    print('点击按钮:', class_name)
    delay(3)
    get_view_by_class_name(device, class_name).click()


def click_button_by_id(device: u2.Device, button_id: str):
    print('点击按钮:', button_id)
    delay(3)
    get_view_by_id(device, button_id).click()


def click_view_by_description(device: u2.Device, description: str):
    print('点击按钮:', description)
    get_view_by_description(device, description).click()
    delay(3)


def click_view(view: u2.UiObject):
    print('点击按钮:', get_view_info(view))
    view.click()
    delay(3)
