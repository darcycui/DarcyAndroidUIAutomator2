from message_signal.helper.add_friend_helper import add_friend_signal
from tests.signal.base.base_test import BaseTest


class AddFriend(BaseTest):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_add_friend(self):
        add_friend_signal(self.device_in, self.user_in)
