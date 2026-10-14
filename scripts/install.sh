#!/usr/bin/env bash
# ==============================================================================
# Instalador Automatizado de la Suite de Agentes ECCL para Linux y macOS
# Escuela Canaria de Creación Literaria (ECCL)
# ==============================================================================

set -e

echo "======================================================================"
echo "  INSTALADOR DE LA SUITE DE AGENTES Y SKILLS ECCL"
echo "  Escuela Canaria de Creación Literaria - 22 Años Formando Escritores"
echo "======================================================================"
echo ""

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(dirname "$SCRIPT_DIR")"

# 1. Comprobar instalación de Python
echo "[1/4] Comprobando entorno de Python..."
if ! command -v python3 &> /dev/null; then
    echo "Error: Python 3 no está instalado. Instala Python 3.8+ para continuar."
    exit 1
fi
echo "      Detectado: $(python3 --version)"

# 2. Configuración del Plugin en Antigravity / Gemini
echo "[2/4] Vinculando plugin en Antigravity..."
PLUGIN_TARGET_DIR="$HOME/.gemini/config/plugins/eccl-agent-suite"
mkdir -p "$HOME/.gemini/config/plugins"

if [ ! -e "$PLUGIN_TARGET_DIR" ]; then
    ln -s "$REPO_ROOT" "$PLUGIN_TARGET_DIR" 2>/dev/null || {
        echo "      Copiando archivos al directorio de plugins..."
        cp -r "$REPO_ROOT" "$PLUGIN_TARGET_DIR"
    }
    echo "      Plugin vinculado con éxito en: $PLUGIN_TARGET_DIR"
else
    echo "      El plugin ya se encuentra vinculado en: $PLUGIN_TARGET_DIR"
fi

# 3. Comprobación de Salud Pre-Vuelo
echo "[3/4] Ejecutando verificación de componentes y linters de calidad..."
python3 "$REPO_ROOT/scripts/verify_installation.py"

# 4. Finalización y Mensaje de Bienvenida
echo ""
echo "======================================================================"
echo "  ¡INSTALACIÓN COMPLETADA CON ÉXITO!"
echo "======================================================================"
echo ""
echo "  Componentes activos:"
echo "    - 17 Asistentes especializados en 'agents/'"
echo "    - 24 Skills modulares en 'skills/'"
echo "    - 6 Protocolos operativos (SOPs) en 'protocols/'"
echo "    - Corpus canónico verificado en 'knowledge/'"
echo ""
echo "  Para comenzar a interactuar, invoca al coordinador central:"
echo "    @coordinador-de-agentes-de-la-eccl"
echo ""
