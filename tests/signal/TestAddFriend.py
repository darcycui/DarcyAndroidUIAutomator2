from message_signal.helper.add_friend_helper import add_friend_signal
from tests.signal.base.BaseSignalTest import BaseSignalTest


class TestAddFriend(BaseSignalTest):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_add_friend(self):
        add_friend_signal(self.device_in, self.user_in)
