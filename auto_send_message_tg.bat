@echo off
chcp 65001
cd D:\Projectss\Python\AndroidUiAutomator2Project
D:
echo 检测到当前目录为：%cd%
echo send_message_tg 开始...
timeout /t 10 >nul
call python .\send_message_tg.py
:: echo install_manually 开始...
:: call python .\install_manually_tg.py
:: echo install_manually 结束...
echo send_message_tg 结束！
pause