from message_signal.helper.login_helper import login_signal
from tests.signal.base.base_test import BaseTest


class LoginSignal(BaseTest):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_login(self):
     login_signal(self.device_in, self.user_in)