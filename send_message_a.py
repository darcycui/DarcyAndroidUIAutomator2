import sys

from message.contact import start_chat
from message.login import login
from message.permission import grant_permissions
from message.secret_chat import secret_chat_on_off
from message.send import send_text_message, send_image
from utils.date_time_util import delay
from utils.uiautomator2.apps import stop_app, clear_app_data, start_app
from utils.uiautomator2.connect import connect_device
from utils.uiautomator2.device import turn_screen_on
from utils.uiautomator2.press_key import press_back, press_home

package_name = 'org.telegram.messenger'
package_name_web = 'org.telegram.messenger.web'

# device_id = 'RFCW8014R4E'
# country_number = '852'
# phone_number = '51617407'
# chat_user_name = 'Qiao LL'

device_id = 'OBTWQSGYTCCA9PT4'
country_number = '86'
phone_number = '19910358658'
chat_user_name = 'Ciii Home 7407'

if __name__ == '__main__':
    try:
        print('tg send message start')
        # 连接设备
        d = connect_device(device_id)

        # 亮屏
        turn_screen_on(d)
        # 按Home 键
        press_home(d)
        # 结束应用
        stop_app(d, package_name)
        # 清空应用数据
        clear_app_data(d, package_name)
        # 启动应用
        start_app(d, package_name)
        # 授权所有权限
        grant_permissions(d, package_name)

        # 登录
        login(d, package_name, package_name_web, country_number, phone_number)

        # 开始聊天
        start_chat(d, chat_user_name)
        # 开启密聊
        secret_chat_on_off(d)
        # 发送文本消息
        send_text_message(d, 'On')
        # 收起键盘
        press_back(d)
        delay(3)
        # 发送图片
        send_image(d)
        # 关闭密聊
        secret_chat_on_off(d)
        # 发送文本消息
        send_text_message(d, 'Off')
        # 收起键盘
        press_back(d)
        delay(3)
        # 息屏
        # turn_screen_off(d)
        print('send message success')
    except Exception as e:
        print(f'send message failed:{e}')
