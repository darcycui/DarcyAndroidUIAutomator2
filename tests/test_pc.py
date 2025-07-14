import os
import unittest

from pc_script import call_pc_powershell, call_pc_bat


class TestPC(unittest.TestCase):
    def setUp(self):
        print('setUp')

    def tearDown(self):
        print('tearDown')

    def test_call_pc_powershell(self):
        b = call_pc_powershell('D:/bbb/copy_TG.ps1')
        # b = call_pc_powershell('../pc/test.ps1')
        self.assertEqual(True, b, '调用 Powershell 脚本错误')

    def test_call_pc_bat(self):
        # 获取文件所在目录的绝对路径
        current_dir = os.path.dirname(os.path.abspath(__file__))
        bat_path = os.path.join(current_dir, '..', 'pc', 'test.bat')
        b = call_pc_bat(bat_path)
        self.assertEqual(True, b, '调用 Bat 脚本错误')
