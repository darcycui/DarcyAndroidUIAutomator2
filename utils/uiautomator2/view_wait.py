import uiautomator2 as u2

from utils.uiautomator2.view_get import get_view_by_id, get_view_by_text_contains, get_view_by_text
from utils.uiautomator2.view_info import get_view_text
from utils.uiautomator2.view_list_get import get_view_list_by_text_contains


def wait_view_appear_by_text(device: u2.Device, text: str, timeout=120) -> bool:
    print('等待元素出现:', text)
    b = device(textContains=text).wait(timeout=timeout)
    print(f'是否存在 {text}:', b)
    return b


def wait_view_gone_by_text(device: u2.Device, text: str, timeout=120) -> bool:
    print('等待元素消失:', text)
    b = device(textContains=text).wait(exists=False, timeout=timeout)
    print(f'是否存在 {text}:', b)
    return b


def wait_view_appear_by_class_name(device: u2.Device, class_name: str, position: int, timeout=120) -> bool:
    print('等待元素消失:', class_name)
    b = device(className=class_name, instance=position).wait(exists=False, timeout=timeout)
    print(f'是否存在 {class_name}:', b)
    return b

def wait_view_appear_by_view_id(device: u2.Device, view_id: str, timeout=120) -> bool:
    print('等待元素出现:', view_id)
    b = device(resourceId=view_id).wait(timeout=timeout)
    print(f'是否存在 {view_id}:', b)
    return b


def wait_view_gone_by_view_id(device: u2.Device, text: str, timeout=120) -> bool:
    print('等待元素消失:', text)
    b = device(resourceId=text).wait(exists=False, timeout=timeout)
    print(f'是否存在 {text}:', b)
    return b
