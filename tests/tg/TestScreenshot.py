import unittest

from tests.data.TestData import DEVICE_ID
from utils.date_time_util import get_current_day
from utils.file_util import check_file_exists, create_folders
from utils.uiautomator2.connect import connect_device
from utils.uiautomator2.screenshot import screen_shot
from utils.uiautomator2.view_wait import wait_view_appear_by_text, wait_view_gone_by_text


class TestWait(unittest.TestCase):

    def setUp(self):
        """每个测试方法前运行"""
        self.device = connect_device(DEVICE_ID)
        self.assertIsNotNone(self.device, '设备连接失败')

    def tearDown(self):
        """每个测试方法后运行"""
        print("tearDown")


    def test_create_folders(self):
        """测试创建目录"""
        file_path = '../../screen_shot/kugou'
        success = create_folders(file_path)
        self.assertTrue(success, '目录创建失败1')
        file_exist = check_file_exists(file_path)
        self.assertTrue(file_exist, '目录创建失败2')

    def test_screenshot(self):
        """测试截图"""
        current_day = get_current_day()
        file_path = screen_shot(self.device, f'tg_{current_day}', 'inspection', 1)
        file_exist = check_file_exists(file_path)
        self.assertTrue(file_exist, '截图失败')
