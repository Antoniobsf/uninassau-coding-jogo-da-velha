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
        
        # O Integrante 2 vai adicionar o ciclo de leitura e validação aqui no próximo commit
        print("\n[O tabuleiro foi gerado! A leitura de jogadas será inserida na próxima etapa.]")

    elif opcao_menu == "4":
        print("A encerrar o programa...")
    elif opcao_menu == "2" or opcao_menu == "3":
        print("Funcionalidade em desenvolvimento para os próximos commits...")
    else:
        print("Opção inválida! Escolha um número de 1 a 4.")
