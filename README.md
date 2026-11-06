# Jogo da Velha no Terminal - Coding UNINASSAU

Trabalho de 2ª Avaliação da disciplina de Coding do curso de Análise e Desenvolvimento de Sistemas (UNINASSAU) do Professor Thiago Martins.

## Como executar o programa
Para rodar o jogo, certifique-se de ter o Python instalado. Abra o terminal na pasta do projeto e execute o comando:
`python jogo_da_velha.py`

## Regras do Jogo
O jogo acontece em um tabuleiro 3x3. Dois jogadores (X e O) se alternam, informando a linha e a coluna para marcar uma casa vazia. Vence quem completar primeiro uma linha, uma coluna ou uma diagonal com o seu símbolo. Se todas as casas forem preenchidas sem um vencedor, o jogo termina empatado.

## Desafio Lógico Escolhido
**Estatísticas da Sessão (Nível Básico):** O menu principal possui uma opção para exibir o placar acumulado. Ele calcula e mostra o total de partidas finalizadas, as vitórias absolutas de cada jogador, os empates e a taxa de vitória (porcentagem) de cada um durante a sessão.

## Divisão de Tarefas do Trio
* **[Antônio José Barros]:** Criação do repositório, declaração da matriz do tabuleiro, laço while do menu principal, renderização visual do tabuleiro com `for` aninhado e contagem de casas vazias.
* **[Marcos Aurelio]:** Implementação do sistema de input, lógica de validação de entradas com conversão para string e laço de checagem para impedir ocupação de casas já preenchidas.
* **[Mayson de Tacio]:** Lógica das verificações automáticas de vitória integrando o laço `for`, implementação da tela de regras e cálculos das Estatísticas da Sessão.
