import uiautomator2 as u2


# {
#     "contentDescription": "",
#     "checked": false,
#     "scrollable": false,
#     "text": "Settings",
#     "packageName": "com.android.launcher",
#     "selected": false,
#     "enabled": true,
#     "bounds": {
#         "top": 385,
#         "right": 360,
#         "bottom": 585,
#         "left": 200
#     },
#     "className": "android.widget.TextView",
#     "focused": false,
#     "focusable": true,
#     "clickable": true,
#     "childCount": 0,
#     "longClickable": true,
#     "visibleBounds": {
#         "top": 385,
#         "right": 360,
#         "bottom": 585,
#         "left": 200
#     },
#     "checkable": false
# }
def get_view_info(view: u2.UiObject) -> dict:
    if view is None:
        print('元素不存在')
        return {}
    info = view.info
    print('元素信息:', info)
    return info


def get_view_text(view: u2.UiObject) -> str:
    text = get_view_info(view)['text']
    print('获取元素文本:', text)
    return text


def get_view_description(view: u2.UiObject) -> str:
    description = get_view_info(view)['contentDescription']
    print('获取元素描述:', description)
    return description


def get_view_package_name(view: u2.UiObject) -> str:
    package_name = get_view_info(view)['packageName']
    print('获取元素包名:', package_name)
    return package_name


def get_view_class_name(view: u2.UiObject) -> str:
    class_name = get_view_info(view)['className']
    print('获取元素类名:', class_name)
    return class_name


def is_view_checked(view: u2.UiObject) -> bool:
    checked = get_view_info(view)['checked']
    print('获取元素是否选中:', checked)
    return checked


def is_view_selected(view: u2.UiObject) -> bool:
    selected = get_view_info(view)['selected']
    print('获取元素是否被选中:', selected)
    return selected


def get_view_center_x(view: u2.UiObject):
    bounds: dict = get_view_info(view)['bounds']
    start_x = bounds['left']
    end_x = bounds['right']
    return int((start_x + end_x) / 2)


def get_view_center_y(view: u2.UiObject):
    bounds: dict = get_view_info(view)['bounds']
    start_y = bounds['top']
    end_y = bounds['bottom']
    return int((start_y + end_y) / 2)
