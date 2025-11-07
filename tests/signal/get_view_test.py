from tests.signal.base.base_test import BaseTest
from utils.uiautomator2.view_get import get_view_by_id

from utils.uiautomator2.view_info import get_view_info


class GetView(BaseTest):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_get_view_by_id(self):
        view = get_view_by_id(self.device_in, f'{self.user_in.package_name}:id/country_code')
        get_view_info(view)
        self.assertIsNotNone(view, '获取view失败')
