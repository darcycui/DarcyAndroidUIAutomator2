import logging
import time

import uiautomator2 as u2

from message.permission import grant_app_permissions
from utils.date_time_util import delay
from utils.uiautomator2.apps import stop_app, clear_app_data, start_app
from utils.uiautomator2.device import turn_screen_on
from utils.uiautomator2.press_key import press_home


def connect_device(device_id: str) -> u2.Device:
    print('连接设备:', device_id)
    # 连接设备
    device = u2.connect(device_id)
    # 开启 uiautomator2 调试日志
    logging.basicConfig(level=logging.DEBUG)
    # 格式化log
    u2.enable_pretty_logging()
    # 打印出代码背后的HTTP请求
    # device.debug = True
    # 设置元素查找等待时间(默认20s)
    device.implicitly_wait(20.0)
    print('设备信息:', device.info)
    return device

def prepare(device: u2.Device, package_name: str, need_clear_data: bool = False):
    # 亮屏
    turn_screen_on(device)
    # 按Home 键
    press_home(device)
    # 结束应用
    stop_app(device, package_name)
    if need_clear_data:
        # 清空应用数据
        clear_app_data(device, package_name)
    # 授权所有权限
    grant_app_permissions(device, package_name)
    # 启动应用
    start_app(device, package_name)


def quite(device):
    print('退出')
    delay(3)
    device.stop_uiautomator()
