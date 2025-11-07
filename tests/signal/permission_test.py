import unittest

from message_signal.config.global_config_sig import SIGNAL_PERMISSIONS
from tests.signal.base.base_test import BaseTest
from utils.uiautomator2.permission import grant_app_permissions


class Permission(BaseTest):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_grant_app_permissions(self):
        grant_app_permissions(self.device_in, self.user_in.package_name, SIGNAL_PERMISSIONS)
