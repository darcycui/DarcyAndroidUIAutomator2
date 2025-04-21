import os
import signal
import subprocess
import time

import uiautomator2 as u2


def connect_device(device_id):
    print('连接设备:', device_id)
    # 连接设备
    device = u2.connect(device_id)
    # 格式化log
    # u2.enable_pretty_logging()
    # 打印出代码背后的HTTP请求
    # device.debug = True
    # 设置元素查找等待时间(默认20s)
    device.implicitly_wait(10.0)
    print('设备信息:', device.info)
    return device


def start_app(device, package_name):
    print('启动应用:', package_name)
    device.app_start(package_name)
    time.sleep(3)


def stop_app(device, package_name):
    print('停止应用:', package_name)
    device.app_stop(package_name)
    time.sleep(3)


def click_button_by_text(device, button_name):
    print('点击按钮:', button_name)
    time.sleep(3)
    device(text=button_name).click()


def click_button_by_class_name(device, class_name):
    print('点击按钮:', class_name)
    time.sleep(3)
    device(className=class_name).click()


def click_button_by_id(device, button_id):
    print('点击按钮:', button_id)
    time.sleep(3)
    device(resourceId=button_id).click()


def screen_shot(device, file_name, delay):
    print('截图开始+++')
    time.sleep(delay)
    time_stamp = time.strftime('%Y%m%d_%H%M', time.localtime())
    # 检查文件夹是否存在
    if not os.path.exists('screen_shot'):
        os.mkdir('screen_shot')
    real_file_name = 'screen_shot/' + file_name + '_' + time_stamp + '.jpg'
    device.screenshot(real_file_name)
    print('截图结束---')


# scrcpy -s RFCW8014R4E --record v.mp4
def screen_record_start(file_name, device_id):
    print('录屏开始+++')
    # 格式化时间戳
    time_stamp = time.strftime('%Y%m%d_%H%M', time.localtime())
    # 检查文件夹是否存在
    if not os.path.exists('screen_record'):
        os.mkdir('screen_record')
    real_file_name = 'screen_record/' + file_name + '_' + time_stamp + '.mp4'
    # deprecated 推荐使用scrcpy录屏
    # device.screenrecord(real_file_name)
    command = ['scrcpy', '-s', device_id, '--record', real_file_name]
    print('command=', command)
    # 执行cmd命令
    process = subprocess.Popen(command)
    return process


def screen_record_stop(process):
    print('录屏结束---')
    # device.screenrecord.stop()
    time.sleep(10)
    # 终止 scrcpy
    process.terminate()
    # # 发送中断信号（Ctrl+C）给scrcpy进程
    # os.kill(process.pid, signal.SIGINT)
    process.wait()
    print('录屏结束完毕---')

def unlock_screen(device):
    print('解锁屏幕')
    device.unlock()

def lock_screen(device):
    print('锁屏')
    device.lock()

def turn_screen_on(device):
    print('屏幕点亮')
    device.screen_on()


def turn_screen_off(device):
    print('屏幕熄灭')
    device.screen_off()


def press_back(device):
    print('点击返回键')
    time.sleep(3)
    device.press('back')


'''
支持的按键
home
back
left
right
up
down
center
menu
search
enter
delete ( or del)
recent (recent apps)
volume_up
volume_down
volume_mute
camera
power
'''


def press_home(device):
    print('点击Home键')
    time.sleep(1)
    device.press('home')


def press_menu(device):
    print('点击Menu键')
    time.sleep(1)
    device.press('menu')


def press_recent(device):
    print('点击最近任务键')
    time.sleep(1)
    device.press('recent')


def press_search(device):
    print('点击搜索键')
    time.sleep(1)
    device.press('search')


def get_view_by_id(device, view_id):
    view = device(resourceId=view_id)
    return view


def get_view_by_text(device, text):
    view = device(text=text)
    return view


def get_view_by_class_name(device, class_name):
    view = device(className=class_name)
    return view


def get_view_info(view):
    info = view.info
    print('获取元素信息:', info)
    return info


def get_child_view_by_text(view, text):
    return view.child_by_text(text)


def get_child_view_by_class_name(view, class_name):
    return view.child(className=class_name)


def input_text(device, hint, text):
    print('输入文本:', text)
    time.sleep(1)
    # 确保快速输入法已启用
    device.set_fastinput_ime(False)
    # 发送文本
    device(text=hint).send_keys(text)


def swipe(device, start_x, start_y, end_x, end_y, duration=0.5):
    print('滑动屏幕:', start_x, start_y, end_x, end_y)
    device.swipe(start_x, start_y, end_x, end_y, duration)


def swipe_up(device, duration=0.5):
    print('向上滑动屏幕')
    device.swipe_ext("up", duration=duration)


def swipe_down(device, duration=0.5):
    print('向下滑动屏幕')
    device.swipe_ext("down", duration=duration)


def swipe_left(device, duration=0.5):
    print('向左滑动屏幕')
    device.swipe_ext("left", duration=duration)


def swipe_right(device, duration=0.5):
    print('向右滑动屏幕')
    device.swipe_ext("right", duration=duration)


def swipe_relative_view_up(device, view, duration=0.5):
    print('相对view滑动屏幕:', view)
    view.swipe("up", duration=duration)


def swipe_relative_view_down(device, view, duration=0.5):
    print('相对view滑动屏幕:', view)
    view.swipe("down", duration=duration)


def exists_by_text(device, text):
    b = device.exists(text=text)
    print('是否存在:', text, b)
    return b


def quite(device):
    print('退出')
    time.sleep(3)
    device.stop_uiautomator()
    print('退出完毕')
