import uiautomator2 as u2


def swipe_duration(device: u2.Device, start_x: int, start_y: int, end_x: int, end_y: int, duration: float = 0.5):
    print('滑动屏幕:', start_x, start_y, end_x, end_y)
    device.swipe(start_x, start_y, end_x, end_y, duration=duration)


def swipe_steps(device: u2.Device, start_x: int, start_y: int, end_x: int, end_y: int, steps: int = 10):
    print('滑动屏幕:', start_x, start_y, end_x, end_y)
    device.swipe(start_x, start_y, end_x, end_y, steps=steps)


def swipe_up(device: u2.Device, duration: float = 0.5):
    print('向上滑动屏幕')
    device.swipe_ext("up", duration=duration)


def swipe_down(device: u2.Device, duration: float = 0.5):
    print('向下滑动屏幕')
    device.swipe_ext("down", duration=duration)


def swipe_left(device: u2.Device, duration: float = 0.5):
    print('向左滑动屏幕')
    device.swipe_ext("left", duration=duration)


def swipe_right(device: u2.Device, duration: float = 0.5):
    print('向右滑动屏幕')
    device.swipe_ext("right", duration=duration)


def swipe_relative_view_up(device, view: u2.UiObject, duration: float = 0.1):
    print('相对view滑动屏幕:', view)
    step_count = calculate_steps(duration)
    view.swipe("up", steps=step_count)


def swipe_relative_view_down(device: u2.Device, view: u2.UiObject, duration: float = 0.1):
    print('相对view滑动屏幕:', view)
    # 计算step数 一个step对应0.005秒滑动
    step_count = calculate_steps(duration)
    view.swipe("down", steps=step_count)


# 计算step数 一个step对应0.005秒滑动
def calculate_steps(duration):
    step_count = int(duration / 0.005)
    return step_count
