import unittest

from message.login import login
from tests.data.TestData import DEVICE_ID, PACKAGE_NAME, PACKAGE_NAME_WEB, COUNTRY_NUMBER, PHONE_NUMBER
from utils.uiautomator2.connect import connect_device, prepare


class TestLogin(unittest.TestCase):
    def setUp(self):
        """每个测试方法前运行"""
        self.device = connect_device(DEVICE_ID)
        self.assertIsNotNone(self.device, '设备连接失败')

    def test_login(self):
        """测试登录"""
        prepare(self.device, PACKAGE_NAME, True)
        b = login(self.device, PACKAGE_NAME, PACKAGE_NAME_WEB, COUNTRY_NUMBER, PHONE_NUMBER)
        self.assertEqual(True, b, '登录失败')


if __name__ == '__main__':
    unittest.main()
