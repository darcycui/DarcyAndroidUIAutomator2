Write-Host "test start..."
Write-Host "汉字打印..."
$outPath="D:\bbb\Telegram\2025-07-18-09_37_07"
# & "D:\bbb\Telegram\TGPASS-testlog.exe" $outPath
Start-Process -FilePath "D:\bbb\Telegram\TGPASS.exe" -ArgumentList $outPath

$alias = "log-new-1"
$parts = $alias -split "-"
$alias_prefix = $parts[0]
Write-Host "alias_prefix: $alias_prefix"
$alias_suffix = $parts[1]
Write-Host "alias_suffix: $alias_suffix"
