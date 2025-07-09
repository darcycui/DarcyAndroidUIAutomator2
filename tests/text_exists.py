import unittest

from tests.data.TestData import DEVICE_ID, CHAT_USER_NAME
from utils.uiautomator2.connect import connect_device
from utils.uiautomator2.view_exists import exists_by_text, exists_by_text_contains, exists_by_description, exists_by_id
from utils.uiautomator2.view_get import get_view_by_text


class TestViewExists(unittest.TestCase):
    def setUp(self):
        """每个测试方法前运行"""
        print("setUp")
        self.device = connect_device(DEVICE_ID)
        self.assertIsNotNone(self.device, '设备连接失败')
    def tearDown(self):
        """每个测试方法后运行"""
        print("tearDown")

    def test_get_view_by_text(self):
        target_text = "forTest"
        target_text = "Gallery"
        target_text = "You joined the secret chat"
        target_text = "Check your Telegram messages"
        b: bool = get_view_by_text(self.device, target_text) is not None
        self.assertEqual(True, b, f"{target_text} 不存在")

    def test_exists_by_text(self):
        target_text = "forTest"
        target_text = "Gallery"
        target_text = "You joined the secret chat"
        target_text = "Check your Telegram messages"
        b: bool = exists_by_text(self.device, target_text)
        self.assertEqual(True, b, f"{target_text} 不存在")

    def test_exists_by_text_contains(self):
        target_text = "Telegram"
        target_text = "You joined the secret chat"
        target_text = CHAT_USER_NAME
        b: bool = exists_by_text_contains(self.device, target_text)
        self.assertEqual(True, b, f"{target_text} 不存在")

    def test_exists_by_description(self):
        target_text = "Instant camera"
        b: bool = exists_by_description(self.device, target_text)
        self.assertEqual(True, b, f"{target_text} 不存在")

    def test_exists_by_id(self):
        b: bool = exists_by_id(self.device, "android:id/navigationBarBackground")
        print(f"b={b}, type={type(b)}")  # 检查返回值类型
        self.assertEqual(True, b, "android:id/navigationBarBackground 不存在")