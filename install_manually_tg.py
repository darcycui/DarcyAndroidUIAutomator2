from message_tg.config.global_config_tg import APKS_FOLDER_TG
from message_tg.tg_factory import get_user_in_tg, get_user_out_tg, get_user_out_huawei_tg
from utils.file_util import get_latest_file_in_folder
from utils.uiautomator2.connect import connect_device
from utils.uiautomator2.device import turn_screen_on
from utils.uiautomator2.install_apk import install_from_file_explorer
from utils.uiautomator2.push import push_file_to_device

if __name__ == '__main__':
    print('tg 安装apk开始+++')
    user_in = get_user_in_tg()
    user_out = get_user_out_tg()
    user_out_huawei = get_user_out_huawei_tg()

    apk_path = get_latest_file_in_folder(APKS_FOLDER_TG)
    apk_name = apk_path.split("\\")[-1]
    device_file_path = f"/sdcard/Documents/PTG/{apk_name}"
    print(f'apk_path: {apk_path}')
    print(f'apk_name: {apk_name}')

    device_in = connect_device(user_in.device_id)
    turn_screen_on(device_in)
    push_file_to_device(device_in, apk_path, device_file_path)
    install_from_file_explorer(device_in, user_in.file_explorer_package_name, user_in.file_explorer_text, apk_name)

    device_out = connect_device(user_out.device_id)
    turn_screen_on(device_out)
    push_file_to_device(device_out, apk_path, device_file_path)
    install_from_file_explorer(device_out, user_out.file_explorer_package_name, user_out.file_explorer_text, apk_name)

    device_out_huawei = connect_device(user_out_huawei.device_id)
    turn_screen_on(device_out_huawei)
    push_file_to_device(device_out_huawei, apk_path, device_file_path)
    install_from_file_explorer(device_out_huawei, user_out_huawei.file_explorer_package_name,
                               user_out_huawei.file_explorer_text, apk_name)
    print('tg 安装apk结束+++')
