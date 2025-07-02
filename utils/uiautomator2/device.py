import uiautomator2 as u2


def unlock_screen(device: u2.Device):
    print('解锁屏幕')
    device.unlock()


def lock_screen(device: u2.Device):
    print('锁屏')
    device.screen_off()


def turn_screen_on(device: u2.Device):
    print('屏幕点亮')
    device.screen_on()


def turn_screen_off(device: u2.Device):
    print('屏幕熄灭')
    device.screen_off()
