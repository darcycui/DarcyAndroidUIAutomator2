import uiautomator2 as u2

from utils.uiautomator2.connect import connect_device



if __name__ == '__main__':
    print('message_signal send message...')
    # try:
    #     print('发送消息 start+++')
    #     # 连接设备
    #     in_device: u2.Device = connect_device(DEVICE_ID_IN)
    #     out_device: u2.Device = connect_device(DEVICE_ID_OUT)
    #     print('---------------------------------------------登录:开始------------------------------------------------')
    #     # 登录准备
    #     prepare_login(in_device, PACKAGE_NAME)
    #     prepare_login(out_device, PACKAGE_NAME)
    #     # 登录
    #     login(in_device, PACKAGE_NAME, PACKAGE_NAME_WEB, PACKAGE_NAME_BETA, COUNTRY_NUMBER_IN, PHONE_NUMBER_IN)
    #     login(out_device, PACKAGE_NAME, PACKAGE_NAME_WEB, PACKAGE_NAME_BETA, COUNTRY_NUMBER_OUT, PHONE_NUMBER_OUT)
    #     print('---------------------------------------------登录:结束------------------------------------------------')
    #     delay(3)
    #     print('-------------------------------------------普通聊天:开始----------------------------------------------')
    #     # 聊天准备
    #     prepare(in_device, PACKAGE_NAME)
    #     prepare(out_device, PACKAGE_NAME)
    #     start_chat(in_device, CHAT_USER_NAME_IN)
    #     start_chat(out_device, CHAT_USER_NAME_OUT)
    #     # 清空历史
    #     clear_history(in_device)
    #     clear_history(out_device)
    #     # 聊天
    #     chat(in_device, out_device, 'Normal')
    #     delay(3)
    #     print('-------------------------------------------普通聊天:结束----------------------------------------------')
    #     delay(3)
    #     # 息屏
    #     # turn_screen_off(d)
    #     print('发送消息成功')
    # except Exception as e:
    #     print(f'发送消息失败:{e}')
    #     sys.exit(-1)
