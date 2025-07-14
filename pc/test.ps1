Write-Host "test start..."
Write-Host "汉字打印..."
$alias = "log-new-1"
$parts = $alias -split "-"
$alias_prefix = $parts[0]
Write-Host "alias_prefix: $alias_prefix"
$alias_suffix = $parts[1]
Write-Host "alias_suffix: $alias_suffix"
