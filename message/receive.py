import uiautomator2 as u2

from message.send import send_text_message


def receive_on_message(device: u2.Device) -> bool:
    """测试接收 on 文本消息"""
    # 回复消息
    send_text_message(device, 'OnOnOn-Reply')
    return True


def receive_off_message(device: u2.Device) -> bool:
    """测试接收 off 文本消息"""
    # 回复消息
    return send_text_message(device, 'OffOffOff-Reply')


def receive_chat_message(device: u2.Device) -> bool:
    """测试接收 chat 文本消息"""
    # 回复消息
    return send_text_message(device, 'Chat Message-Reply')
