import re

def split_verification_code(message: str) -> str:
    match = re.search(r"Login code:\s*([0-9]+)\.", message)
    if match:
        return match.group(1)
    else:
        raise ValueError("验证码不匹配 获取验证码失败！")
