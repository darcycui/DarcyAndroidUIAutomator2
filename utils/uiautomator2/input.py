import uiautomator2 as u2

from utils.date_time_util import delay


def input_text(device: u2.Device, view: u2.UiObject, text: str):
    print('输入文本:', text)
    delay(3)
    # 确保快速输入法已启用
    device.set_input_ime(False)
    # 发送文本
    view.send_keys(text)
    delay(3)
