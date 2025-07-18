@echo off
chcp 65001
cd D:\Projectss\Python\AndroidUiAutomator2Project
D:
echo 检测到当前目录为：%cd%
echo vip start...
timeout /t 10 >nul
call python .\vip.py
echo vip finish！
pause