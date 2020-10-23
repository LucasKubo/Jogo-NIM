def  computador_escolhe_jogada (n, m): #Quantas peças o computador quer tirar
    for tirado in range (1,m+1):
        resultado = n - tirado
        if resultado % (m+1) == 0:
            return tirado
    return m
def  usuario_escolhe_jogada (n, m): #Quantas peças o jogador quer tirar 
    while (True):
        peças_tiradas_jogador = int (input ("Quantas peças você vai tirar? "))
        if peças_tiradas_jogador <= m:
            return peças_tiradas_jogador
        else:
            print ("\nOops! Jogada inválida! Tente de novo.\n")
def partida ():
    n = int(input("Quantas peças? ")) 
    m = int(input("Limite de peças por jogada? ")) 
    #Decide quem começa a jogar
    if n % (m+1) == 0:
        print ("\nVocê começa!\n ")
    else: 
        print ("\nComputador começa!\n ")

    peças_no_tabuleiro = n
    while (peças_no_tabuleiro != 0):
        if peças_no_tabuleiro % (m+1) == 0: 
            #multiplo de m+1, ou seja, o jogador joga
            peças_tiradas_pelo_jogador = usuario_escolhe_jogada (peças_no_tabuleiro, m)
            peças_no_tabuleiro = peças_no_tabuleiro - peças_tiradas_pelo_jogador
            if peças_tiradas_pelo_jogador == 1:
               print ("Você tirou uma peça.")
            else: 
                print ("Você tirou {} peças".format (peças_tiradas_pelo_jogador))
            if peças_no_tabuleiro == 1:
                print ("Agora resta apenas uma peça no tabuleiro.\n")
            else:
                print ("Agora restam {} peças no tabuleiro.\n".format (peças_no_tabuleiro))
            # computador joga
            peças_tiradas_pelo_computador = computador_escolhe_jogada (peças_no_tabuleiro,m)
            peças_no_tabuleiro = peças_no_tabuleiro - peças_tiradas_pelo_computador
            if peças_tiradas_pelo_computador == 1:
               print ("O computador tirou uma peça.")
            else: 
                print ("O computador tirou {} peças do tabuleiro.".format (peças_tiradas_pelo_computador))
            if peças_no_tabuleiro != 0:
                print ("Agora restam {} peças no tabuleiro.".format (peças_no_tabuleiro))
        else:
            #Não multiplo de m+1,ou seja, computador joga 
            peças_tiradas_pelo_computador = computador_escolhe_jogada (peças_no_tabuleiro,m)
            peças_no_tabuleiro = peças_no_tabuleiro - peças_tiradas_pelo_computador
            if peças_tiradas_pelo_computador == 1:
               print ("O computador tirou uma peça.")
            else: 
                print ("Computador tirou {} peças do tabuleiro.".format (peças_tiradas_pelo_computador))
            if peças_no_tabuleiro != 0:
                print ("Agora restam {} peças no tabuleiro.\n".format (peças_no_tabuleiro))
    print ("Fim do jogo! O computador ganhou!")
def campeonato ():
    for c in range (1,3+1):
        print ("\n**** Rodada {} ****\n".format (c))
        partida ()
    print ("\n**** Final do campeonato! ****\n")
    print ("Placar: Você 0 X 3 Computador")
def main ():
    print ("\nBem-vindo ao jogo do NIM! Escolha:\n")
    print ("1 - para jogar uma partida isolada")
    escolha = int(input("2 - para jogar um campeonato "))
    if escolha == 1:
        print ("\nVoce escolheu um partida!")
        partida ()
    else:
        print ("\nVoce escolheu um campeonato!")
        campeonato ()
main ()