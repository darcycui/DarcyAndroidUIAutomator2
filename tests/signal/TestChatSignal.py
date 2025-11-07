from message_signal.helper.chat_helper import chat_signal
from tests.signal.base.BaseSignalTest import BaseSignalTest


class TestChatSignal(BaseSignalTest):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_chat(self):
        chat_signal(self.device_in, self.device_out, self.user_in, self.user_out)