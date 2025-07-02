import uiautomator2 as u2


def exists_by_text(device: u2.Device, text: str):
    b = device.exists(text=text)
    print('是否存在:', text, b)
    return b
