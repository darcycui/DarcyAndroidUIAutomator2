import os
import time
import uiautomator2 as u2

from utils.date_time_util import delay


def screen_shot(device: u2.Device, file_name: str, delay_seconds: int):
    print(f'等待 {delay_seconds}s 后截图')
    delay(delay_seconds)
    time_stamp = time.strftime('%Y%m%d_%H%M', time.localtime())
    # 检查文件夹是否存在
    if not os.path.exists('../../screen_shot'):
        os.mkdir('../../screen_shot')
    real_file_name = 'screen_shot/' + file_name + '_' + time_stamp + '.jpg'
    print('截图开始+++')
    device.screenshot(real_file_name)
    print('截图结束---')
