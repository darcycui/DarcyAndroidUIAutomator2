import string
import sys
from datetime import datetime

from utils.date_time_util import delay
from utils.uiautomator2.view_click import click_view_by_id
from utils.uiautomator2.apps import start_app, stop_app
from utils.uiautomator2.connect import connect_device, quite
from utils.uiautomator2.device import turn_screen_on, turn_screen_off
from utils.file_util import write_map_to_file
from utils.uiautomator2.view_get import get_view_by_class_name, get_view_by_id
from utils.uiautomator2.press_key import press_back
from utils.uiautomator2.screenshot import screen_shot
from utils.uiautomator2.view_info import get_view_info, get_view_text
from utils.uiautomator2.view_wait import wait_view_appear_by_view_id

device_id_samsang = 'RFCW8014R4E'
package_name = 'com.kugou.android.lite'
if __name__ == '__main__':
    try:
        print('vip start')
        # 开始录屏
        # record_process = screen_record_start('checkin_vip', device_id_samsang)
        # 连接设备
        d = connect_device(device_id_samsang)
        # 亮屏
        turn_screen_on(d)
        # 先结束app
        stop_app(d, package_name)
        # click_button_by_text(d, '酷狗概念版')
        # 再启动app
        start_app(d, package_name)
        # 首页播放按钮
        click_view_by_id(d, package_name + ':id/eu0')
        # 播放页播放按钮 开始播放
        click_view_by_id(d, package_name + ':id/ezj')
        delay(6)
        # 播放页播放按钮 暂停播放
        click_view_by_id(d, package_name + ':id/ezj')
        # 结束录屏
        # screen_record_stop(record_process)
        # 返回上一页
        press_back(d)
        # 点击我的按钮
        click_view_by_id(d, package_name + ':id/ett')
        # 点击会员中心图标
        click_view_by_id(d, package_name + ':id/a9f')
        # 获取有效期区域元素 tabVIP
        tab_vip = get_view_by_id(d, 'tabVIP')
        # 等待tabVIP元素加载完成
        wait_view_appear_by_view_id(d, 'tabVIP')
        # 截图
        screen_shot(d, 'checkin_vip', 10)
        # 获取有效期区域子元素
        get_view_info(tab_vip)
        # 得到所有TextView
        no_view = get_view_by_class_name(d, 'android.widget.TextView', 1)
        date_view = get_view_by_class_name(d, 'android.widget.TextView', 2)
        # 创建映射
        text_map = {'vip_no': get_view_text(no_view), 'vip_date': get_view_text(date_view)}
        # 打印会员id和有效期
        print('会员编号:', text_map['vip_no'])
        original_string: string = text_map['vip_date']
        vip_date_string: string = original_string.split(' ')[-1]
        vip_date: datetime = datetime.strptime(vip_date_string, '%Y-%m-%d')
        current_date: datetime = datetime.now()
        if vip_date >= current_date:
            period = (vip_date - current_date).days
            print(f"会员有效期: {vip_date.strftime('%Y-%m-%d')} 还剩余 {period} 天")
        else:
            print("*************************会员已过期*************************")
        # 将 text_map 写入文件
        write_map_to_file('log/vip_info.txt', text_map)
        # 退出
        quite(d)
        # 息屏
        turn_screen_off(d)
        print('++++++++++++++++++++ 今日vip签到: 成功 ++++++++++++++++++++')
    except Exception as e:
        print(f'-------------------- 今日vip签到: 失败 {e} --------------------')
        sys.exit(-1)
