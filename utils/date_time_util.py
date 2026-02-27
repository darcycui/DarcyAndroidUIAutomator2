import time


def get_current_time(format_str: str = '%Y-%m-%d %H:%M:%S') -> str:
    # 格式化时间戳
    return time.strftime(format_str, time.localtime(time.time()))

def get_current_day(format_str: str = '%Y-%m-%d') -> str:
    return time.strftime(format_str, time.localtime(time.time()))

def delay(time_seconds: float) -> None:
    time.sleep(time_seconds)
