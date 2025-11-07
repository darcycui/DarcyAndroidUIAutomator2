import unittest
import uiautomator2 as u2

from message_tg.tg_factory import get_user_in_tg, get_user_out_tg, get_user_out_huawei_tg
from utils.uiautomator2.connect import connect_device


class BaseTGTest(unittest.TestCase):
    def setUp(self):
        self.user_in = get_user_in_tg()
        self.user_out = get_user_out_tg()
        self.user_out_huawei = get_user_out_huawei_tg()

        self.device_in: u2.Device = connect_device(self.user_in.device_id)
        self.device_out: u2.Device = connect_device(self.user_out.device_id)
        self.device_out_huawei: u2.Device = connect_device(self.user_out_huawei.device_id)

        pass

    def tearDown(self):
        pass
