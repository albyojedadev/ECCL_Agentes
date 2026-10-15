#!/usr/bin/env bash
set -euo pipefail
if [[ $# -lt 1 ]]; then
  echo "Uso: ./scripts/install.sh /ruta/destino [--update]" >&2
  exit 2
fi
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
python3 -B "$SCRIPT_DIR/install.py" --target "$@"
