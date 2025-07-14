import sys
import unittest

import uiautomator2 as u2

from tests.data.TestData import DEVICE_ID
from utils.uiautomator2.connect import connect_device
from utils.uiautomator2.view_exists import exists_by_text
from utils.uiautomator2.view_get import get_view_by_text, get_view_by_class_name, get_view_by_text_contains
from utils.uiautomator2.view_wait import wait_view_appear_by_text


class TestGetView(unittest.TestCase):
    def setUp(self):
        """每个测试方法前运行"""
        print("setUp")
        self.device: u2.Device = connect_device(DEVICE_ID)
        self.assertIsNotNone(self.device, "设备连接失败")

    def tearDown(self):
        """每个测试方法后运行"""
        print("tearDown")

    def test_get_view_by_text(self):
        target_text = "forTest"
        target_text = "Gallery"
        target_text = "You joined the secret chat"
        target_text = "Check your Telegram messages"
        target_text = "Yes, it's me"
        target_text = "接听"
        if not wait_view_appear_by_text(self.device, target_text, timeout=10):
            print(f'未检测到 {target_text} 按钮')
            sys.exit(1)
        self.dump_ui_to_file()
        view = get_view_by_text(self.device, target_text)
        print(f'view type: {type(view)}')
        b: bool = view is not None
        self.assertEqual(True, b, f"{target_text} 获取失败")

    def dump_ui_to_file(self):
        # 打印当前页面结构用于调试
        hierarchy = self.device.dump_hierarchy()
        with open("current_ui.xml", "w", encoding="utf-8") as f:
            f.write(hierarchy)
        print("当前UI结构已保存至 current_ui.xml")

    def test_get_view_by_class_name(self):
        class_name = "android.view.View"
        b: bool = get_view_by_class_name(self.device, class_name, 6) is not None
        self.assertEqual(True, b, f"{class_name} 获取失败")
