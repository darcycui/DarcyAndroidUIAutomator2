import unittest
import uiautomator2 as u2

from tests.data.TestData import DEVICE_ID
from utils import string_util
from utils.uiautomator2.apps import start_app, stop_app
from utils.uiautomator2.connect import connect_device


class TestVerificationCode(unittest.TestCase):
    def setUp(self):
        """每个测试方法前运行"""
        self.device: u2.Device = connect_device(DEVICE_ID)
        self.assertIsNotNone(self.device, '设备连接失败')

    def tearDown(self):
        """每个测试方法后运行"""
        print("tearDown")

    def test_split_verification_code(self):
        code:int = 65795
        print(f"code={code}")
        code_str:str = f"Login code: {code}. Do not give this code to anyone, even if they say they are from Telegram!"
        print(f"code_str={code_str}")
        code_split:str = string_util.split_verification_code(code_str)
        self.assertEqual(f"{code}", code_split, "验证码提取失败")
