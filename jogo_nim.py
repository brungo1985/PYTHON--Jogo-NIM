print ("============== Lista Semana 6 - Exercicio JOGO NIM ==============")

'''IMPLEMENTAR JOGO NIM

n = numero de peças no tabuleiro

m = numero de peças maximo q o jogador ou o Pc pode retirar por jogada

'''

"""#############################  FUNÇÃO IMPLEMENTA JOGADA DO COMPUTADOR #############################"""

def computador_escolhe_jogada(n, m):                            #Objetivo dessa função, é culacular sempre a pior cenario para deixar para o adversário

    Pc_remove = 1                                               #Inicio a variavel Pc_remove como 1. É N° minimo de peças que ele deve retirar
    condicao_pc = False

    while not condicao_pc:

        if (n - Pc_remove) % (m + 1) == 0:                          #PC verifica o numero de peças q ficará para o adversario.
            condicao_pc = True
            return Pc_remove

        else:
            if (Pc_remove == m):
                condicao_pc = True
                Pc_remove = m
                return Pc_remove

        Pc_remove = Pc_remove + 1                               #Senão, Pc_remove ganha incremento de 1


"""#############################  FUNÇÃO IMPLEMENTA JOGADA DO USUARIO #############################"""

def usuario_escolhe_jogada(n, m):

    jogada_Ok = False                                                   #Já inicia partindo do ponto q a jogada do usuário será falsa

    while not jogada_Ok:                                                #Enquanto minha jogada não tiver um valor válido. Repete o pedido de jogada

        User_remove = int (input("Quantas peças deseja retirar? - "))   #Solicita o valor ao usuário

        if User_remove > m or User_remove < 1 or (n < m and User_remove > n):                          #Verifico se é um valor válido
            print ()
            print("Esse valor não é um valor de jogada válida:")    
            print ()

        else:                                                           #Se for uma jogada válida. Seta o bit de jogada válida
            jogada_Ok = True

    return User_remove




"""#############################  FUNÇÃO IMPLEMENTA PARTIDA #############################"""


def partida():

    n = int (input("Quantas peças o jogo iniciará? - "))                           #Solicita o numero de peças q o jogo irá começar
    m = int (input("Qual o limite máximo de peças para teirar por jogada? - "))    #Solicita o número maximo de peças q cada jogador poderá retirar

    Vez_Pc = False
    
    vencedor = "Indefinido"         #Inicia sem definição de um vencedor

    if n % (m + 1) == 0:            #Verifica se o numero inicial de peças é multiplo de (m+1). Se for, PC deixa Usuario começar
        print()
        print("Você começa!")

    else:                           #Senão, o PC inicia o a partida
        print()
        print("Computador começa!")
        Vez_Pc = True


    while n > 0:
        if Vez_Pc:                                                  #Se vez do pc for verdadeira
            Pc_remove_1 = computador_escolhe_jogada(n, m)           #Chama função para Pc remover peça

            n = n - Pc_remove_1                                     #Decrementa do numero total

            print()
            print("Computador removeu ", Pc_remove_1," peças:") 

            Vez_Pc = False

        else:
            User_remove_1 = usuario_escolhe_jogada (n, m)           #Se for a vez do usuário, chama função jogada do usuário

            n = n - User_remove_1                                   #Decrementa do numero total

            print()
            print("Usuário removeu ", User_remove_1," peças:")

            Vez_Pc = True

        print()                                                         
        print("Agora restam ", n," peças no tabuleiro")

    if n == 0 and Vez_Pc == False:                                   #Verifica se o Pc venceu a partida
        print()
        print("O Computador Venceu!!!!!")
        vencedor = "PC"
        

    else:
        if n == 0 and Vez_Pc == True:                                #Verifica se o Usuario venceu a partida
            print()
            print("Parabén, você venceu!!!!!")
            vencedor = "USER"

    return vencedor

"""#############################  FUNÇÃO CAMPEONATO #############################"""

def campeonato():

    num_rod = 1                                             #Inicia em 1. Primeira rodada
    vencedeor_1 = "Indefinido"    
    placar_pc = 0
    placar_user = 0

    while num_rod <= 3:                                     #Verifica se numero de rodadas é menor ou igual a 3. Melhor de três
        
        print ()
        print ("****** Rodada N°", num_rod," ******")
        print ()
        
        vencedeor_1 = partida()                             #Chama a partida

        if vencedeor_1 == "PC":                             #Verifica se o PC venceu
            placar_pc = placar_pc + 1                       #Se sim, icrementa 1 no placar

        else:
            if vencedeor_1 == "USER":                       #Verifica se o Usuário venceu
                placar_user = placar_user + 1               #Se sim, icrementa 1 no placar      
        
        num_rod = num_rod + 1                               #Incrementa 1 em numero de rodada a cada partida jogada
        

    print ()
    print ("Placar: Você ", placar_user, " X ", placar_pc, " Computador")


"""#############################  FUNÇÃO PRINCIPAL #############################"""

print("Bem-vindo ao jogo do NIM! Escolha: ")
print()
print("1 - para jogar uma partida isolada;")
print("2 - para jogar um campeonato;")
print()

partida_valida = False

while not partida_valida:
    
    num_partida = int(input(""))
    
    if num_partida == 2 and partida_valida == False:
        print()
        print("Vc escolheu campeonato!")
        print()

        campeonato()

        partida_valida = True

    else:
        if num_partida == 1 and partida_valida == False:
            print()
            print("Vc escolheu jogar uma partida isolada!")
            print()
            
            partida()

            partida_valida = True

        else:
            print()
            print("Valor inválido. Por favor digite um valor de partida válido:")
            print()
            print("1 - para jogar uma partida isolada;")
            print("2 - para jogar um campeonato;")
            print()


