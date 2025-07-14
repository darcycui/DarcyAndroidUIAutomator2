import unittest

from tests.data.TestData import DEVICE_ID
from utils.uiautomator2.connect import connect_device
from utils.uiautomator2.view_wait import wait_view_appear_by_text, wait_view_gone_by_text


class TestWait(unittest.TestCase):

    def setUp(self):
        """每个测试方法前运行"""
        self.device = connect_device(DEVICE_ID)
        self.assertIsNotNone(self.device, '设备连接失败')

    def tearDown(self):
        """每个测试方法后运行"""
        print("tearDown")

    def test_wait_view_appear(self):
        """测试等待 view 出现"""
        text = 'End Call'
        b = wait_view_appear_by_text(self.device, text, 20)
        self.assertTrue(b, 'view 未出现')

    def test_wait_view_gone(self):
        """测试等待 view 消失"""
        text = 'End Call'
        b = wait_view_gone_by_text(self.device, text, 20)
        self.assertTrue(b, 'view 未消失')
