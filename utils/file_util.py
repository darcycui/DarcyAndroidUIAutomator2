import os
import re
from typing import Optional


def write_string_to_file(file_path: str, text: str):
    # 覆盖方式写入文件
    file = open(file_path, 'w')
    file.write(text + '\n')
    file.close()


def write_map_to_file(file_path: str, map_: dict[str, str]):
    # 追加方式写入文件
    file = open(file_path, 'a')
    for key in map_:
        file.write(key + '=' + map_[key] + '\n')
    file.close()


def get_latest_file_in_folder(folder_path: str) -> Optional[str]:
    # 获取文件夹下版本号最大的文件  版本号格式4.2.0  4.2.1  4.2.2

    # 获取文件夹中所有文件
    files = [f for f in os.listdir(folder_path)
             if os.path.isfile(os.path.join(folder_path, f))]

    if not files:
        return None

    latest_file = None
    latest_version = (0, 0, 0)  # 初始版本号

    # 正则表达式匹配版本号格式 x.y.z
    version_pattern = re.compile(r'(\d+)\.(\d+)\.(\d+)')

    for file in files:
        # 尝试从文件名中提取版本号
        match = version_pattern.search(file)
        if match:
            # 将版本号转换为整数元组以便比较
            version = tuple(map(int, match.groups()))

            # 比较版本号
            if version > latest_version:
                latest_version = version
                latest_file = file

    # 返回完整文件路径
    return os.path.join(folder_path, latest_file) if latest_file else None


def check_file_exists(file_path: str) -> bool:
    if file_path is None or file_path == '':
        return False
    return os.path.exists(file_path)


def create_folders(folder_path: str) -> bool:
    if not os.path.exists(folder_path):
        os.makedirs(folder_path, exist_ok=True)
        return True
    return True
