import sys

import uiautomator2 as u2

from message_signal.bean.SignalBean import SignalBean
from utils.date_time_util import delay
from utils.uiautomator2.apps import start_app, stop_app
from utils.uiautomator2.device import get_device_name
from utils.uiautomator2.input import input_text
from utils.uiautomator2.view_click import click_view_by_id, click_screen_by_x_y
from utils.uiautomator2.view_exists import exists_by_text
from utils.uiautomator2.view_get import get_view_by_id
from utils.uiautomator2.view_wait import wait_view_appear_by_text


def login_signal(device: u2.Device, user_bean: SignalBean) -> bool:
    try:
        package_name_: str = user_bean.package_name
        country_number_: str = user_bean.country_number
        phone_number_: str = user_bean.phone_number

        print(f'登录: {get_device_name(device)} {package_name_} {country_number_}-{phone_number_}')
        # 结束 app
        stop_app(device, package_name_)
        delay(1)
        # 打开 app
        start_app(device, package_name_)
        delay(3)
        # 找到手机号输入框
        country_edit_text = get_view_by_id(device, f'{package_name_}:id/country_code')
        phone_edit_text = get_view_by_id(device, f'{package_name_}:id/number')
        if country_edit_text is None or phone_edit_text is None:
            print('未找到手机号输入框')
            sys.exit(-1)
        input_text(device, country_edit_text, country_number_)
        input_text(device, phone_edit_text, phone_number_)
        # 点击箭头
        click_view_by_id(device, f'{package_name_}:id/registerButton')
        # 等待页面切换到验证码页面
        delay(10)
        wait_view_appear_by_text(device, '验证码')
        print('验证码已发送')

        # 点击自定义键盘 输入验证码
        click_screen_by_x_y(device, x=301 - 100, y=219 - 100 + 1401) // 1
        click_screen_by_x_y(device, x=301 * 2 - 100, y=219 - 100 + 1401) // 2
        click_screen_by_x_y(device, x=301 * 3 - 100, y=219 - 100 + 1401) // 3
        click_screen_by_x_y(device, x=301 - 100, y=219 * 2 - 100 + 1401) // 4
        click_screen_by_x_y(device, x=301 * 2 - 100, y=219 * 2 - 100 + 1401) // 5
        click_screen_by_x_y(device, x=301 * 3 - 100, y=219 * 2 - 100 + 1401) // 6

        delay(10)
        # 输入用户名
        user_name_edit = get_view_by_id(device, f'{package_name_}:id/name')
        input_text(device, user_name_edit, user_bean.user_name)
        # 点击完成按钮
        click_view_by_id(device, f'{package_name_}:id/finish_button')
        delay(1)

        # 登录成功
        b = exists_by_text(device, 'Signal')
        if b:
            print('登录成功')
            return True
        else:
            print('登录失败')
            sys.exit(-1)
    except Exception as e:
        print(f'登录失败: {e}')
        sys.exit(-1)
