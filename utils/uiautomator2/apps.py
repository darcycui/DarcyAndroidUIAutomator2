import uiautomator2 as u2

from utils.date_time_util import delay


def start_app(device: u2.Device, package_name: str):
    print('启动应用:', package_name)
    device.app_start(package_name)
    delay(3)


def stop_app(device: u2.Device, package_name: str):
    print('停止应用:', package_name)
    device.app_stop(package_name)
    delay(3)


def clear_app_data(device: u2.Device, package_name: str):
    print('清除应用数据:', package_name)
    device.app_clear(package_name)
    delay(3)
    print('清除应用数据:完成')
