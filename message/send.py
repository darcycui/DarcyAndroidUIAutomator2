from utils.uiautomator2.press_key import press_back
from utils.uiautomator2.view_click import click_view_by_description
from utils.uiautomator2.view_get import get_view_by_class_name, get_view_by_description
from utils.date_time_util import get_current_time, delay
from utils.uiautomator2.input import input_text
import uiautomator2 as u2


def send_text_message(device: u2.Device, message_text: str) -> bool:
    try:
        # 循环3次
        for i in range(1):
            # 输入文本
            view = get_view_by_class_name(device, 'android.widget.EditText')
            input_text(device, view, message_text)
            # 点击发送按钮
            click_view_by_description(device, 'Send')
            delay(2)
        # 收起键盘
        press_back(device)
        delay(3)
        print(f'send text message success:{message_text}')
        return True
    except Exception as e:
        print(f'send text message failed:{e}')
        return False


def send_image(device: u2.Device) -> bool:
    try:
        for i in range(1):
            print('send image')
            # 点击附件按钮
            views = get_view_by_class_name(device, 'android.widget.ImageView')
            print('点击附件按钮')
            views[len(views) - 1].click()
            delay(3)
            # 选中图片
            views = get_view_by_class_name(device, 'android.widget.Switch')
            print('选中图片')
            views[i].click()
            delay(1)
            # 点击发送按钮
            views = get_view_by_class_name(device, 'android.widget.ImageView')
            print('点击发送按钮')
            print(views)
            views[len(views) - 1].click()
            delay(3)
        print(f'send image success')
        return True
    except Exception as e:
        print(f'send image failed:{e}')
        pass
