import unittest

from message_tg.bean.TGBean import TGBean
from message_tg.config.global_config_tg import TG_PERMISSIONS
from message_tg.helper.login_helper import login_tg
from tests.data.TestData import DEVICE_ID, COUNTRY_NUMBER, PHONE_NUMBER, \
    CHAT_USER_NAME, ROOT_NAME
from tests.tg.base.BaseTGTest import BaseTGTest
from utils.uiautomator2.connect import connect_device, prepare_login


class TestLogin(BaseTGTest):
    def setUp(self):
        """每个测试方法前运行"""
        super(TestLogin, self).setUp()
        self.device = self.device_out_huawei
        self.user = self.user_out_huawei
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
