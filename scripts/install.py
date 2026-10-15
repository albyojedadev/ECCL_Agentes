"""Valida y copia el paquete a destino explícito; no configura servicios globales."""
from pathlib import Path
import argparse,hashlib,json,shutil,subprocess,sys
REPO=Path(__file__).resolve().parents[1]
EXCLUDE={'.git','__pycache__','.pytest_cache','dist','scratch','tmp','.eccl-installed'}
def package_files(base):
    return sorted(p for p in base.rglob('*') if p.is_file() and not EXCLUDE.intersection(p.relative_to(base).parts))
def install(source,target,update=False):
    source=source.resolve();target=target.resolve()
    if target==source or target.is_relative_to(source) or source.is_relative_to(target):raise ValueError('Destino debe estar separado del repositorio fuente')
    if target.exists() and any(target.iterdir()) and not update:raise ValueError('Destino no vacío; usa --update para actualizar ECCL')
    if target.exists() and any(target.iterdir()) and not (target/'plugin.json').is_file():raise ValueError('No actualizar una carpeta ajena a ECCL')
    subprocess.run([sys.executable,'-B',str(source/'scripts/verify_installation.py')],check=True)
    target.mkdir(parents=True,exist_ok=True);files=package_files(source)
    for p in files:
        dest=target/p.relative_to(source);dest.parent.mkdir(parents=True,exist_ok=True);shutil.copyfile(p,dest)
    for p in files:
        dest=target/p.relative_to(source)
        if hashlib.sha256(p.read_bytes()).digest()!=hashlib.sha256(dest.read_bytes()).digest():raise ValueError(f'Copia distinta: {dest}')
    subprocess.run([sys.executable,'-B',str(target/'scripts/verify_installation.py')],check=True)
    receipt={'source':str(source),'target':str(target),'version':json.loads((target/'plugin.json').read_text(encoding='utf-8-sig'))['version'],'archivos_verificados':len(files),'alcance':'copia/carga_contexto; no inferencia de modelo'}
    (target/'installation_receipt.json').write_text(json.dumps(receipt,ensure_ascii=False,indent=2),encoding='utf-8')
    return receipt
def main():
    p=argparse.ArgumentParser();p.add_argument('--target',type=Path,required=True);p.add_argument('--update',action='store_true');a=p.parse_args()
    try:print(json.dumps(install(REPO,a.target,a.update),ensure_ascii=False,indent=2))
    except (ValueError,OSError,subprocess.CalledProcessError) as e:p.exit(1,str(e)+'\n')
if __name__=='__main__':main()
