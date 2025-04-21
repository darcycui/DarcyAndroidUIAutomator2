import time

from date_util import get_current_time
from uiautomator2_util import start_app, connect_device, stop_app, click_button_by_text, click_button_by_class_name, \
    press_search, input_text, turn_screen_on, turn_screen_off, press_menu, get_view_by_class_name, \
    get_child_view_by_text, get_view_by_text, get_view_info, press_back

device_id_samsang = 'RFCW8014R4E'
package_name = 'org.telegram.messenger'


def start_chat(contact_name):
    # 定位左上角设置按钮
    press_menu(d)
    # 点击联系人按钮
    click_button_by_text(d, 'Contacts')
    # 点击搜索按钮
    press_search(d)
    click_button_by_class_name(d, 'android.widget.ImageButton')
    # 输入文本
    input_text(d, 'Search', contact_name)
    time.sleep(3)
    # 点击联系人5786 开始聊天
    click_button_by_class_name(d, 'android.widget.Switch')


def send_text_message(device, message_text):
    # 循环3次
    for i in range(3):
        time.sleep(3)
        # 输入文本
        # input_text(device, 'Message', message_text + ' ' + get_current_time())
        view = get_view_by_class_name(d, 'android.widget.EditText')
        view.send_keys(message_text + ' ' + get_current_time())
        time.sleep(3)
        # 点击发送按钮
        views = get_view_by_class_name(d, 'android.view.View')
        print('点击发送按钮')
        views[len(views) - 1].click()
        time.sleep(3)
    # 收起键盘
    # press_back(device)
    # time.sleep(3)


def send_image(d):
    print('send image')
    for i in range(1, 3):
        # 点击附件按钮
        views = get_view_by_class_name(d, 'android.widget.ImageView')
        print('点击附件按钮')
        views[len(views) - 1].click()
        time.sleep(3)
        # 选中图片
        views = get_view_by_class_name(d, 'android.widget.Switch')
        print('选中图片')
        views[i].click()
        time.sleep(1)
        # 点击发送按钮
        views = get_view_by_class_name(d, 'android.widget.ImageView')
        print('点击发送按钮')
        print(views)
        views[len(views) - 1].click()
        time.sleep(3)


def secret_chat_on_off(device):
    # 点击头像
    click_button_by_text(device, 'Ciii Home 5786')
    print('点击密聊开关')
    click_button_by_text(device, 'Secure')
    # 返回聊天页
    press_back(device)
    time.sleep(3)

if __name__ == '__main__':
    try:
        print('tg send message start')
        # 连接设备
        d = connect_device(device_id_samsang)
        # 亮屏
        turn_screen_on(d)
        # 结束应用
        stop_app(d, package_name)
        # 启动应用
        start_app(d, package_name)
        # 开始聊天
        start_chat('Ciii Home 5786')
        # 开启密聊
        secret_chat_on_off(d)
        # 发送文本消息
        send_text_message(d, 'On')
        # 收起键盘
        press_back(d)
        time.sleep(3)
        # 发送图片
        send_image(d)
        # 关闭密聊
        secret_chat_on_off(d)
        # 发送文本消息
        send_text_message(d, 'Off')
        # 收起键盘
        press_back(d)
        time.sleep(3)
        # 息屏
        # turn_screen_off(d)
        print('tg send message success')
    except Exception as e:
        print(f'tg send message failed:{e}')

