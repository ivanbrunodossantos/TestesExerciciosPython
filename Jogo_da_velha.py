def menu():
    continuar = 1
    while continuar:
        continuar = int(input('0. Sair \n' +
                              '1. Jogar mais uma? \n'))
        if continuar:
            jogo()
        else:
            print('até a próxima')


def jogo():
    jogada = 0
    while venceu() == 0:
        print(f' \n Jogador {jogada % 2 + 1}')
        exibe()
        linha = int(input('\n Linha :'))
        coluna = int(input('Coluna:'))
        if board[linha - 1][coluna - 1] == 0:
            if (jogada % 2 + 1) == 1:
                board[linha - 1][coluna - 1] = 1
            else:
                board[linha - 1][coluna - 1] = -1
        else:
            print('Nao esta vazio')
            jogada -= 1
        if venceu():
            print(f'Jogador, {jogada % 2 + 1} ganhou depois de {jogada + 1} rodadas')
        jogada += 1


def venceu():
    for c in range(3):
        soma = board[c][0] + board[c][1] + board[c][2]
        if soma == 3 or soma == -3:
            return 1
    for c in range(3):
        soma = board[0][c] + board[1][c] + board[2][c]
        if soma == 3 or soma == -3:
            return 1
    diag1 = board[0][0] + board[1][1] + board[2][2]
    diag2 = board[0][2] + board[1][1] + board[2][0]
    if diag1 == 3 or diag1 == -3 or diag2 == 3 or diag2 == -3:
        return 1
    return 0


def exibe():
    for a in range(3):
        for b in range(3):
            if board[a][b] == 0:
                print(' _ ', end=' ')
            elif board[a][b] == 1:
                print(' X ', end=' ')
            elif board[a][b] == -1:
                print(' O ', end=' ')
        print()


board = [[0, 0, 0],
         [0, 0, 0],
         [0, 0, 0]]
menu()
