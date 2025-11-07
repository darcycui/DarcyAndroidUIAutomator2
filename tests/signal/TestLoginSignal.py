from message_signal.helper.login_helper import login_signal
from tests.signal.base.BaseSignalTest import BaseSignalTest


class TestLoginSignal(BaseSignalTest):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_login(self):
     login_signal(self.device_in, self.user_in)