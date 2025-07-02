import sys
import uiautomator2 as u2
from message.permission import grant_permissions
from utils.date_time_util import delay
from utils.uiautomator2.apps import start_app, stop_app
from utils.uiautomator2.click_view import click_button_by_text, click_view_by_description
from utils.uiautomator2.get_view import get_view_by_class_name, get_view_by_text
from utils.uiautomator2.input import input_text
from utils.uiautomator2.notification import open_notification, close_notification
from utils.uiautomator2.press_key import press_home
from utils.uiautomator2.wait_view import wait_view_text_by_text


# 登录
def login(device: u2.Device, package_name_: str, package_name_web_: str, country_number_: str, phone_number_: str):
    # 授权所有权限
    grant_permissions(device, package_name_web_)
    # 打开.web app
    start_app(device, package_name_web_)
    # 等待连接成功
    get_view_by_text(device, 'Telegram').wait()
    # 按
    press_home(device)
    # 打开 app
    start_app(device, package_name_)

    # 点击开始按钮
    click_button_by_text(device, 'Start Messaging')
    delay(3)
    # 找到手机号输入框
    phone_edit_text_list = get_view_by_class_name(device, 'android.widget.EditText')
    if len(phone_edit_text_list) < 2:
        print('未找到手机号输入框')
        sys.exit(-1)
    input_text(device, phone_edit_text_list[0], country_number_)
    input_text(device, phone_edit_text_list[1], phone_number_)
    # 点击箭头
    click_view_by_description(device, 'Done')
    # 点击Yes
    click_button_by_text(device, 'Yes')
    # 等待页面切换到验证码页面
    get_view_by_text(device, 'Check your Telegram messages').wait()
    delay(3)
    # 打开.web app
    start_app(device, package_name_web_)
    # 等待连接成功
    get_view_by_text(device, 'Telegram').wait()
    delay(3)
    # 打开 app
    start_app(device, package_name_)

    # 打开通知栏
    open_notification(device)
    # wait_view_appear_by_id(device, 'com.android.systemui:id/verification_code')
    verify_code_message = wait_view_text_by_text(device, 'Login code:', 120)
    # verify_code_message = wait_view_text_by_id(device, 'android:id/message_text', 120)
    # verify_code_message = wait_view_text_by_id(device, 'com.android.systemui:id/notification_text', 120)
    if verify_code_message is None:
        print('未找到验证码')
        sys.exit(-1)
    verify_code_numbers = verify_code_message[12:17]
    print('找到验证码-->', verify_code_numbers)
    # 关闭通知栏
    close_notification(device)
    # # 打开 app
    # start_app(device, package_name)

    # 找到验证码输入框
    code_edit_text_list = get_view_by_class_name(device, 'android.widget.EditText')
    print('输入框个数-->', len(code_edit_text_list), '验证码位数-->', len(verify_code_numbers))
    if len(code_edit_text_list) <= 0 or len(code_edit_text_list) != len(verify_code_numbers):
        print('输入框个数与验证码位数不一致')

    for i, item in enumerate(verify_code_numbers):
        input_text(device, code_edit_text_list[i], item)
    # 点击OK 二次密码提示
    click_button_by_text(device, 'OK')
    # # 点击 Continue
    # click_button_by_text(device, 'Continue')
    # # 允许通知
    # click_button_by_text(device, '允许')
    # 登录成功
    # 关闭.web app
    stop_app(device, package_name_web_)
