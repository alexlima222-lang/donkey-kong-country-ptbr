# DKC PT-BR v199 — placa “Bananas do Kong”

**Correção concluída e validada visualmente no Mesen 2.** A revisão modifica somente o recurso gráfico da placa da caverna no início da primeira fase. Os menus da v198 e os demais textos permanecem como estavam.

## Problema e causa

A placa não é um retângulo gráfico único. Ela é montada a partir de 13 sprites de 8 × 8 ou 16 × 16 pixels, com coordenadas diferentes, formando tábuas inclinadas e o poste. A composição reta da tradução anterior não respeitava essa montagem, produzindo letras recortadas e elementos fora das tábuas.

O recurso foi identificado pela comparação entre as ROMs e a VRAM real. Seu início é o offset de arquivo `0x06099B`, carregado no intervalo de VRAM de objetos `0x3400–0x37FF`. A paleta de objetos usada é a 3. As coordenadas dos sprites e os dados de paleta não foram alterados.

## Alteração

- Restaurada a base gráfica americana da placa para eliminar resíduos da inscrição anterior.
- Removidas as letras inglesas; a madeira coberta por elas foi recuperada por amostragem de pixels próximos na mesma tábua, preservando os tons da paleta original.
- Letras extraídas da própria placa americana e reorganizadas para escrever **BANANAS / DO / KONG**.
- Escrita ajustada à inclinação das tábuas; a primeira e a terceira linha receberam ajustes de tamanho para caber na madeira.
- Mantidos os três tons claros da pintura original, em lugar da fonte reta e uniforme da v198.

O construtor verifica que os 357 pixels da nova inscrição estão sobre a silhueta original da madeira: **zero pixels novos de texto fora do objeto**. A menor distância entre a inscrição e a transparência é de um pixel nativo. A largura da primeira linha é de 43 pixels; “DO” ocupa 15 e “KONG”, 31.

A intervenção altera **504 bytes por variante**, todos dentro do bloco gráfico de 1.024 bytes da placa. Nada foi alterado fora dele. Não houve mudança de código, colisões, física, rotinas de save, coordenadas de sprites ou paletas. Cada ROM continua com 4.194.304 bytes.

## Validação real no Mesen

A execução foi automatizada com `--testRunner`, saída 0 e `Snes.DisableFrameSkipping=true`. O personagem entra na caverna, sai e entra novamente. As capturas finais foram obtidas diretamente pelo buffer gráfico da PPU, sem imagens simuladas.

| Verificação | Resultado |
|---|---|
| Variante com nomes traduzidos | Executada até o quadro 4220, com duas visitas à caverna |
| Variante com nomes originais | Mesmo roteiro, duas visitas à caverna |
| Quadros comparados por variante | 2800, 3000, 3300, 3600, 3900 e 4200 |
| Comparações de imagem | 12 pares com a v198 |
| Dentro da caverna | 717 pixels diferentes, exclusivamente na placa |
| Fora da caverna / transições amostradas | Zero pixels diferentes |
| WRAM, SRAM, OAM e CGRAM | Zero bytes diferentes em todos os pares |
| VRAM dentro da caverna | Somente os 504 bytes dos gráficos da placa diferem |
| VRAM fora do recurso da placa | Zero bytes diferentes |
| Placa na reentrada | Idêntica à primeira visita |
| Duas variantes da tradução | Mantida a divergência original dos 124 bytes de nomes das fases |
| IPS | Seis patches, com aplicação e reversão verificadas |
| Construtor portátil | Reproduziu as duas ROMs finais byte a byte |

O retângulo de diferenças visuais é `x=59–106, y=152–183` no buffer nativo de 239 linhas, incluindo a margem superior da PPU. É o local da inscrição da placa. As imagens resumidas mostram recortes ampliados com vizinho mais próximo, sem inventar pixels intermediários.

As capturas, estados e dumps estão em `Resultados/Mesen/`; as medições estão em `Resultados/validacao.json` e `.csv`. As execuções finais também registram o SHA-256 da ROM efetivamente testada.

## Arquivos

- `ROMs/`: v199 com nomes de fases traduzidos ou originais.
- `Patches/`: IPS completos USA→v199, incrementais v198→v199 e reversíveis v199→v198.
- `Capturas/`: comparação antes/depois, referência americana e caverna completa.
- `Fontes_USA/`: índice gráfico original, paleta e mapeamento das peças da placa.
- `Scripts/`: construtor, captura, decodificação e verificação.

O pacote anterior `DKC_PTBR_v198_MENUS_ESTILO_USA.zip` permanece preservado separadamente. A reversão por IPS também permite recuperar suas duas ROMs exatas a partir desta entrega.

### Reconstrução

```bash
python3 Scripts/recriar_placa.py \
  --original /caminho/USA_v1.0_sem_header.smc \
  --base /caminho/DKC_PTBR_v198_MENUS_ESTILO_USA.zip \
  --saida Recriado
```

Dependências: Python 3, NumPy, Pillow e SciPy. O construtor confere os hashes de origem antes da alteração.

### SHA-256 das ROMs finais

```text
Nomes traduzidos:
240cf99a17801b1cd7780804db9d7be178da3514b33bba36ad66a5278cbc4e6e
Nomes originais:
8a08beff657e5ae2e06461b0ffe402c075a5e52e3f306617b3f001d8afe33bce
```

Esta validação cobre a alteração da placa e o roteiro descrito. Não certifica uma campanha completa nem os demais textos da tradução. O checksum SNES armazenado foi mantido como na base; a integridade desta entrega é registrada pelos SHA-256 em `SHA256SUMS.txt`.
