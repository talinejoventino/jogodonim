def computador_escolhe_jogada(n, m):
    rem = n % (m + 1)
    if rem > m:
        rem = m
        print('O computador tirou', m, 'peças.')
        return m
    else:
        print('O computador tirou', rem, 'peças.')
        return rem

def usuario_escolhe_jogada(n, m):
    jogada_usuario = int(input('Quantas peças você vai tirar?'))
    while jogada_usuario > m or jogada_usuario <= 0 or jogada_usuario > n:
        print('Oops! Jogada inválida! Tente de novo.')
        jogada_usuario = int(input('Quantas peças você vai tirar?'))
    if jogada_usuario == 1:
        print('Você tirou uma peça.')
    if jogada_usuario <= n and n != 1:
        print('Voce tirou', jogada_usuario, 'peças.')
    return jogada_usuario


def partida():
    n = int(input('Quantas peças?'))
    m = int(input('Limite de peças por jogada?'))
    while m > n or m <= 0 or n <= 0:
        print("Digite um valor válido")
        n = int(input('Quantas peças?'))
        m = int(input('Limite de peças por jogada?'))
    if n % (m + 1) == 0:
        print("Você começa!")
    else:
        print("Computador começa!")
    while n % (m + 1) == 0 and n > 0:
        jogada_usuario = usuario_escolhe_jogada(n, m)
        n = n - jogada_usuario
        print('Agora restam',n ,'peças no tabuleiro.')
        while n % (m + 1) != 0 and n > 0:
            jogada_computador = computador_escolhe_jogada(n, m)
            n = n - jogada_computador
            print('Agora restam',n ,'peças no tabuleiro.')
    while n % (m + 1) != 0 and n > 0:
        jogada_computador = computador_escolhe_jogada(n, m)
        n = n - jogada_computador
        print('Agora restam',n ,'peças no tabuleiro.')
        while n % (m + 1) == 0 and n > 0:
            jogada_usuario = usuario_escolhe_jogada(n, m)
            n = n - jogada_usuario
            print('Agora restam',n ,'peças no tabuleiro.')
    if n == 0:
        print('Fim do jogo! O computador ganhou!')


def campeonato():
    partidas = 0
    while partidas < 3:
        partidas = partidas + 1
        partida()
    print('Placar: Você 0 X',partidas,'Computador')


def interface():
    print('-------------------------------------------')
    print('Bem vindo ao jogo do NIM!! Escolha uma opção:')
    print('-------------------------------------------')
    print('1 - para jogar uma partida isolada')
    print('2 - para jogar um campeonato 2')
    opcao = int(input(''))

    while opcao!= 1 and opcao != 2:
        print('Escolha uma opção válida!')
        opcao = int(input(''))
    if opcao == 1:
        print('Voce escolheu uma partida isolada!!')
        partida()
    if opcao == 2:
        print('Voce escolheu um campeonato!')
        campeonato()


interface()

#Revisar codigo alternativo para a função computador_escolhe_jogada
    # jogadas = 0
    # while jogadas <= n:
    #     jogadas = jogadas + 1
    #     if (m - jogadas) % (m + 1) == 0:
    #         print('O computador tirou', jogadas, 'peças.')
    #         break
    #     if jogadas == n:
    #         print('O computador tirou', jogadas, 'peças.')
    #         break
    # return jogadas