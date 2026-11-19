# Publicação e manutenção

Nome preparado: `donkey-kong-country-ptbr`. Visibilidade autorizada pelo responsável: pública.

Os comandos abaixo descrevem o envio inicial. Eles só devem ser usados em uma conta GitHub autenticada e no diretório deste projeto. O ZIP preparado não representa, por si só, uma publicação no GitHub.

```bash
python3 scripts/verificar_repositorio.py
git init -b main
git add .
git commit -m "Documenta tradução DKC PT-BR até a v199"
gh repo create donkey-kong-country-ptbr --public --source=. --remote=origin --push
```

O autor do commit deve ser configurado com a identidade verificada do responsável, sem inventar nome de usuário ou e-mail. Caso o repositório já exista, confirme o destino e use o remoto correto; não force um envio sobre outro projeto.

## Atualizações

Acrescente o patch da nova versão, o relatório, capturas pertinentes e métricas. Atualize `project.json`, o README, o histórico e `checksums.json`. Execute a verificação e publique um commit descritivo. Preserve os patches e relatórios anteriores.

## Releases

Uma release deve anexar somente patches e documentação pública. Não envie o ZIP completo dos checkpoints de trabalho, pois ele pode conter ROMs, dumps ou saves. Os checkpoints privados são usados para retomada do trabalho, não como anexos de distribuição pública.
