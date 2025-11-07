import unittest

from message_tg.config.global_config_tg import APKS_FOLDER_TG
from tests.data.TestData import DEVICE_ID, FILE_EXPLORER_PACKAGE_NAME, FILE_EXPLORER_TEXT
from utils.file_util import get_latest_file_in_folder
from utils.uiautomator2.connect import connect_device
from utils.uiautomator2.install_apk import install_apk, install_from_file_explorer
from utils.uiautomator2.push import push_file_to_device


class InstallTest(unittest.TestCase):
    def setUp(self):
        self.folder = APKS_FOLDER_TG
        self.device = connect_device(DEVICE_ID)

    def tearDown(self):
        pass

    def test_install_apk(self):
        apk_path = get_latest_file_in_folder(self.folder)
        install_apk(self.device, apk_path)

    def test_install_apk_manually(self):
        apk_path = get_latest_file_in_folder(self.folder)
        apk_name = apk_path.split("\\")[-1]
        push_file_to_device(self.device, apk_path, f"/sdcard/Documents/PTG/{apk_name}")
        install_from_file_explorer(self.device, FILE_EXPLORER_PACKAGE_NAME, FILE_EXPLORER_TEXT, apk_name)
