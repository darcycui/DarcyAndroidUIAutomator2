import unittest
import uiautomator2 as u2

from message_signal.bean.SignalBean import SignalBean
from message_signal.config.global_config_sig import SIGNAL_DEVICE_ID_IN, SIGNAL_COUNTRY_NUMBER_IN, \
    SIGNAL_PHONE_NUMBER_IN, SIGNAL_CHAT_USER_NAME_IN, SIGNAL_ROOT_NAME_IN, \
    SIGNAL_PERMISSIONS, SIGNAL_USER_NAME_IN
from utils.uiautomator2.connect import connect_device
from utils.uiautomator2.permission import grant_app_permissions


class Permission(unittest.TestCase):
    def setUp(self):
        self.user_in = SignalBean(
            device_id=SIGNAL_DEVICE_ID_IN,
            country_number=SIGNAL_COUNTRY_NUMBER_IN,
            phone_number=SIGNAL_PHONE_NUMBER_IN,
            chat_user_name=SIGNAL_CHAT_USER_NAME_IN,
            root_name=SIGNAL_ROOT_NAME_IN,
            user_name=SIGNAL_USER_NAME_IN)

        # self.device: u2.Device = connect_device(self.user_in.device_id)
        self.device: u2.Device = connect_device(self.user_out.device_id)

    def tearDown(self):
        pass

    def test_grant_app_permissions(self):
        grant_app_permissions(self.device, self.user_in.package_name, SIGNAL_PERMISSIONS)
