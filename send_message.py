import sys

import uiautomator2 as u2

from message.call import call_voice, call_answer_voice, call_answer_video, call_end, call_rate_close, call_video
from message.chat_end2end import start_end2end_chat_in, start_end2end_chat_out
from message.chat_normal import start_chat
from message.chat_secure import secure_chat_on
from message.history import clear_history
from message.login import login
from message.send import send_text_message, send_image, send_video, send_file
from message.take import send_take_image, send_take_video, send_take_audio, send_take_round_video
from utils.date_time_util import delay
from utils.uiautomator2.connect import connect_device, prepare_login, prepare

PACKAGE_NAME = 'org.telegram.messenger'
PACKAGE_NAME_WEB = 'org.telegram.messenger.web'

DEVICE_ID_IN = 'RFCW8014R4E'
COUNTRY_NUMBER_IN = '852'
PHONE_NUMBER_IN = '51617407'
CHAT_USER_NAME_IN = 'Qiao LL'
ROOT_NAME_IN = 'Galaxy Z Fold5'

DEVICE_ID_OUT = 'OBTWQSGYTCCA9PT4'
COUNTRY_NUMBER_OUT = '86'
PHONE_NUMBER_OUT = '19910358658'
CHAT_USER_NAME_OUT = 'Ciii Darcy 7407'
ROOT_NAME_OUT = 'OPPO K9 Pro 5G'


def chat(in_device_: u2.Device, out_device_: u2.Device, type_: str):
    # 开启密聊
    secure_chat_on(in_device_, CHAT_USER_NAME_IN)
    # 发送 on 消息
    send_text_message(in_device_, f'OnOnOn-{type_}')
    send_text_message(out_device_, f'OnOnOn-Reply-{type_}')
    delay(3)
    # 发送文本
    send_text_message(in_device_, f'Chat Message From In-{type_}')
    send_text_message(out_device_, f'Chat Message From Out-{type_}')
    # 发送图片、视频、文件、拍照、拍摄全屏视频、拍摄圆形视频
    send_image_video_file_audio(in_device_, ROOT_NAME_IN)
    send_image_video_file_audio(out_device_, ROOT_NAME_OUT)
    # 等待消息发送完成
    print('延迟 60s 等待消息发送完成')
    delay(60)
    # 语音通话
    phone_call(in_device_, out_device_)
    phone_call(out_device_, in_device_)
    # 视频通话
    video_call(in_device_, out_device_)
    video_call(out_device_, in_device_)
    # # 关闭密聊
    # secure_chat_off(in_device_, CHAT_USER_NAME_IN)
    # # 发送 off 消息
    # send_text_message(in_device_, f'OffOffOff-{type_}')
    # send_text_message(out_device_, f'OffOffOff-Reply-{type_}')


def send_image_video_file_audio(device: u2.Device, root_name: str):
    # 发送图片
    send_image(device)
    # 发送视频
    send_video(device)
    # 发送文件
    send_file(device, root_name)
    # 发送拍照
    send_take_image(device)
    # 发送拍摄全屏视频
    send_take_video(device)
    # 发送录音
    send_take_audio(device)
    # 发送拍摄圆形视频
    send_take_round_video(device)


def video_call(from_device, to_device):
    call_video(from_device)
    call_answer_video(to_device)
    call_end(from_device)
    call_rate_close(from_device)
    call_rate_close(to_device)


def phone_call(from_device, to_device):
    call_voice(from_device)
    call_answer_voice(to_device)
    call_end(from_device)
    call_rate_close(from_device)
    call_rate_close(to_device)


if __name__ == '__main__':
    try:
        print('发送消息 start+++')
        # 连接设备
        in_device: u2.Device = connect_device(DEVICE_ID_IN)
        out_device: u2.Device = connect_device(DEVICE_ID_OUT)
        print(
            '----------------------------------------------登录:开始-------------------------------------------------')
        # 登录准备
        prepare_login(in_device, PACKAGE_NAME)
        prepare_login(out_device, PACKAGE_NAME)
        # 登录
        login(in_device, PACKAGE_NAME, PACKAGE_NAME_WEB, COUNTRY_NUMBER_IN, PHONE_NUMBER_IN)
        login(out_device, PACKAGE_NAME, PACKAGE_NAME_WEB, COUNTRY_NUMBER_OUT, PHONE_NUMBER_OUT)
        print(
            '----------------------------------------------登录:结束-------------------------------------------------')
        delay(3)
        print(
            '--------------------------------------------普通聊天:开始-----------------------------------------------')
        # 聊天准备
        prepare(in_device, PACKAGE_NAME)
        prepare(out_device, PACKAGE_NAME)
        start_chat(in_device, CHAT_USER_NAME_IN)
        start_chat(out_device, CHAT_USER_NAME_OUT)
        # 清空历史
        clear_history(in_device)
        clear_history(out_device)
        # 聊天
        chat(in_device, out_device, 'Normal')
        delay(3)
        print(
            '--------------------------------------------普通聊天:结束-----------------------------------------------')
        delay(3)
        print(
            '--------------------------------------------私密聊天:开始-----------------------------------------------')
        # 聊天准备
        prepare(in_device, PACKAGE_NAME)
        prepare(out_device, PACKAGE_NAME)
        start_chat(in_device, CHAT_USER_NAME_IN)
        start_end2end_chat_in(in_device, CHAT_USER_NAME_IN)
        start_end2end_chat_out(out_device)
        # 聊天
        chat(in_device, out_device, 'End2End')
        delay(3)
        print(
            '--------------------------------------------私密聊天:结束-----------------------------------------------')
        # 息屏
        # turn_screen_off(d)
        print('发送消息成功')
    except Exception as e:
        print(f'发送消息失败:{e}')
        sys.exit(-1)
