# Como contribuir

Para relatar um erro, informe versão, variante dos nomes das fases, emulador/hardware, local e passos para reproduzir. Uma captura do jogo é útil.

Para propor uma mudança:

1. Descreva o problema concreto e o comportamento esperado.
2. Preserve as duas variantes e os textos que não fazem parte da alteração.
3. Registre o hash da ROM usada localmente.
4. Quando houver alteração visual, inclua capturas reais antes/depois no mesmo roteiro.
5. Informe o que foi testado e os limites do teste.
6. Execute `python3 scripts/verificar_repositorio.py` antes do envio.

Não envie ROMs, saves pessoais, estados de emulador, dumps, executáveis de emuladores, credenciais ou arquivos de ambiente. Use pastas locais ignoradas pelo Git. Patches IPS e métricas são suficientes para documentar mudanças binárias.

Não declare uma correção concluída apenas por um script terminar sem erro: compare também o resultado visual quando a alteração afetar gráficos ou textos na tela.
