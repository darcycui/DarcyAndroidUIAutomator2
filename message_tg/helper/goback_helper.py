import uiautomator2 as u2

from utils.date_time_util import delay
from utils.uiautomator2.view_click import click_view_by_description


def go_back(device: u2.Device):
    # 返回箭头
    print('点击返回箭头')
    delay(1)
    click_view_by_description(device, 'Go back')
    delay(1)
