import time


def get_current_time() -> str:
    # 格式化时间戳
    return time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))


def delay(time_seconds: float) -> None:
    time.sleep(time_seconds)
