import uiautomator2 as u2
from uiautomator2.utils import Exists


def exists_by_id(device: u2.Device, view_id: str) -> bool:
    b: Exists = device.exists(resourceId=view_id)
    print(f'是否存在 {view_id} : {b}')
    return bool(b)


def exists_by_text(device: u2.Device, text: str) -> bool:
    b: Exists = device.exists(text=text)
    print(f'是否存在 {text} : {b}')
    return bool(b)


def exists_by_text_contains(device: u2.Device, text: str) -> bool:
    b: Exists = device.exists(textContains=text)
    print(f'是否存在 {text} : {b}')
    return bool(b)


def exists_by_description(device: u2.Device, description: str) -> bool:
    b: Exists = device.exists(description=description)
    print(f'是否存在 {description} : {b}')
    return bool(b)

def exists_by_class_name(device: u2.Device, class_name: str) -> bool:
    b: Exists = device.exists(className=class_name)
    print(f'是否存在 {class_name} : {b}')
    return bool(b)

def exist_by_view_id(device: u2.Device, view_id: str) -> bool:
    b: Exists = device.exists(resourceId=view_id)
    print(f'是否存在 {view_id} : {b}')
    return bool(b)
