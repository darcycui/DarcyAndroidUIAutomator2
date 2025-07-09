import time
import uiautomator2 as u2

from utils.date_time_util import delay


def touch_down_x_y(device: u2.Device, x: int, y: int):
    print(f'touch DOWN 事件 x={x} y={y}')
    device.touch.down(x, y)


def touch_up_x_y(device: u2.Device, x: int, y: int):
    print(f'touch UP 事件 x={x} y={y}')
    device.touch.up(x, y)

def touch_move_x_y(device: u2.Device, x: int, y: int):
    print(f'touch MOVE 事件 x={x} y={y}')
    device.touch.move(x, y)

def touch_sleep(device: u2.Device, duration: float):
    print(f'touch SLEEP 事件 duration={duration}')
    device.sleep(duration)
