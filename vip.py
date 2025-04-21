from file_util import write_map_to_file
from uiautomator2_util import *

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
        click_button_by_id(d, package_name + ':id/eu0')
        # 播放页播放按钮 开始播放
        click_button_by_id(d, package_name + ':id/ezj')
        time.sleep(6)
        # 播放页播放按钮 暂停播放
        click_button_by_id(d, package_name + ':id/ezj')
        # 结束录屏
        # screen_record_stop(record_process)
        # 返回上一页
        press_back(d)
        # 点击我的按钮
        click_button_by_id(d, package_name + ':id/ett')
        # 点击会员中心图标
        click_button_by_id(d, package_name + ':id/a9f')
        # 截图
        screen_shot(d, 'checkin_vip', 10)
        # 获取有效期
        tab_vip = get_view_by_id(d, 'tabVIP')
        get_view_info(tab_vip)
        # 得到所有TextView
        text_views = get_view_by_class_name(d, 'android.widget.TextView')
        # 创建映射
        text_map = {}

        # for循环遍历
        for i in range(len(text_views)):
            # print('i=', i)
            if i == 1:
                text = get_view_info(text_views[i])
                text_map['vip_no'] = text['text']
            if i == 2:
                date = get_view_info(text_views[i])
                text_map['vip_date'] = date['text']
        # 将 text_map 写入文件
        write_map_to_file('log/vip_info.txt', text_map)
        # 退出
        quite(d)
        # 息屏
        turn_screen_off(d)
        print('++++++++++++++++++++vip success 成功++++++++++++++++++++')
    except Exception as e:
        print(f'--------------------vip failed: 失败 {e}--------------------')

