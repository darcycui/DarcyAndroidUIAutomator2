import os
import time

import uiautomator2 as u2

from utils.date_time_util import delay
from utils.file_util import check_file_exists


def screen_shot(device: u2.Device, sub_folder_name: str, file_name: str, delay_seconds: int):
    print(f'等待 {delay_seconds}s 后截图')
    # delay(delay_seconds)
    delay(1)
    time_stamp = time.strftime('%Y%m%d_%H%M', time.localtime())
    # 检查文件夹是否存在
    if not os.path.exists('screen_shot'):
        os.mkdir('screen_shot')
    # 检查文件夹是否存在
    # 统一路径处理
    folder_path = f'screen_shot/{sub_folder_name}'
    if not os.path.exists(folder_path):
        os.mkdir(folder_path)
        exist = check_file_exists(folder_path)
        print(f'创建后检查：{folder_path} 是否存在:{exist}')
    else:
        print(f'{folder_path} 存在')
    # real_file_name = f'{folder_path }/' + file_name + '_' + time_stamp + '.jpg'
    real_file_name = f'screen_shot/{sub_folder_name}/' + file_name + '_' + time_stamp + '.jpg'
    print('截图开始+++')
    device.screenshot(real_file_name)
    print('截图结束---')
