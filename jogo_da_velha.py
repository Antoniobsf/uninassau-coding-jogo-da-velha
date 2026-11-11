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

        # Troca temporária de jogador (o Integrante 3 vai mover isto para depois da verificação de vitória)
        if jogador_atual == "X":
            jogador_atual = "O"
        else:
            jogador_atual = "X"
        print("\n[O tabuleiro foi gerado! A leitura de jogadas será inserida na próxima etapa.]")

    elif opcao_menu == "4":
        print("A encerrar o programa...")
    elif opcao_menu == "2" or opcao_menu == "3":
        print("Funcionalidade em desenvolvimento para os próximos commits...")
    else:
        print("Opção inválida! Escolha um número de 1 a 4.")
