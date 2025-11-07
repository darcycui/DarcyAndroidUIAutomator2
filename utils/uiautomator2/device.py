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


def get_device_info(device: u2.Device) -> dict:
    return device.info


def get_device_name(device: u2.Device) -> str:
    info_map = get_device_info(device)
    return f'设备名称: {info_map['productName']}'


def get_device_sdk(device: u2.Device) -> int:
    return int(get_device_info(device)['sdkInt'])
