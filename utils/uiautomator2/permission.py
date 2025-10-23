# 授权所有权限
from utils.date_time_util import delay
import uiautomator2 as u2


def grant_app_permissions(device: u2.Device, app_name: str, permissions: list[str]):
    print(f'{app_name} 授权权限')
    for permission in permissions:
        print('授权权限-->', permission)
        device.shell(['pm', 'grant', app_name, permission])
    delay(3)
    print(f'{app_name} 授权完成')
