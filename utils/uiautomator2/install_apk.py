import sys
import time

import uiautomator2 as u2

from utils.uiautomator2.apps import start_app, stop_app
from utils.uiautomator2.device import get_device_name
from utils.uiautomator2.screenshot import screen_shot
from utils.uiautomator2.view_click import click_view_by_text
from utils.uiautomator2.view_exists import exists_by_text, exists_by_id


def install_apk(device: u2.Device, apk_path: str):
    print(f'安装apk: {apk_path}')
    device.app_install(apk_path)


def uninstall_apk(device: u2.Device, package_name: str):
    print(f'卸载apk: {package_name}')
    device.app_uninstall(package_name)


def install_from_file_explorer(
        device: u2.Device,
        file_explorer_package_name: str,
        file_explorer_text: str,
        apk_name: str
) -> bool:
    print(f'从文件浏览器安装apk开始: {apk_name}')
    stop_app(device, file_explorer_package_name)
    time.sleep(1)
    start_app(device, file_explorer_package_name)
    time.sleep(1)
    click_view_by_text(device, file_explorer_text)
    click_view_by_text(device, 'Documents')
    click_view_by_text(device, 'PTG')
    click_view_by_text(device, apk_name)
    time.sleep(1)
    if exists_by_text(device, '继续安装'):
        click_view_by_text(device, '继续安装')
    if exists_by_text(device, '始终'):
        click_view_by_text(device, '始终')
    time.sleep(10)
    if exists_by_text(device, '继续安装') or exists_by_text(device, '不建议安装此应用；若仍需安装，可查看详情'):
        print(f'OPPO手机 从文件浏览器安装apk成功: {apk_name}')
        click_view_by_text(device, '取消安装')
        return True
    elif exists_by_text(device, '了解风险'):
        print(f'HuaWei手机 从文件浏览器安装apk成功: {apk_name}')
        click_view_by_text(device, '取消')
        return True
    elif exists_by_id(device, 'android:id/button1'):
        print(f'三星手机 从文件浏览器安装apk成功: {apk_name}')
        click_view_by_text(device, '取消')
        return True
    else:
        device_name = get_device_name(device)
        print(f'从文件浏览器安装apk失败: {device_name} {apk_name}')
        folder = APK_INSTALL_FAIL_FOLDER
        file = f'{folder}/{device_name}_{apk_name}_install_fail.png'
        screen_shot(device, 'install_from_file_explorer_fail', 3)
        sys.exit(-1)
