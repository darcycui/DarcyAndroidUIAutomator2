from message.send import send_text_message
from utils.uiautomator2.view_wait import wait_view_text_by_text_contains
import uiautomator2 as u2


def receive_on_message(device: u2.Device) -> bool:
    """测试接收 on 文本消息"""
    received_message: str | None = wait_view_text_by_text_contains(device, 'OnOnOn', 120)
    if received_message:
        print(f'接收到 on 消息：{received_message}')
        # 回复消息
        send_text_message(device, 'OnOnOn-Reply')
        return True
    else:
        print('没有接收到 on 消息')
        return False

def receive_off_message(device: u2.Device) -> bool:
    """测试接收 off 文本消息"""
    received_message: str | None = wait_view_text_by_text_contains(device, 'OffOffOff', 120)
    if received_message:
        print(f'接收到 off 消息：{received_message}')
        # 回复消息
        return send_text_message(device, 'OffOffOff-Reply')
    else:
        print('没有接收到 off 消息')
        return False
