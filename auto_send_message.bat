@echo off
chcp 65001
cd D:\Projectss\Python\WebClickProject\AndroidUiAutomator2Project
D:
echo 检测到当前目录为：%cd%
echo send_message start...
timeout /t 10 >nul
call python .\send_message.py
echo send_message finish！
pause