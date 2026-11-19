# Donkey Kong Country â€” TraduÃ§Ã£o PT-BR ðŸ‡§ðŸ‡·

Projeto independente de traduÃ§Ã£o de **Donkey Kong Country (Super Nintendo)** para portuguÃªs brasileiro, desenvolvido a partir da versÃ£o americana do jogo.

O objetivo Ã© oferecer uma experiÃªncia em portuguÃªs preservando a jogabilidade, a identidade visual e, sempre que possÃ­vel, a apresentaÃ§Ã£o do jogo original.

## Estado do projeto

**Primeira versÃ£o pÃºblica: v1.0 Beta** (base tÃ©cnica: checkpoint v199).

A traduÃ§Ã£o jÃ¡ possui melhorias em menus e textos, alÃ©m de ajustes grÃ¡ficos. Esta primeira distribuiÃ§Ã£o inclui a correÃ§Ã£o da placa da placa **BANANAS DO KONG**, encontrada na caverna da primeira fase. A campanha completa ainda nÃ£o foi certificada; por isso, esta primeira versÃ£o Ã© apresentada como beta.

## Duas opÃ§Ãµes de traduÃ§Ã£o

A versÃ£o pÃºblica **v1.0** utiliza internamente o checkpoint **v199**; essa numeraÃ§Ã£o tÃ©cnica permanece nos nomes dos patches para garantir rastreabilidade.

O projeto oferece dois patches alternativos:

| VersÃ£o | CaracterÃ­sticas | Arquivo IPS |
| --- | --- | --- |
| **Nomes traduzidos** | Menus e nomes das fases em portuguÃªs | `USA_v1.0_para_v199_TRADUZIDOS.ips` |
| **Nomes originais** | Preserva os nomes americanos das fases, mantendo as demais alteraÃ§Ãµes da traduÃ§Ã£o | `USA_v1.0_para_v199_ORIGINAIS.ips` |

**Escolha somente um dos patches.** Ambos sÃ£o cumulativos e devem ser aplicados diretamente Ã  ROM americana original, sem traduÃ§Ã£o prÃ©via.

## Destaques da primeira versÃ£o (v1.0)

- CorreÃ§Ã£o grÃ¡fica da placa **BANANAS DO KONG** na caverna da primeira fase.
- Letras adaptadas Ã  inclinaÃ§Ã£o das tÃ¡buas, utilizando tons e elementos grÃ¡ficos da placa americana.
- PreservaÃ§Ã£o das melhorias de menus da v198.
- Duas variantes com nomes de fases traduzidos ou originais.

## Como instalar

1. Utilize sua prÃ³pria cÃ³pia de **Donkey Kong Country USA v1.0**, sem cabeÃ§alho de copiador (*header*).
2. FaÃ§a backup da ROM original e, por precauÃ§Ã£o, dos arquivos de salvamento (`.srm`).
3. Baixe o patch IPS da variante desejada na pasta `patches/` ou na seÃ§Ã£o **Releases**.
4. Aplique o IPS Ã  **ROM original limpa** com um programa compatÃ­vel com IPS.
5. Abra a ROM modificada em um emulador compatÃ­vel com SNES.

NÃ£o aplique os dois patches entre si, nem sobre uma versÃ£o jÃ¡ traduzida. Se o emulador associa o salvamento ao nome da ROM, uma cÃ³pia do `.srm` com o nome correspondente pode ser necessÃ¡ria. NÃ£o Ã© obrigatÃ³rio iniciar um jogo novo para a correÃ§Ã£o da placa.

## Testes e limitaÃ§Ãµes

A base tÃ©cnica v199 foi testada no **Mesen 2** nas duas variantes, com visitas e reentrada na caverna. O relatÃ³rio tÃ©cnico documenta comparaÃ§Ãµes de imagens e memÃ³ria, indicando que a alteraÃ§Ã£o da v199 em relaÃ§Ã£o Ã  v198 ficou restrita ao recurso grÃ¡fico da placa.

**Esses testes nÃ£o equivalem Ã  conclusÃ£o de uma campanha inteira.** Outros textos e situaÃ§Ãµes do jogo ainda podem precisar de revisÃ£o.

## Estrutura do repositÃ³rio

- `patches/` â€” patches IPS para aplicar Ã  ROM original.
- `docs/` â€” relatÃ³rios, capturas de comparaÃ§Ã£o e dados de validaÃ§Ã£o.
- `README.md` â€” apresentaÃ§Ã£o e instruÃ§Ãµes do projeto.

## Como relatar problemas

Abra uma **Issue** informando a variante do patch, o emulador e sua versÃ£o, a fase ou menu afetado e, se possÃ­vel, uma captura de tela e os passos para reproduzir o problema. NÃ£o envie ROMs comerciais.

## CrÃ©ditos e direitos autorais

Projeto de traduÃ§Ã£o PT-BR independente, mantido por **alexlima222-lang**, com auxÃ­lio de ferramentas de anÃ¡lise e do ChatGPT durante o desenvolvimento.

*Donkey Kong Country*, seus personagens, mÃºsicas, imagens e demais elementos originais pertencem aos respectivos titulares de direitos. Este projeto nÃ£o Ã© oficial e **nÃ£o distribui ROMs comerciais**: somente patches e documentaÃ§Ã£o.