from utils.uiautomator2.get_view import get_view_by_class_name, get_view_by_description
from utils.date_time_util import get_current_time, delay


def send_text_message(device, message_text):
    # 循环3次
    for i in range(3):
        delay(3)
        # 输入文本
        # input_text(device, 'Message', message_text + ' ' + get_current_time())
        view = get_view_by_class_name(device, 'android.widget.EditText')
        view.send_keys(message_text + ' ' + get_current_time())
        delay(3)
        # 点击发送按钮
        views = get_view_by_description(device, 'Send')
        print('点击发送按钮')
        views[len(views) - 1].click()
        delay(3)
    # 收起键盘
    # press_back(device)
    # delay(3)


def send_image(device):
    print('send image')
    for i in range(1, 3):
        # 点击附件按钮
        views = get_view_by_class_name(device, 'android.widget.ImageView')
        print('点击附件按钮')
        views[len(views) - 1].click()
        delay(3)
        # 选中图片
        views = get_view_by_class_name(device, 'android.widget.Switch')
        print('选中图片')
        views[i].click()
        delay(1)
        # 点击发送按钮
        views = get_view_by_class_name(device, 'android.widget.ImageView')
        print('点击发送按钮')
        print(views)
        views[len(views) - 1].click()
        delay(3)
