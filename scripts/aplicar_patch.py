#!/usr/bin/env python3
"""Aplica o patch completo v199 à ROM USA verificada; a ROM permanece local."""
from pathlib import Path
import argparse
import hashlib
import json
from patch_io import apply_ips


def main():
    root = Path(__file__).resolve().parent.parent
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--rom', type=Path, required=True)
    parser.add_argument('--variante', choices=['traduzidos', 'originais'], default='traduzidos')
    parser.add_argument('--saida', type=Path, required=True)
    args = parser.parse_args()
    project = json.loads((root/'project.json').read_text())
    data = args.rom.read_bytes()
    source = project['source_rom']
    if len(data) != source['size'] or hashlib.sha256(data).hexdigest() != source['sha256']:
        parser.error('ROM diferente da USA v1.0 sem header validada neste projeto')
    if args.saida.resolve() == args.rom.resolve():
        parser.error('A saída deve ser um arquivo diferente da ROM original')
    if args.saida.exists():
        parser.error('O arquivo de saída já existe; escolha outro nome')
    variant = args.variante.upper()
    patch = root/'patches/v199'/f'USA_v1.0_para_v199_{variant}.ips'
    result = apply_ips(data, patch.read_bytes())
    digest = hashlib.sha256(result).hexdigest()
    if digest != project['variants'][variant]['sha256']:
        raise SystemExit('Falha de integridade: a ROM final não corresponde à v199')
    args.saida.parent.mkdir(parents=True, exist_ok=True)
    args.saida.write_bytes(result)
    print(f'ROM criada localmente: {args.saida}\nSHA-256: {digest}')


if __name__ == '__main__':
    main()
