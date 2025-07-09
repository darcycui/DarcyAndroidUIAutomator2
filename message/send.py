import uiautomator2 as u2

from utils.date_time_util import delay
from utils.uiautomator2.input import input_text
from utils.uiautomator2.swipe import swipe_up
from utils.uiautomator2.view_click import click_view_by_description, click_view_by_text, click_view_by_class_name, \
    click_view, click_view_by_text_contains
from utils.uiautomator2.view_get import get_view_by_class_name
from utils.uiautomator2.view_list_get import get_view_list_by_text


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
        # press_back(device)
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
            print('点击附件按钮')
            click_view_by_description(device, 'Attach media')
            # 向上滑动
            swipe_up(device, 0.1)
            # 点击 Gallery
            click_view_by_text(device, 'Gallery')
            # 选中 forTest
            click_view_by_description(device, '_forTestImage')  # _forTestImage
            # 选中图片 Photo. Jul 07 2025, 09:44
            print('选中图片')
            click_view_by_class_name(device, 'android.widget.Switch')
            # 点击发送按钮
            print('点击发送按钮')
            click_view_by_text(device, 'Send 1 photo')
            delay(3)
        print(f'send image success')
        return True
    except Exception as e:
        print(f'send image failed:{e}')
        pass


def send_video(device: u2.Device) -> bool:
    try:
        for i in range(1):
            print('send video')
            # 点击附件按钮
            print('点击附件按钮')
            click_view_by_description(device, 'Attach media')
            # 向上滑动
            swipe_up(device, 0.1)
            # 点击 Gallery
            click_view_by_text(device, 'Gallery')
            # 选中 forTest
            click_view_by_description(device, '_forTestVideo')  # _forTestVideo
            # 选中视频 Video, 2 seconds. Jul 07 2025, 09:44
            print('选中视频')
            click_view_by_class_name(device, 'android.widget.Switch')
            # 点击发送按钮
            print('点击发送按钮')
            click_view_by_text(device, 'Send 1 photo')
            delay(3)
        print(f'send video success')
        return True
    except Exception as e:
        print(f'send video failed:{e}')
        pass


def send_file(device: u2.Device, root_name: str) -> bool:
    try:
        for i in range(1):
            print('send file')
            # 点击附件按钮
            print('点击附件按钮')
            click_view_by_description(device, 'Attach media')
            # 点击File按钮
            print('点击File按钮')
            click_view_by_text(device, 'File')
            # 点击 Internal Storage
            click_view_by_text(device, 'Internal Storage')
            # 打开根目录
            click_view_by_description(device, '显示根目录')
            # 选中根目录
            root_items = get_view_list_by_text(device, root_name)
            click_view(root_items[len(root_items) - 1])
            # 选中 "其他"目录
            click_view_by_text(device, '其他')
            # 选中 forTest
            click_view_by_text(device, '_forTestFile')  # _forTestFile
            # 发送文件 file, 测试文档
            print('发送文件')
            click_view_by_text_contains(device, '测试文档')
            delay(3)
        print(f'send file success')
        return True
    except Exception as e:
        print(f'send file failed:{e}')
        pass
