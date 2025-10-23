import unittest

import uiautomator2 as u2

from message_signal.bean.SignalBean import SignalBean
from message_signal.config.global_config_sig import SIGNAL_DEVICE_ID_IN, SIGNAL_COUNTRY_NUMBER_IN, \
    SIGNAL_PHONE_NUMBER_IN, SIGNAL_CHAT_USER_NAME_IN, SIGNAL_ROOT_NAME_IN, SIGNAL_USER_NAME_IN
from message_signal.helper.add_friend_helper import add_friend_signal
from utils.uiautomator2.connect import connect_device


class AddFriend(unittest.TestCase):
    def setUp(self):
        self.user_in = SignalBean(
            device_id=SIGNAL_DEVICE_ID_IN,
            country_number=SIGNAL_COUNTRY_NUMBER_IN,
            phone_number=SIGNAL_PHONE_NUMBER_IN,
            chat_user_name=SIGNAL_CHAT_USER_NAME_IN,
            root_name=SIGNAL_ROOT_NAME_IN,
            user_name=SIGNAL_USER_NAME_IN)

        self.device: u2.Device = connect_device(self.user_in.device_id)

    def tearDown(self):
        pass

    def test_add_friend(self):
        add_friend_signal(self.device, self.user_in)
