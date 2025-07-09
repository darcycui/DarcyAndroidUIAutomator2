import uiautomator2 as u2

from utils.uiautomator2.view_info import get_view_info


# 支持的查找方式:
# text, textContains, textMatches, textStartsWith
# className, classNameMatches
# description, descriptionContains, descriptionMatches, descriptionStartsWith
# checkable, checked, clickable, longClickable
# scrollable, enabled,focusable, focused, selected
# packageName, packageNameMatches
# resourceId, resourceIdMatches
# index, instance

def get_view_list_by_id(device: u2.Device, view_id: str) -> u2.UiObject:
    view = device(resourceId=view_id)
    return view


def get_view_list_by_text(device: u2.Device, text: str) -> u2.UiObject:
    view = device(text=text)
    # print('view的类型:', type(view))
    get_view_info(view)
    return view


def get_view_list_by_text_contains(device: u2.Device, text_contains: str) -> u2.UiObject:
    view = device(textContains=text_contains)
    return view


def get_view_list_by_text_match(device: u2.Device, text_match: str) -> u2.UiObject:
    """
    根据正则表达式查找目标元素
    :param device: 设备
    :param text_match: 正则表达式
    :param position: 多个元素命中 指定元素位置
    :return: 元素
    """
    view = device(textMatches=text_match)
    return view


def get_view_list_by_class_name(device: u2.Device, class_name: str) -> u2.UiObject:
    view = device(className=class_name)
    return view


def get_view_list_by_description(device: u2.Device, description: str) -> u2.UiObject:
    view = device(description=description)
    return view


def get_child_view_list_by_text(view, text: str) -> u2.UiObject:
    return view.child_by_text(text)


def get_child_view_list_by_class_name(view, class_name) -> u2.UiObject:
    return view.child(className=class_name)
