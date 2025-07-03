import sys

from message.contact import start_chat
from message.history import clear_history
from message.login import login
from message.permission import grant_app_permissions
from message.secret_chat import secret_chat_on, secret_chat_off
from message.send import send_text_message, send_image
from utils.date_time_util import delay
from utils.uiautomator2.apps import stop_app, clear_app_data, start_app
from utils.uiautomator2.connect import connect_device, prepare
from utils.uiautomator2.device import turn_screen_on
from utils.uiautomator2.press_key import press_back, press_home

PACKAGE_NAME = 'org.telegram.messenger'
PACKAGE_NAME_WEB = 'org.telegram.messenger.web'

# DEVICE_ID = 'RFCW8014R4E'
# COUNTRY_NUMBER = '852'
# PHONE_NUMBER = '51617407'
# CHAT_USER_NAME = 'Qiao LL'

DEVICE_ID = 'OBTWQSGYTCCA9PT4'
COUNTRY_NUMBER = '86'
PHONE_NUMBER = '19910358658'
CHAT_USER_NAME = 'Ciii Darcy 7407'

if __name__ == '__main__':
    try:
        print('tg send message start')
        # 连接设备
        device = connect_device(DEVICE_ID)
        # app准备
        prepare(device, PACKAGE_NAME, True)
        # 登录
        login(device, PACKAGE_NAME, PACKAGE_NAME_WEB, COUNTRY_NUMBER, PHONE_NUMBER)
        # 开始聊天
        start_chat(device, CHAT_USER_NAME)
        # 清空历史
        clear_history(device)
        # 开启密聊
        secret_chat_on(device, CHAT_USER_NAME)
        # 发送 on 消息
        send_text_message(device, 'OnOnOn')
        # 收起键盘
        press_back(device)
        delay(3)
        # 发送图片
        send_image(device)
        # 关闭密聊
        secret_chat_off(device)
        # 发送 off 消息
        send_text_message(device, 'OffOffOff')
        # 收起键盘
        press_back(device)
        delay(3)
        # 息屏
        # turn_screen_off(d)
        print('send message success')
    except Exception as e:
        print(f'send message failed:{e}')
