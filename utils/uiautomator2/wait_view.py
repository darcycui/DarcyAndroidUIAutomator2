import uiautomator2 as u2

from utils.uiautomator2.get_view import get_view_by_id, get_view_by_text_contains
from utils.uiautomator2.view_info import get_view_text


def wait_view_text_by_id2(device: u2.Device, view_id: str, timeout=10) -> str | None:
    print('等待元素出现2:', view_id)
    target_view = get_view_by_id(device, view_id)
    b: bool = target_view.exists(timeout=timeout)
    return get_view_text_or_none(b, target_view)


def wait_view_text_by_id(device: u2.Device, view_id: str, timeout=10) -> str | None:
    print('等待元素出现:', view_id)
    target_view = get_view_by_id(device, view_id)
    b: bool = target_view.wait(timeout=timeout)
    return get_view_text_or_none(b, target_view)

def wait_view_text_by_text(device: u2.Device, text: str, timeout=10) -> str | None:
    print('等待元素出现:', text)
    target_view = get_view_by_text_contains(device, text)
    b: bool = target_view.wait(timeout=timeout)
    return get_view_text_or_none(b, target_view)


def get_view_text_or_none(b, target_view):
    print('是否存在:', b)
    if b:
        return get_view_text(target_view)
    else:
        return None
