def write_string_to_file(file_path, string):
    # 覆盖方式写入文件
    file = open(file_path, 'w')
    file.write(string + '\n')
    file.close()


def write_map_to_file(file_path, map_):
    # 追加方式写入文件
    file = open(file_path, 'a')
    for key in map_:
        file.write(key + '=' + map_[key] + '\n')
    file.close()
