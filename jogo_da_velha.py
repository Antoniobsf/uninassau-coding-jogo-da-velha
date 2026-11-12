opcao_menu = ""
vitorias_x = 0
vitorias_o = 0
empates = 0
total_partidas = 0

while opcao_menu != "4":
    print("\n=== JOGO DA VELHA (UNINASSAU) ===")
    print("1 - Jogar")
    print("2 - Ver Regras")
    print("3 - Placar e Estatísticas (Desafio)")
    print("4 - Sair")
    opcao_menu = input("Escolha uma opção: ")

    if opcao_menu == "1":
        # 1. Matriz declarada por extenso (lista de listas)
        tabuleiro = [
            [" ", " ", " "],
            [" ", " ", " "],
            [" ", " ", " "]
        ]
        venceu = False
        deu_empate = False
        jogador_atual = "X"

        # LOOP DA PARTIDA: Mantém o jogo rodando até ter um vencedor ou empate
        while venceu == False and deu_empate == False:
            print("\n  0   1   2")
        # 2. Exibição da matriz com for aninhado
        for i in range(3):
            linha_str = str(i) + " "
            for j in range(3):
                linha_str = linha_str + tabuleiro[i][j]
                if j < 2:
                    linha_str = linha_str + " | "
            print(linha_str)
            if i < 2:
                print("  ---------")
        
        # 3. Validação de entrada sem quebrar o programa (Integrante 2)
        jogada_valida = False
        while jogada_valida == False:
            print("\nVez do jogador " + jogador_atual)
            linha_str = input("Escolha a linha (0, 1 ou 2): ")
            col_str = input("Escolha a coluna (0, 1 ou 2): ")

            linha_ok = False
            col_ok = False

            # Compara o texto com as strings válidas usando for para evitar ValueError
            for n in range(3):
                if linha_str == str(n):
                    linha_ok = True
                    linha_escolhida = n
                if col_str == str(n):
                    col_ok = True
                    col_escolhida = n

            if linha_ok == True and col_ok == True:
                if tabuleiro[linha_escolhida][col_escolhida] == " ":
                    jogada_valida = True
                    tabuleiro[linha_escolhida][col_escolhida] = jogador_atual
                else:
                    print("Erro: Casa já ocupada! Escolha outra.")
            else:
                print("Erro: Entrada inválida! Digite apenas 0, 1 ou 2.")

       # 4. Verificação de vitória automática com laço for
            for i in range(3):
                # Testa as 3 linhas
                if tabuleiro[i][0] == jogador_atual and tabuleiro[i][1] == jogador_atual and tabuleiro[i][2] == jogador_atual:
                    venceu = True
                # Testa as 3 colunas
                if tabuleiro[0][i] == jogador_atual and tabuleiro[1][i] == jogador_atual and tabuleiro[2][i] == jogador_atual:
                    venceu = True

            # Testa as diagonais
            if tabuleiro[0][0] == jogador_atual and tabuleiro[1][1] == jogador_atual and tabuleiro[2][2] == jogador_atual:
                venceu = True
            if tabuleiro[0][2] == jogador_atual and tabuleiro[1][1] == jogador_atual and tabuleiro[2][0] == jogador_atual:
                venceu = True

            # 5. Verificação de empate com for aninhado
            vazias = 0
            for i in range(3):
                for j in range(3):
                    if tabuleiro[i][j] == " ":
                        vazias = vazias + 1
            
            if vazias == 0 and venceu == False:
                deu_empate = True

            # Fim de turno: Computa resultados ou troca o jogador
            if venceu == True:
                print("\n>>> O jogador " + jogador_atual + " VENCEU a partida! <<<")
                total_partidas = total_partidas + 1
                if jogador_atual == "X":
                    vitorias_x = vitorias_x + 1
                else:
                    vitorias_o = vitorias_o + 1
            elif deu_empate == True:
                print("\n>>> Deu EMPATE! <<<")
                total_partidas = total_partidas + 1
                empates = empates + 1
            else:
                if jogador_atual == "X":
                    jogador_atual = "O"
                else:
                    jogador_atual = "X"
    elif opcao_menu == "4":
        print("A encerrar o programa...")
    elif opcao_menu == "2" or opcao_menu == "3":
        print("Funcionalidade em desenvolvimento para os próximos commits...")
    else:
        print("Opção inválida! Escolha um número de 1 a 4.")
