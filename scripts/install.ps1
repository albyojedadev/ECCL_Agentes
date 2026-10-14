# ==============================================================================
# Instalador Automatizado de la Suite de Agentes ECCL para Windows (PowerShell)
# Escuela Canaria de Creación Literaria (ECCL)
# ==============================================================================

[CmdletBinding()]
param(
    [switch]$Force,
    [switch]$SkipCheck
)

$ErrorActionPreference = "Stop"

Write-Host "======================================================================" -ForegroundColor Cyan
Write-Host "  INSTALADOR DE LA SUITE DE AGENTES Y SKILLS ECCL" -ForegroundColor Yellow
Write-Host "  Escuela Canaria de Creación Literaria - 22 Años Formando Escritores" -ForegroundColor White
Write-Host "======================================================================" -ForegroundColor Cyan
Write-Host ""

$ScriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$RepoRoot = Split-Path -Parent $ScriptDir

# 1. Comprobar instalación de Python
Write-Host "[1/4] Comprobando entorno de Python..." -ForegroundColor Green
try {
    $pythonVer = python --version 2>&1
    Write-Host "      Detectado: $pythonVer" -ForegroundColor Gray
} catch {
    Write-Error "Python 3 no está disponible en el PATH. Por favor instala Python 3.8+ para ejecutar los linters."
}

# 2. Configuración del Plugin en Antigravity
Write-Host "[2/4] Vinculando plugin en Antigravity / Gemini..." -ForegroundColor Green
$PluginTargetDir = Join-Path $env:USERPROFILE ".gemini\config\plugins\eccl-agent-suite"

if (-not (Test-Path $PluginTargetDir)) {
    try {
        New-Item -ItemType SymbolicLink -Path $PluginTargetDir -Target $RepoRoot -Force | Out-Null
        Write-Host "      Enlace simbólico creado con éxito en: $PluginTargetDir" -ForegroundColor Gray
    } catch {
        Write-Host "      No se pudo crear symlink directo (permisos estándar). Copiando manifiesto de vinculación..." -ForegroundColor Yellow
        New-Item -ItemType Directory -Path $PluginTargetDir -Force | Out-Null
        Copy-Item -Path (Join-Path $RepoRoot "plugin.json") -Destination $PluginTargetDir -Force
        Copy-Item -Path (Join-Path $RepoRoot "agents") -Destination $PluginTargetDir -Recurse -Force
        Copy-Item -Path (Join-Path $RepoRoot "skills") -Destination $PluginTargetDir -Recurse -Force
        Copy-Item -Path (Join-Path $RepoRoot "knowledge") -Destination $PluginTargetDir -Recurse -Force
        Copy-Item -Path (Join-Path $RepoRoot "protocols") -Destination $PluginTargetDir -Recurse -Force
        Copy-Item -Path (Join-Path $RepoRoot "evals") -Destination $PluginTargetDir -Recurse -Force
        Write-Host "      Archivos desplegados en: $PluginTargetDir" -ForegroundColor Gray
    }
} else {
    Write-Host "      El plugin ya se encuentra vinculado en: $PluginTargetDir" -ForegroundColor Gray
}

# 3. Comprobación de Salud Pre-Vuelo
Write-Host "[3/4] Ejecutando verificación de componentes y linters de calidad..." -ForegroundColor Green
$VerifyScript = Join-Path $RepoRoot "scripts\verify_installation.py"
python $VerifyScript
if ($LASTEXITCODE -ne 0) {
    Write-Error "La verificación de salud falló. Por favor revisa los mensajes anteriores."
}

# 4. Finalización y Mensaje de Bienvenida
Write-Host ""
Write-Host "======================================================================" -ForegroundColor Green
Write-Host "  ¡INSTALACIÓN COMPLETADA CON ÉXITO!" -ForegroundColor Yellow
Write-Host "======================================================================" -ForegroundColor Green
Write-Host ""
Write-Host "  Componentes activos:" -ForegroundColor White
Write-Host "    - 17 Asistentes especializados en 'agents/'" -ForegroundColor Gray
Write-Host "    - 24 Skills modulares en 'skills/'" -ForegroundColor Gray
Write-Host "    - 6 Protocolos operativos (SOPs) en 'protocols/'" -ForegroundColor Gray
Write-Host "    - Corpus canónico verificado en 'knowledge/'" -ForegroundColor Gray
Write-Host ""
Write-Host "  Para comenzar a interactuar, puedes invocar al coordinador central:" -ForegroundColor White
Write-Host "    @coordinador-de-agentes-de-la-eccl" -ForegroundColor Cyan
Write-Host ""
