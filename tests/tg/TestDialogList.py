import unittest

import uiautomator2 as u2

from message_tg.bean.TGBean import TGBean
from message_tg.helper.dialog_list_helper import click_dialog_list, click_dialog_list_with_position
from message_tg.tg_factory import get_user_in_tg, get_user_out_huawei_tg
from tests.data.TestData import DEVICE_ID, COUNTRY_NUMBER, PHONE_NUMBER, CHAT_USER_NAME, ROOT_NAME
from tests.tg.base.BaseTGTest import BaseTGTest
from utils.uiautomator2.connect import connect_device, prepare


class TestDialogList(BaseTGTest):
    def setUp(self):
        """每个测试方法前运行"""
        print("setUp")
        super(TestDialogList, self).setUp()
        self.device = self.device_out_huawei
        self.user = self.user_out_huawei

    def tearDown(self):
        """每个测试方法后运行"""
        print("tearDown")

    def test_click_dialog_list(self):
        """测试点击聊天列表"""
        prepare(self.device, self.user)
        b = click_dialog_list(self.device)
        self.assertEqual(True, b, "点击列表失败")

    def test_click_dialog_item(self):
        """测试点击聊天列表项 item """
        prepare(self.device, self.user)
        position: int = 0
        b = click_dialog_list_with_position(self.device, position)
        self.assertEqual(True, b, "点击列表 item 失败")
