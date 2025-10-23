import time

import uiautomator2 as u2

from message_signal.bean import SignalBean
from message_signal.helper.call_helper import call_signal, call_answer_signal, start_video_call_signal, call_end_signal
from message_signal.helper.send_helper import send_text_signal, send_image_signal, send_video_signal, send_file_signal
from message_signal.helper.take_helper import send_take_image_signal, send_take_audio_signal


def chat_signal(device_in: u2.Device, device_out: u2.Device, user_in: SignalBean, user_out: SignalBean) -> bool:
    try:
        package_name: str = user_in.package_name
        # # 文本消息
        # send_text_signal(device_in, package_name, 'OnOnOn-1')
        # send_text_signal(device_out, package_name, 'Come on baby-1.')
        # # 发送消息 in-->out
        # chat_once(device_in, device_out, user_in)

        send_text_signal(device_out, package_name, 'OnOnOn-2')
        send_text_signal(device_in, package_name, 'Come on baby-2.')
        # 发送消息 out->in
        chat_once(device_out, device_in, user_out)
        return True
    except Exception as e:
        print(f'聊天失败: {e}')
        return False


def chat_once(device_from: u2.Device, device_to: u2.Device, user: SignalBean):
    package_name: str = user.package_name
    root_name = user.root_name
    # 图片
    send_image_signal(device_from, package_name, root_name)
    # 视频
    send_video_signal(device_from, package_name, root_name)
    # 文件
    send_file_signal(device_from, package_name, root_name)
    # 拍照
    send_take_image_signal(device_from, package_name)
    # 录音
    send_take_audio_signal(device_from, package_name)
    # 拨打电话
    call_signal(device_from, package_name)
    call_answer_signal(device_to, package_name)
    time.sleep(3)
    start_video_call_signal(device_from, package_name)
    start_video_call_signal(device_to, package_name)
    time.sleep(5)
    call_end_signal(device_from, package_name)
