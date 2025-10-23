import unittest

from message_tg.bean.TGBean import TGBean
from message_tg.config.global_config_tg import TG_PERMISSIONS
from message_tg.helper.login_helper import login_tg
from tests.data.TestData import DEVICE_ID, COUNTRY_NUMBER, PHONE_NUMBER, \
    CHAT_USER_NAME, ROOT_NAME
from utils.uiautomator2.connect import connect_device, prepare_login


class TestLogin(unittest.TestCase):
    def setUp(self):
        """每个测试方法前运行"""
        self.device = connect_device(DEVICE_ID)
        self.assertIsNotNone(self.device, '设备连接失败')
        self.user = TGBean(DEVICE_ID, COUNTRY_NUMBER, PHONE_NUMBER, CHAT_USER_NAME, ROOT_NAME)

    def tearDown(self):
        """每个测试方法后运行"""
        print("tearDown")

    def test_login(self):
        """测试登录"""
        prepare_login(self.device, self.user, TG_PERMISSIONS)
        b = login_tg(self.device, self.user)
        self.assertEqual(True, b, '登录失败')


if __name__ == '__main__':
    unittest.main()
