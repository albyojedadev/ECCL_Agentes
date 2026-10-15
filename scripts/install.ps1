[CmdletBinding()]
param(
    [Parameter(Mandatory=$true)][string]$TargetPath,
    [switch]$Update
)
$ErrorActionPreference = "Stop"
$Installer = Join-Path $PSScriptRoot "install.py"
$InstallArgs = @("-B", $Installer, "--target", $TargetPath)
if ($Update) { $InstallArgs += "--update" }
& python @InstallArgs
if ($LASTEXITCODE -ne 0) { throw "La copia o su validación ha fallado." }
Write-Host "Paquete copiado y comprobado. Consulte docs/INSTALACION.md."
