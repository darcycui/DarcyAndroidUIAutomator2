import unittest
import uiautomator2 as u2

from tests.data.TestData import DEVICE_ID
from utils.uiautomator2.apps import start_app, stop_app
from utils.uiautomator2.connect import connect_device


class TestApps(unittest.TestCase):
    def setUp(self):
        """每个测试方法前运行"""
        self.device: u2.Device = connect_device(DEVICE_ID)
        self.assertIsNotNone(self.device, '设备连接失败')

    def tearDown(self):
        """每个测试方法后运行"""
        print("tearDown")

    def test_start_app(self):
        app_name = 'org.telegram.messenger.beta'
        start_app(self.device, app_name)

    def test_stop_app(self):
        app_name = 'org.telegram.messenger.beta'
        stop_app(self.device, app_name)
