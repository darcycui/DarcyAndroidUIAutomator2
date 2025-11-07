@echo off
chcp 65001
cd D:\Projectss\Python\AndroidUiAutomator2Project
D:
echo 检测到当前目录为：%cd%
echo send_message_signal 开始...
timeout /t 10 >nul
call python .\send_message_signal.py
echo send_message_signal 结束！
pause