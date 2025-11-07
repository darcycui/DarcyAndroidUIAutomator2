import unittest

import uiautomator2 as u2

from message_signal.factory.signal_factory import get_signal_in, get_signal_out, get_signal_out_huawei
from utils.uiautomator2.connect import connect_device


class BaseSignalTest(unittest.TestCase):
    def setUp(self):
        self.user_in = get_signal_in()
        self.user_out = get_signal_out()
        self.user_out_huawei = get_signal_out_huawei()

        self.device_in: u2.Device = connect_device(self.user_in.device_id)
        self.device_out: u2.Device = connect_device(self.user_out.device_id)
        self.device_out_huawei: u2.Device = connect_device(self.user_out_huawei.device_id)

    def tearDown(self):
        pass
