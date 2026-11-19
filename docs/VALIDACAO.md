# Validação no Mesen 2

## Evidência existente

Os relatórios v198 e v199 descrevem execuções anteriores, com seus limites. A verificação automática do GitHub confere os arquivos públicos; não reproduz uma campanha e não possui ROMs ou saves.

## Repetir o roteiro da caverna localmente

Use um runtime Mesen 2 compatível com os scripts Lua fornecidos. O teste exige acesso de I/O dos scripts e `Snes.DisableFrameSkipping=true`, conforme `scripts/settings_mesen.json`. Mantenha esse perfil separado da sua instalação de uso pessoal.

O script inicializa uma SRAM artificial zerada, entra na primeira fase, visita a caverna, sai e entra de novo. Ele não carrega o seu save pessoal.

Exemplo no Linux, com a ROM já gerada localmente:

```bash
mkdir -p local/capturas-v199
DKC_CAPTURE_DIR="$PWD/local/capturas-v199" \
DOTNET_SYSTEM_GLOBALIZATION_INVARIANT=1 \
/caminho/runtime/Mesen --testRunner --enableStdout \
  "$PWD/scripts/validar_caverna_mesen.lua" \
  "$PWD/local/DKC_PTBR_v199_NOMES_TRADUZIDOS.sfc" --timeout=60
```

O resultado esperado inclui `DONE`, código de saída 0 e capturas dos quadros 2800, 3000, 3300, 3600, 3900 e 4200. Use o buffer direto `*_core.ppm` para a comparação. As linhas de margem da PPU fazem a imagem nativa ter 239 linhas; os recortes resumidos mostram 224 linhas visíveis.

Para uma revisão nova, repita o mesmo roteiro na versão anterior e na candidata. Compare as imagens e as memórias de acordo com o escopo da alteração. Não publique os arquivos `.bin`, saves ou ROMs gerados: mantenha-os em `local/` e registre métricas e capturas selecionadas.
