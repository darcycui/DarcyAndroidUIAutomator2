import unittest

from adbutils import device

from message_tg.bean.UserBean import UserBean
from message_tg.chat_end2end import start_end2end_chat_in, start_end2end_chat_out
from message_tg.chat_normal import start_chat
from message_tg.chat_secure import secure_chat_on, secure_chat_off
from message_tg.send import send_text_message
from tests.data.TestData import DEVICE_ID, CHAT_USER_NAME, PACKAGE_NAME_TEST, COUNTRY_NUMBER, PHONE_NUMBER, ROOT_NAME
from utils.date_time_util import get_current_time
from utils.uiautomator2.connect import connect_device, prepare


class TestSecretChat(unittest.TestCase):
    def setUp(self):
        """每个测试方法前运行"""
        print('setUp')
        self.device = connect_device(DEVICE_ID)
        self.assertIsNotNone(self.device, '设备连接失败')
        self.user = UserBean(DEVICE_ID, COUNTRY_NUMBER, PHONE_NUMBER, CHAT_USER_NAME, ROOT_NAME)

    def tearDown(self):
        """每个测试方法后运行"""
        print('tearDown')

    def test_start_end_to_end_chat_in(self):
        """测试开始端到端聊天 in"""
        prepare(self.device, self.user)
        start = start_chat(self.device, self.user)
        self.assertEqual(True, start, '开始聊天失败')
        b = start_end2end_chat_in(self.device, CHAT_USER_NAME)
        self.assertEqual(True, b, 'in: 开始End2End聊天失败')

    def test_start_end_to_end_chat_out(self):
        """测试开始端到端聊天 out"""
        prepare(self.device, self.user)
        b = start_end2end_chat_out(self.device)
        self.assertEqual(True, b, 'out: 开始End2End聊天失败')

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


if __name__ == '__main__':
    # 启动单元测试
    # unittest.main()

    # 创建测试套件
    suite = unittest.TestSuite()
    # 将测试用例添加到套件中
    suite.addTest(TestSecretChat())
    # 创建执行器
    runner = unittest.TextTestRunner(verbosity=2)
    # 运行测试套件
    result = runner.run(suite)
