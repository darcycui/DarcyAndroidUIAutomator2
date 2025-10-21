import os
import subprocess
import time
from subprocess import Popen

import uiautomator2 as u2


# scrcpy -s RFCW8014R4E --record v.mp4
def screen_record_start(file_name: str, device_id: str) -> Popen:
    print('录屏开始+++')
    # 格式化时间戳
    time_stamp = time.strftime('%Y%m%d_%H%M', time.localtime())
    # 检查文件夹是否存在
    if not os.path.exists('../../screen_record'):
        os.mkdir('../../screen_record')
    real_file_name = 'screen_record/' + file_name + '_' + time_stamp + '.mp4'
    # deprecated 推荐使用scrcpy录屏
    # device.screenrecord(real_file_name)
    command = ['scrcpy', '-s', device_id, '--record', real_file_name]
    print('command=', command)
    # 执行cmd命令
    process = subprocess.Popen(command)
    return process


def screen_record_stop(process: Popen):
    print('录屏结束---')
    # device.screenrecord.stop()
    time.sleep(10)
    # 终止 scrcpy
    process.terminate()
    # # 发送中断信号（Ctrl+C）给scrcpy进程
    # os.kill(process.pid, message_signal.SIGINT)
    process.wait()
    print('录屏结束完毕---')
