from uiautomator2 import Device


def push_file_to_device(device: Device, local_file_path: str, remote_file_path: str):
    print(f'推送文件: {local_file_path} 到 {remote_file_path}')
    device.push(local_file_path, remote_file_path)
