import sys
import time

import uiautomator2 as u2
from utils.uiautomator2.input import input_text
from utils.uiautomator2.view_click import click_view_by_id, click_view_by_description, click_view, click_view_by_text, \
    click_view_by_text_contains
from utils.uiautomator2.view_get import get_view_by_id
from utils.uiautomator2.view_list_get import get_view_list_by_text


def send_text_signal(device: u2.Device, package_name: str, message_text: str) -> bool:
    try:
        print(f'开始发送文本消息:{message_text}')
        # 找到输入框
        text_edit_view = get_view_by_id(device, f'{package_name}:id/embedded_text_editor')
        # 输入文本
        input_text(device, text_edit_view, message_text)
        # 点击发送按钮
        click_view_by_id(device, f'{package_name}:id/button_toggle')
        print(f'发送文本消息成功')
        time.sleep(3)
        return True
    except Exception as e:
        print(f'发送文本消息失败 {e}')
        sys.exit(-1)


def send_image_signal(device: u2.Device, package_name: str, root_name: str) -> bool:
    try:
        print(f'开始发送图片消息')
        # 点击附件按钮
        click_view_by_id(device, f'{package_name}:id/button_toggle')
        # 点击图片选择按钮
        click_view_by_id(device, f'{package_name}:id/gallery_button')
        # 打开根目录
        click_view_by_description(device, '显示根目录')
        # 选中根目录
        root_items = get_view_list_by_text(device, root_name)
        click_view(root_items[len(root_items) - 1])
        # 选中 "其他"目录
        click_view_by_text(device, '其他')
        # 选中 forTest
        click_view_by_text(device, '_forTestImage')  # _forTestFile
        # 选择图片
        click_view_by_text_contains(device, f'image_')
        # 点击发送按钮
        click_view_by_id(device, f'{package_name}:id/button_toggle')
        time.sleep(3)
        print(f'发送图片成功')
        return True
    except Exception as e:
        print(f'发送图片失败 {e}')
        sys.exit(-1)

def send_video_signal(device: u2.Device, package_name: str, root_name: str) -> bool:
    try:
        print(f'开始发送视频消息')
        # 点击附件按钮
        click_view_by_id(device, f'{package_name}:id/button_toggle')
        # 点击视频选择按钮
        click_view_by_id(device, f'{package_name}:id/gallery_button')
        # 打开根目录
        click_view_by_description(device, '显示根目录')
        # 选中根目录
        root_items = get_view_list_by_text(device, root_name)
        click_view(root_items[len(root_items) - 1])
        # 选中 "其他"目录
        click_view_by_text(device, '其他')
        # 选中 forTest
        click_view_by_text(device, '_forTestVideo')  # _forTestFile
        # 选择视频
        click_view_by_text_contains(device, f'video_')
        # 点击发送按钮
        click_view_by_id(device, f'{package_name}:id/button_toggle')
        time.sleep(3)
        print(f'发送视频成功')
        return True
    except Exception as e:
        print(f'发送视频失败 {e}')
        sys.exit(-1)

def send_file_signal(device: u2.Device, package_name: str, root_name: str) -> bool:
    try:
        print(f'开始发送文件消息')
        # 点击附件按钮
        click_view_by_id(device, f'{package_name}:id/button_toggle')
        # 点击文件选择按钮
        click_view_by_id(device, f'{package_name}:id/document_button')
        # 打开根目录
        click_view_by_description(device, '显示根目录')
        # 选中根目录
        root_items = get_view_list_by_text(device, root_name)
        click_view(root_items[len(root_items) - 1])
        # 选中 "其他"目录
        click_view_by_text(device, '其他')
        # 选中 forTest
        click_view_by_text(device, '_forTestFile')  # _forTestFile
        # 选择文件
        click_view_by_text_contains(device, f'file_')
        # 点击发送按钮
        click_view_by_id(device, f'{package_name}:id/button_toggle')
        time.sleep(3)
        print(f'发送文件成功')
        return True
    except Exception as e:
        print(f'发送文件失败 {e}')
        sys.exit(-1)
