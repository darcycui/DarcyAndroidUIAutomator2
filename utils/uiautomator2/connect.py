import time

import uiautomator2 as u2

from utils.date_time_util import delay


def connect_device(device_id: str) -> u2.Device:
    print('连接设备:', device_id)
    # 连接设备
    device = u2.connect(device_id)
    # 格式化log
    # u2.enable_pretty_logging()
    # 打印出代码背后的HTTP请求
    # device.debug = True
    # 设置元素查找等待时间(默认20s)
    device.implicitly_wait(20.0)
    print('设备信息:', device.info)
    return device


def quite(device):
    print('退出')
    delay(3)
    device.stop_uiautomator()
    print('退出完毕')
