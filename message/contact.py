import uiautomator2 as u2

from utils.uiautomator2.click_view import click_button_by_text, click_button_by_class_name
from utils.uiautomator2.get_view import get_view_by_text
from utils.uiautomator2.input import input_text
from utils.uiautomator2.press_key import press_menu, press_search


def start_chat(device: u2.Device, contact_name: str):
    # 定位左上角设置按钮
    press_menu(device)
    # 点击联系人按钮
    click_button_by_text(device, 'Contacts')
    # 点击搜索按钮
    press_search(device)
    click_button_by_class_name(device, 'android.widget.ImageButton')
    # 输入文本
    search_view = get_view_by_text(device, 'Search')
    input_text(device, search_view, contact_name)
    # 点击联系人 开始聊天
    click_button_by_class_name(device, 'android.widget.Switch')
