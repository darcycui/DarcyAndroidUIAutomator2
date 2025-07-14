import os
import subprocess


def call_pc_powershell(script_path):
    """执行 PowerShell 脚本"""
    # 检查脚本路径是否存在
    if not os.path.exists(script_path):
        print(f"脚本路径不存在：{script_path}")
        return False

    # 使用subprocess模块执行PowerShell脚本
    try:
        result = subprocess.run(['powershell', '-File', script_path], capture_output=True, text=True)
        # 输出结果
        if result.stdout:
            print("标准输出:\n", result.stdout)
        if result.stderr:
            print("标准错误:\n", result.stderr)
        return True
    except subprocess.CalledProcessError as e:
        print(f"powershell 脚本执行失败：{e.stderr}")
        return False


def call_pc_bat(script_path):
    """执行 bat 脚本"""
    # 检查脚本路径是否存在
    if not os.path.exists(script_path):
        print(f"脚本路径不存在：{script_path}")
        return False
    try:
        # 使用subprocess.run来执行BAT文件并捕获输出
        result = subprocess.run(script_path, capture_output=True, text=True, shell=True)

        # 输出结果
        if result.stdout:
            print("标准输出:\n", result.stdout)
        if result.stderr:
            print("标准错误:\n", result.stderr)
        return True
    except Exception as e:
        print(f"Bat 脚本执行失败: {e}")
        return False
