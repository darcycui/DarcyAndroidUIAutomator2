import unittest

from message_tg.helper.send_helper import send_image, send_video, send_file
from message_tg.helper.take_helper import send_take_image, send_take_video, send_take_audio, send_take_round_video
from tests.data.TestData import DEVICE_ID, ROOT_NAME
from utils.uiautomator2.connect import connect_device


class TestImage(unittest.TestCase):
    def setUp(self):
        """每个测试方法前运行"""
        print('setUp')
        self.device = connect_device(DEVICE_ID)
        self.assertIsNotNone(self.device, '设备连接失败')

    def tearDown(self):
        """每个测试方法后运行"""
        print('tearDown')

    def test_send_image(self):
        """测试发送图片"""
        b = send_image(self.device)
        self.assertEqual(True, b, '发送图片失败')

    def test_send_video(self):
        """测试发送视频"""
        b = send_video(self.device)
        self.assertEqual(True, b, '发送视频失败')

    def test_send_file(self):
        """测试发送文件"""
        b = send_file(self.device, ROOT_NAME)
        self.assertEqual(True, b, '发送文件失败')

    def test_send_take_image(self):
        """测试发送拍照"""
        b = send_take_image(self.device)
        self.assertEqual(True, b, '发送拍照失败')

    def test_send_take_video(self):
        """测试发送拍摄全屏视频"""
        b = send_take_video(self.device)
        self.assertEqual(True, b, '发送拍摄全屏视频失败')

    def test_send_take_audio(self):
        """测试发送录音"""
        b = send_take_audio(self.device)
        self.assertEqual(True, b, '发送录音失败')

    def test_send_take_round_video(self):
        """测试发送拍摄短视频"""
        b = send_take_round_video(self.device)
        self.assertEqual(True, b, '发送拍摄短视频失败')