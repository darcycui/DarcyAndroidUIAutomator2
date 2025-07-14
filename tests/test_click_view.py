import unittest

import uiautomator2 as u2

from tests.data.TestData import DEVICE_ID
from utils.uiautomator2.connect import connect_device
from utils.uiautomator2.view_click import click_view_by_text, click_view_by_class_name, click_view_by_x_y, click_view, \
    click_x_y
from utils.uiautomator2.view_get import get_view_by_text
from utils.uiautomator2.view_info import get_view_center_x, get_view_center_y, get_view_info


class TestGetView(unittest.TestCase):
    def setUp(self):
        """每个测试方法前运行"""
        print("setUp")
        self.device: u2.Device = connect_device(DEVICE_ID)
        self.assertIsNotNone(self.device, "设备连接失败")

    def tearDown(self):
        """每个测试方法后运行"""
        print("tearDown")

    def test_click_view_by_text_directly(self):
        target_text = "接听"
        # 注意 这里不能使用 click_view_by_text(text 和 position 定位元素),会导致无法点击
        view = self.device(text=target_text)
        get_view_info(view)
        bb = click_view(view)
        self.assertEqual(True, bb, f"{target_text} 点击失败")

    def test_click_view_by_text(self):
        target_text = "forTest"
        target_text = "Gallery"
        target_text = "You joined the secret chat"
        target_text = "Check your Telegram messages"
        target_text = "Yes, it's me"
        target_text = "接听"
        target_text = "Unmute"
        target_text = "End Call"
        click_x_y(self.device, 500, 500)
        b: bool = click_view_by_text(self.device, target_text, waite=False)
        self.assertEqual(True, b, f"{target_text} 点击失败")

    def test_click_view_by_class_name(self):
        class_name = "android.view.View"
        b = click_view_by_class_name(self.device, class_name, 14)
        self.assertEqual(True, b, f"{class_name} 点击失败")

    def test_click_x_y(self):
        x = 500
        y = 500
        b = click_x_y(self.device, 500, 500)
        self.assertEqual(True, b, f"({x},{y}) 点击失败")
