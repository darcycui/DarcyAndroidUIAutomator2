# 授权所有权限
from utils.date_time_util import delay
import uiautomator2 as u2

def grant_permissions(device: u2.Device, app_name:str):
    print(f'{app_name} 授权权限')
    permissions = [
        'android.permission.POST_NOTIFICATIONS',
        'android.permission.CAMERA',
        'android.permission.RECORD_AUDIO',
        'android.permission.READ_EXTERNAL_STORAGE',
        'android.permission.READ_MEDIA_IMAGES',
        'android.permission.READ_MEDIA_VIDEO',
        'android.permission.READ_MEDIA_AUDIO',
        'android.permission.WRITE_EXTERNAL_STORAGE',
        'android.permission.REQUEST_IGNORE_BATTERY_OPTIMIZATIONS',
    ]
    for permission in permissions:
        print('授权权限-->', permission)
        device.shell(['pm', 'grant', app_name, permission])
    delay(3)
    print(f'{app_name} 授权完成')
