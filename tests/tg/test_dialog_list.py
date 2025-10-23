import unittest

import uiautomator2 as u2

from message_tg.bean.TGBean import TGBean
from message_tg.helper.dialog_list_helper import click_dialog_list, click_dialog_list_with_position
from tests.data.TestData import DEVICE_ID, COUNTRY_NUMBER, PHONE_NUMBER, CHAT_USER_NAME, ROOT_NAME
from utils.uiautomator2.connect import connect_device, prepare


class TestDialogList(unittest.TestCase):
    def setUp(self):
        """每个测试方法前运行"""
        print("setUp")
        self.device: u2.Device = connect_device(DEVICE_ID)
        self.assertIsNotNone(self.device, "设备连接失败")
        self.user = TGBean(DEVICE_ID, COUNTRY_NUMBER, PHONE_NUMBER, CHAT_USER_NAME, ROOT_NAME)

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
