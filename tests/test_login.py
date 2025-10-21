import unittest

from message_tg.bean.UserBean import UserBean
from message_tg.login import login
from tests.data.TestData import DEVICE_ID, PACKAGE_NAME_TEST, PACKAGE_NAME_WEB_TEST, COUNTRY_NUMBER, PHONE_NUMBER, \
    CHAT_USER_NAME, ROOT_NAME
from utils.uiautomator2.connect import connect_device, prepare, prepare_login


class TestLogin(unittest.TestCase):
    def setUp(self):
        """每个测试方法前运行"""
        self.device = connect_device(DEVICE_ID)
        self.assertIsNotNone(self.device, '设备连接失败')
        self.user = UserBean(DEVICE_ID, COUNTRY_NUMBER, PHONE_NUMBER, CHAT_USER_NAME, ROOT_NAME)

    def tearDown(self):
        """每个测试方法后运行"""
        print("tearDown")

    def test_login(self):
        """测试登录"""
        prepare_login(self.device, self.user)
        b = login(self.device, self.user)
        self.assertEqual(True, b, '登录失败')


if __name__ == '__main__':
    unittest.main()
