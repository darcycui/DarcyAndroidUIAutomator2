import time


def get_current_time():
    # 格式化时间戳
    return time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))