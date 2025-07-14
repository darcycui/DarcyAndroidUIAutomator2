import uiautomator2 as u2


def get_view_up_by_class_name(from_view: u2.UiObject, class_name: str) -> u2.UiObject:
    return from_view.up(className=class_name)


def get_view_down_by_class_name(from_view: u2.UiObject, class_name: str) -> u2.UiObject:
    return from_view.down(className=class_name)


def get_view_left_by_class_name(from_view: u2.UiObject, class_name: str) -> u2.UiObject:
    return from_view.left(className=class_name)


def get_view_right_by_class_name(from_view: u2.UiObject, class_name: str) -> u2.UiObject:
    return from_view.right(className=class_name)
