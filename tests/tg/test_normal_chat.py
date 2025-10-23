import unittest
from unittest import skipIf, skip

from message_tg.bean.TGBean import TGBean
from message_tg.helper.chat_normal_helper import start_chat_tg
from message_tg.helper.history_helper import clear_history_tg
from message_tg.helper.receive_helper import receive_off_message, receive_on_message, receive_chat_message
from message_tg.helper.chat_secure_helper import secure_chat_on, secure_chat_off
from message_tg.helper.send_helper import send_text_message
from tests.data.TestData import DEVICE_ID, CHAT_USER_NAME, COUNTRY_NUMBER, PHONE_NUMBER, ROOT_NAME
from utils.date_time_util import get_current_time
from utils.uiautomator2.connect import connect_device, prepare


class TestChat(unittest.TestCase):
    def setUp(self):
        """每个测试方法前运行"""
        print('setUp')
        self.device = connect_device(DEVICE_ID)
        self.assertIsNotNone(self.device, '设备连接失败')
        self.user = TGBean(DEVICE_ID, COUNTRY_NUMBER, PHONE_NUMBER, CHAT_USER_NAME, ROOT_NAME)

    def tearDown(self):
        """每个测试方法后运行"""
        print('tearDown')

    def test_open_chat_page(self):
        """测试打开聊天页面"""
        prepare(self.device, self.user)
        # 打开聊天页面
        b = start_chat_tg(self.device, self.user)
        self.assertEqual(True, b, '打开聊天页面失败')

    def test_clear_history(self):
        """测试清空聊天记录"""
        b = clear_history_tg(self.device)
        self.assertEqual(True, b, '清空聊天记录失败')

    def test_secure_chat_on(self):
        """测试密聊开关 打开"""
        b = secure_chat_on(self.device, CHAT_USER_NAME)
        self.assertEqual(True, b, '密聊开启失败')

    def test_secure_chat_off(self):
        """测试密聊开关 关闭"""
        b = secure_chat_off(self.device, CHAT_USER_NAME)
        self.assertEqual(True, b, '密聊关闭失败')

    def test_send_on_message(self):
        """测试发送 on 文本消息"""
        b = send_text_message(self.device, 'OnOnOn')
        self.assertEqual(True, b, '发送 on 消息失败')

    def test_send_off_message(self):
        """测试发送 off 文本消息"""
        b = send_text_message(self.device, 'OffOffOff')
        self.assertEqual(True, b, '发送 on 消息失败')

    def test_send_chat_message(self):
        """测试发送 chat 文本消息"""
        b = send_text_message(self.device, f'Chat Message {get_current_time()}')
        self.assertEqual(True, b, '发送 chat 消息失败')

    def test_receive_on_message(self):
        """测试接收 on 文本消息"""
        b = receive_on_message(self.device)
        self.assertEqual(True, b, '未接收到 on 消息')

    def test_receive_off_message(self):
        """测试接收 off 文本消息"""
        b = receive_off_message(self.device)
        self.assertEqual(True, b, '未接收到 off 消息')

    def test_receive_chat_message(self):
        """测试接收 chat 文本消息"""
        b = receive_chat_message(self.device)
        self.assertEqual(True, b, '未接收到 chat 消息')

    @skip('跳过 test_a')
    def test_a(self):
        print('test_a')

    version = 10
    @skipIf(version>=10, 'version>=10 跳过 test_b')
    def test_b(self):
        print('test_b')


if __name__ == '__main__':
    # 启动单元测试
    # unittest.main()

    # 创建测试套件
    suite = unittest.TestSuite()
    # 将测试用例添加到套件中
    suite.addTest(TestChat())
    # 创建执行器
    runner = unittest.TextTestRunner(verbosity=2)
    # 运行测试套件
    result = runner.run(suite)
