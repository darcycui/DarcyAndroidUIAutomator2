import unittest

from tests.data.TestData import DEVICE_ID
from utils.uiautomator2.connect import connect_device
from utils.uiautomator2.view_exists import exists_by_text, exists_by_text_contains, exists_by_description, exists_by_id


class TestViewExists(unittest.TestCase):
    def setUp(self):
        """每个测试方法前运行"""
        print("setUp")
        self.device = connect_device(DEVICE_ID)
        self.assertIsNotNone(self.device, '设备连接失败')
    def tearDown(self):
        """每个测试方法后运行"""
        print("tearDown")

    def test_exists_by_text(self):
        b: bool = exists_by_text(self.device, "Telegram")
        self.assertEqual(True, b, "Telegram 不存在")

    def test_exists_by_text_contains(self):
        b: bool = exists_by_text_contains(self.device, "Telegram")
        self.assertEqual(True, b, "*Telegram* 不存在")

    def test_exists_by_description(self):
        b: bool = exists_by_description(self.device, "Search")
        self.assertEqual(True, b, "Search 不存在")

    def test_exists_by_id(self):
        b: bool = exists_by_id(self.device, "android:id/navigationBarBackground")
        print(f"b={b}, type={type(b)}")  # 检查返回值类型
        self.assertEqual(True, b, "android:id/navigationBarBackground 不存在")