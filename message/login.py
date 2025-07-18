import sys

import uiautomator2 as u2

from message.app_web import app_web_prepare, app_web_open, app_web_close
from utils.date_time_util import delay
from utils.uiautomator2.apps import start_app, stop_app
from utils.uiautomator2.device import get_device_name
from utils.uiautomator2.input import input_text
from utils.uiautomator2.notification import open_notification, close_notification
from utils.uiautomator2.view_click import click_view_by_text, click_view_by_description
from utils.uiautomator2.view_exists import exists_by_text, exists_by_description
from utils.uiautomator2.view_get import get_view_by_class_name, get_view_by_text_contains
from utils.uiautomator2.view_info import get_view_text
from utils.uiautomator2.view_list_get import get_view_list_by_class_name
from utils.uiautomator2.view_wait import wait_view_appear_by_text, wait_view_appear_by_text


# 登录
def login(
        device: u2.Device,
        package_name_: str,
        package_name_web_: str,
        package_name_beta_: str,
        country_number_: str,
        phone_number_: str
) -> bool:
    try:
        print(f'登录: {get_device_name(device)} {package_name_} {country_number_}-{phone_number_}')
        # 停止 app beta
        stop_app(device, package_name_beta_)
        # 打开 app
        start_app(device, package_name_)
        # 准备app web
        app_web_prepare(device, package_name_web_)
        # 打开 app
        start_app(device, package_name_)
        # 点击开始按钮
        click_view_by_text(device, 'Start Messaging')
        delay(3)
        # 找到手机号输入框
        country_edit_text = get_view_by_class_name(device, 'android.widget.EditText', position=0)
        phone_edit_text = get_view_by_class_name(device, 'android.widget.EditText', position=1)
        if country_edit_text is None or phone_edit_text is None:
            print('未找到手机号输入框')
            sys.exit(-1)
        input_text(device, country_edit_text, country_number_)
        input_text(device, phone_edit_text, phone_number_)
        # 点击箭头
        click_view_by_description(device, 'Done')
        # 点击Yes
        click_view_by_text(device, 'Yes')
        # 等待页面切换到验证码页面
        delay(10)
        wait_view_appear_by_text(device, 'Check your Telegram messages')
        print('验证码已发送')
        delay(3)
        # 打开.web app
        app_web_open(device, package_name_web_, 5)
        delay(3)
        # 打开 app
        start_app(device, package_name_)

        # 打开通知栏
        open_notification(device)
        verify_code_exist: bool = wait_view_appear_by_text(device, 'Login code:', 120)
        if not verify_code_exist:
            print('未找到验证码')
            sys.exit(-1)
        verify_code_view: u2.UiObject = get_view_by_text_contains(device, 'Login code:')
        verify_code_message: str = get_view_text(verify_code_view)
        verify_code_numbers = verify_code_message[12:17]
        print('找到验证码-->', verify_code_numbers)
        # 关闭通知栏
        close_notification(device)
        # # 打开 app
        # start_app(device, package_name)

        # 找到验证码输入框
        code_edit_text_list = get_view_list_by_class_name(device, 'android.widget.EditText')
        print('输入框个数-->', len(code_edit_text_list), '验证码位数-->', len(verify_code_numbers))
        if len(code_edit_text_list) <= 0 or len(code_edit_text_list) != len(verify_code_numbers):
            print('输入框个数与验证码位数不一致')
        for i, item in enumerate(verify_code_numbers):
            input_text(device, code_edit_text_list[i], item)

        delay(3)
        # 点击OK 二次密码提示
        if exists_by_text(device, 'OK'):
            click_view_by_text(device, 'OK')
        # # 点击 Continue
        # click_button_by_text(device, 'Continue')
        # # 允许通知
        # click_button_by_text(device, '允许')
        # 登录成功
        # 关闭.web app
        app_web_close(device, package_name_web_)
        b = exists_by_description(device, 'Search')
        if b:
            print('登录成功')
            return True
        else:
            print('登录失败')
            sys.exit(-1)
    except Exception as e:
        print(f'登录失败: {e}')
        sys.exit(-1)
