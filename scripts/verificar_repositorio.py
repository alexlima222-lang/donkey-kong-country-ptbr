#!/usr/bin/env python3
"""Confere patches, hashes e ausência de arquivos privados antes da publicação."""
from pathlib import Path
import hashlib
import json
from patch_io import records


def main():
    root = Path(__file__).resolve().parent.parent
    blocked = {'.sfc', '.smc', '.srm', '.sav', '.mss', '.frz', '.bin', '.rom', '.iso', '.chd', '.zip', '.7z', '.rar', '.pem', '.key'}
    excluded_dirs = {'.git', '__pycache__', '.venv', 'local', 'Recriado', 'output', 'runtime'}
    for path in root.rglob('*'):
        if not path.is_file() or any(p in excluded_dirs for p in path.relative_to(root).parts):
            continue
        if path.suffix.lower() in blocked or path.name == '.env' or path.name.startswith('.env.'):
            raise SystemExit(f'Arquivo não publicável: {path.relative_to(root)}')
    checksums = json.loads((root/'checksums.json').read_text())
    for rel, expected in checksums.items():
        file = root/rel
        if not file.is_file() or hashlib.sha256(file.read_bytes()).hexdigest() != expected:
            raise SystemExit(f'Hash divergente ou arquivo ausente: {rel}')
    patches = sorted((root/'patches').rglob('*.ips'))
    for patch in patches:
        for offset, payload in records(patch.read_bytes()):
            if offset + len(payload) > 4194304:
                raise SystemExit(f'Patch ultrapassa 4 MiB: {patch.name}')
    if len(patches) != 12:
        raise SystemExit(f'Esperados 12 patches v198/v199; encontrados {len(patches)}')
    print(f'OK: {len(patches)} patches IPS, {len(checksums)} hashes e conteúdo público verificados.')
    print('Esta checagem não executa uma ROM nem certifica a campanha completa.')


if __name__ == '__main__':
    main()
