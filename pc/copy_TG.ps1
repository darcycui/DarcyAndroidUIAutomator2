# chcp 65001
$OutputEncoding = [System.Text.Encoding]::UTF8
# 获取系统时间
$date = Get-Date -Format "yyyy-MM-dd-HH_mm_ss"

# 创建文件夹
$outPath = "D:\bbb\Telegram\$date"
Write-Host "导出TG文件到目标文件夹: $outPath"
$device = "RFCW8014R4E"
# $device = "OBTWQSGYTCCA9PT4"
# $device = "NAB0220416042561"
# $device = "988995324c4a494f46"

adb devices
Write-Host "device==> $device"
# 执行 adb devices 并获取输出
$adbDevicesOutput = adb devices

# 检查输出中是否包含目标设备 RFCW8014R4E
if ($adbDevicesOutput -match "RFCW8014R4E\s+device") {
    Write-Host "设备 RFCW8014R4E 已找到，继续执行脚本..."
} else {
    Write-Host "设备 RFCW8014R4E 未找到，退出脚本。"
}

# adb connect $device
# try-catch
try {
    
    Write-Host "新建文件夹: $outPath"
    New-Item -ItemType Directory -Path $outPath
    # 输出文件夹
    # 图片 视频 文件
    $filePath = "/sdcard/Android/data/org.telegram.messenger/cache"
    adb -s $device pull $filePath $outPath
    # 列出文件夹中的所有文件
    $files = Get-ChildItem -Path $outPath\cache -File

    # 筛选出文件名以 "5_" 开头且不是 ".tgv" 扩展名 或者 后缀是.ogg的文件
    $filteredFiles = $files | Where-Object {
        ($_.Name.StartsWith("5_") -and $_.Extension -ne ".tgv") -or ($_.Extension -eq ".ogg")
    }
    $filteredFiles | Format-Table -Property Name, FullName
    # 移动filteredFiles中的文件到 $outPath
    foreach ($file in $filteredFiles) {
        Move-Item -Path $file.FullName -Destination $outPath -Force
    }
    # 删除cache文件夹
    Remove-Item -Path "$outPath/cache" -Recurse -Force

    # 录音
    $audioPath = "/sdcard/Android/data/org.telegram.messenger/files/Telegram/Telegram Audio"
    adb -s $device pull $audioPath $outPath
    # 移动Telegram Audio文件夹下的文件到 $outPath
    Move-Item -Path "$outPath/Telegram Audio/*.ogg" -Destination $outPath -Force
    # 删除Telegram Audio文件夹
    Remove-Item -Path "$outPath/Telegram Audio" -Recurse -Force

    
    Write-Host "导出结束:请到$outPath 文件夹查看."
    # 打开输出文件夹
    explorer $outPath
    # 等待3秒
    Start-Sleep -Seconds 3
    # 启动PC exe 阻塞
    # & "D:\bbb\Telegram\TGPASS-testlog.exe" "$outPath"
    # 启动PC exe 不阻塞
    Start-Process -FilePath "D:\bbb\Telegram\TGPASS-testlog.exe" -ArgumentList $outPath
    # 复制outPath到剪贴板(避免多余 BOM 0xfeff)
    Set-Clipboard -Value $outPath
}
catch {
    # 异常代码行号
    $line = $_.InvocationInfo.ScriptLineNumber
    Write-Error "导出错误 Error: $_ at line $line"
}