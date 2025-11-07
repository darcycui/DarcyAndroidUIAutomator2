import unittest

from message_signal.config.global_config_sig import SIGNAL_PERMISSIONS
from tests.signal.base.BaseSignalTest import BaseSignalTest
from utils.uiautomator2.permission import grant_app_permissions


class TestPermission(BaseSignalTest):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_grant_app_permissions(self):
        grant_app_permissions(self.device_in, self.user_in.package_name, SIGNAL_PERMISSIONS)
