import unittest
import uiautomator2 as u2

from message_signal.bean.SignalBean import SignalBean
from message_signal.config.global_config_sig import SIGNAL_DEVICE_ID_IN, SIGNAL_COUNTRY_NUMBER_IN, \
    SIGNAL_PHONE_NUMBER_IN, SIGNAL_CHAT_USER_NAME_IN, SIGNAL_ROOT_NAME_IN, SIGNAL_USER_NAME_IN, SIGNAL_DEVICE_ID_OUT, \
    SIGNAL_COUNTRY_NUMBER_OUT, SIGNAL_PHONE_NUMBER_OUT, SIGNAL_CHAT_USER_NAME_OUT, SIGNAL_ROOT_NAME_OUT, \
    SIGNAL_USER_NAME_OUT
from message_signal.helper.add_friend_helper import add_friend_signal
from message_signal.helper.chat_helper import chat_signal
from utils.uiautomator2.connect import connect_device


class ChatSignal(unittest.TestCase):
    def setUp(self):
        self.user_in = SignalBean(
            device_id=SIGNAL_DEVICE_ID_IN,
            country_number=SIGNAL_COUNTRY_NUMBER_IN,
            phone_number=SIGNAL_PHONE_NUMBER_IN,
            chat_user_name=SIGNAL_CHAT_USER_NAME_IN,
            root_name=SIGNAL_ROOT_NAME_IN,
            user_name=SIGNAL_USER_NAME_IN)

        self.user_out = SignalBean(
            device_id=SIGNAL_DEVICE_ID_OUT,
            country_number=SIGNAL_COUNTRY_NUMBER_OUT,
            phone_number=SIGNAL_PHONE_NUMBER_OUT,
            chat_user_name=SIGNAL_CHAT_USER_NAME_OUT,
            root_name=SIGNAL_ROOT_NAME_OUT,
            user_name=SIGNAL_USER_NAME_OUT)

        self.device_in: u2.Device = connect_device(self.user_in.device_id)
        self.device_out: u2.Device = connect_device(self.user_out.device_id)

    def tearDown(self):
        pass

    def test_chat(self):
        chat_signal(self.device_in, self.device_out, self.user_in, self.user_out)