"""Las skills se mantienen; el generador antiguo destruía enriquecimientos."""
import subprocess,sys
from pathlib import Path
if __name__=='__main__':
    repo=Path(__file__).resolve().parents[1]
    print('No se sobrescriben skills: validación de documentos mantenidos.')
    sys.exit(subprocess.run([sys.executable,'-B',str(repo/'scripts/verify_installation.py')]).returncode)
