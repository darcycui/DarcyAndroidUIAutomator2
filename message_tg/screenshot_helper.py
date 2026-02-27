import uiautomator2 as u2

from utils.date_time_util import get_current_day
from utils.uiautomator2.screenshot import screen_shot


def tg_inspection_screenshot(device: u2.Device):
    current_day = get_current_day()
    screen_shot(device, f'tg_{current_day}', 'inspection', 0)
