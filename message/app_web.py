import uiautomator2 as u2
from message.dialog_list import click_dialog_list
from message.permission import grant_app_permissions
from utils.date_time_util import delay
from utils.uiautomator2.apps import start_app, stop_app
from utils.uiautomator2.press_key import press_home
from utils.uiautomator2.view_click import click_view_by_text
from utils.uiautomator2.view_exists import exists_by_text
from utils.uiautomator2.view_wait import wait_view_appear_by_text


def app_web_prepare(device: u2.Device, package_name_web_: str):
    print('准备.web app')
    # 授权所有权限
    app_web_close(device, package_name_web_)
    grant_app_permissions(device, package_name_web_)
    app_web_open(device, package_name_web_, 10)
    if exists_by_text(device, "Yes, it's me"):
        print('存在[确认是我]按钮 点击')
        click_view_by_text(device, "Yes, it's me")
    print('挨个点击聊天列表')
    click_dialog_list(device)
    # 按Home键
    press_home(device)


def app_web_open(device: u2.Device, package_name_web_: str, duration: int):
    print('打开.web app')
    # 打开.web app
    start_app(device, package_name_web_)
    # 等待连接成功
    delay(duration)
    wait_view_appear_by_text(device, 'Telegram')
    print('web.app 连接成功')

def app_web_close(device: u2.Device, package_name_web_: str):
    # 关闭.web app
    print('关闭.web app')
    stop_app(device, package_name_web_)
    delay(1)
    print('web.app 关闭成功')
