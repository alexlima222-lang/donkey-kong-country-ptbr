# Donkey Kong Country — Tradução PT-BR 🇧🇷

Projeto independente de tradução de **Donkey Kong Country (Super Nintendo)** para português brasileiro, desenvolvido a partir da versão americana do jogo.

O objetivo é oferecer uma experiência em português, preservando a jogabilidade, a identidade visual e, sempre que possível, a apresentação do jogo original.

## Estado do projeto

**Primeira versão pública: v1.0 Beta** (base técnica: checkpoint v199).

A tradução inclui melhorias em menus e textos, além de ajustes gráficos. Esta primeira distribuição inclui a correção da placa **BANANAS DO KONG**, encontrada na caverna da primeira fase.

A campanha completa ainda não foi certificada; por isso, a versão é apresentada como beta.

## Duas opções de tradução

O projeto oferece dois patches alternativos:

| Versão | Características | Arquivo IPS |
| --- | --- | --- |
| **Nomes traduzidos** | Menus e nomes das fases em português | `USA_v1.0_para_v199_TRADUZIDOS.ips` |
| **Nomes originais** | Preserva os nomes americanos das fases, mantendo as demais alterações da tradução | `USA_v1.0_para_v199_ORIGINAIS.ips` |

**Escolha somente um dos patches.** Ambos são cumulativos e devem ser aplicados diretamente à ROM americana original, sem tradução prévia. A numeração v199 nos arquivos identifica o checkpoint técnico usado na versão pública v1.0.

## Destaques da versão 1.0

- Correção gráfica da placa **BANANAS DO KONG** na caverna da primeira fase.
- Letras adaptadas à inclinação das tábuas, utilizando tons e elementos gráficos da placa americana.
- Preservação das melhorias de menus da etapa v198.
- Duas variantes com nomes de fases traduzidos ou originais.

## Como instalar

1. Utilize sua própria cópia de **Donkey Kong Country USA v1.0**, sem cabeçalho de copiador (*header*).
2. Faça backup da ROM original e, por precaução, dos arquivos de salvamento (`.srm`).
3. Baixe **um** dos patches IPS na pasta `patches/` ou na seção **Releases**.
4. Aplique o IPS à **ROM original limpa**, usando uma ferramenta compatível com IPS.
5. Abra a ROM modificada em um emulador compatível com SNES.

Não aplique os dois patches entre si, nem sobre uma versão já traduzida. Se o emulador associa o salvamento ao nome da ROM, talvez seja necessário renomear uma cópia do arquivo `.srm` para corresponder à ROM modificada.

## Testes e limitações

A base técnica v199 foi testada no **Mesen 2** nas duas variantes, incluindo visitas e reentrada na caverna. O relatório técnico registra comparações de imagens e memória, indicando que a alteração da v199 em relação à v198 ficou restrita ao recurso gráfico da placa.

**Esses testes não equivalem à conclusão de uma campanha inteira.** Outros textos e situações do jogo ainda podem precisar de revisão.

## Estrutura do repositório

- `patches/` — patches IPS para aplicar à ROM original.
- `docs/` — relatórios, capturas e dados de validação.
- `scripts/` — ferramentas de aplicação e validação.
- `evidencias/` — registros e evidências de desenvolvimento.
- `README.md` — apresentação e instruções do projeto.

## Como relatar problemas

Abra uma **Issue** informando a variante do patch, o emulador e sua versão, a fase ou menu afetado e, se possível, uma captura de tela e os passos para reproduzir o problema. Não envie ROMs comerciais.

## Créditos e direitos autorais

Projeto de tradução PT-BR independente, mantido por **alexlima222-lang**, com auxílio de ferramentas de análise e do ChatGPT durante o desenvolvimento.

*Donkey Kong Country*, seus personagens, músicas, imagens e demais elementos originais pertencem aos respectivos titulares de direitos. Este projeto não é oficial e **não distribui ROMs comerciais**, somente patches e documentação.