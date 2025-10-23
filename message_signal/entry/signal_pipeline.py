import sys
import traceback

import uiautomator2 as u2

from message_signal.bean.SignalBean import SignalBean
from message_signal.config.global_config_sig import SIGNAL_PERMISSIONS
from message_signal.helper.add_friend_helper import add_friend_signal
from message_signal.helper.chat_helper import chat_signal
from message_signal.helper.login_helper import login_signal
from utils.uiautomator2.connect import connect_device, prepare_login

import logging

logging.basicConfig(level=logging.DEBUG)


def start_chat_pair_signal(user_in: SignalBean, user_out: SignalBean):
    try:
        print('发送消息 start+++')
        # 连接设备
        in_device: u2.Device = connect_device(user_in.device_id)
        out_device: u2.Device = connect_device(user_out.device_id)
        print('---------------------------------------------登录:开始------------------------------------------------')
        # 登录准备
        prepare_login(in_device, user_in, SIGNAL_PERMISSIONS)
        prepare_login(out_device, user_out, SIGNAL_PERMISSIONS)
        # 登录
        login_signal(in_device, user_in)
        login_signal(out_device, user_out)
        print('---------------------------------------------登录:结束------------------------------------------------')
        # 添加好友
        print('-------------------------------------------添加好友:开始----------------------------------------------')
        add_friend_signal(in_device, user_in)
        add_friend_signal(out_device, user_out)
        print('-------------------------------------------添加好友:结束----------------------------------------------')
        # 发送消息
        print('-------------------------------------------发送消息:开始----------------------------------------------')
        chat_signal(in_device, out_device, user_in, user_out)
        print('-------------------------------------------发送消息:结束----------------------------------------------')
    except Exception as e:
        logging.error('发生异常', e)
        exc_type, exc_value, exc_traceback = sys.exc_info()
        print(f"异常类型: {exc_type.__name__}")
        print(f"异常信息: {exc_value}")
        print("追踪信息:")
        traceback.print_tb(exc_traceback)
