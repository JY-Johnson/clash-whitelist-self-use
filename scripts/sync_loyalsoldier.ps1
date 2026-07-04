param(
  [string]$OutputDir = ".\\public\\rules\\loyalsoldier"
)

$ErrorActionPreference = "Stop"

$sources = @{
  "applications.txt" = "https://raw.githubusercontent.com/Loyalsoldier/clash-rules/release/applications.txt"
  "private.txt"      = "https://raw.githubusercontent.com/Loyalsoldier/clash-rules/release/private.txt"
  "direct.txt"       = "https://raw.githubusercontent.com/Loyalsoldier/clash-rules/release/direct.txt"
  "lancidr.txt"      = "https://raw.githubusercontent.com/Loyalsoldier/clash-rules/release/lancidr.txt"
  "cncidr.txt"       = "https://raw.githubusercontent.com/Loyalsoldier/clash-rules/release/cncidr.txt"
}

New-Item -ItemType Directory -Force -Path $OutputDir | Out-Null

foreach ($name in $sources.Keys) {
  $target = Join-Path $OutputDir $name
  Invoke-WebRequest -Uri $sources[$name] -OutFile $target
  Write-Output "synced $name"
}

