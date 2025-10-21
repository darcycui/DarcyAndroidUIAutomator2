import unittest

from message_tg.call import call_voice, call_video, call_end, call_rate_close, call_answer_video, call_answer_voice
from tests.data.TestData import DEVICE_ID
from utils.uiautomator2.connect import connect_device


class TestCall(unittest.TestCase):

    def setUp(self):
        """每个测试方法前运行"""
        self.device = connect_device(DEVICE_ID)
        self.assertIsNotNone(self.device, '设备连接失败')

    def tearDown(self):
        """每个测试方法后运行"""
        print("tearDown")

    def test_call_voice(self):
        """测试语音通话"""
        self.assertTrue(call_voice(self.device), '语音通话失败')

    def test_call_video(self):
        """测试视频通话"""
        self.assertTrue(call_video(self.device), '视频通话失败')

    def test_call_end(self):
        """测试结束通话"""
        self.assertTrue(call_end(self.device, 10), '结束通话失败')

    def test_call_answer_voice(self):
        """测试接听语音通话"""
        self.assertTrue(call_answer_voice(self.device), '接听语音通话失败')

    def test_call_answer_video(self):
        """测试接听视频通话"""
        self.assertTrue(call_answer_video(self.device), '接听视频通话失败')

    def test_call_rate_close(self):
        """测试关闭评分"""
        self.assertTrue(call_rate_close(self.device), '关闭评分失败')

