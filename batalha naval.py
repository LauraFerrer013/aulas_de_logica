tabuleiro = [['~'] * 10 for i in range (10)]

def imprimir_tabuleiro(tabuleiro):
    for linha in tabuleiro:
        print (" ".join(linha))
    print()
    
#imprimir_tabuleiro(tabuleiro)

def colocar_navio(tabuleiro, linha_inicial, coluna_inicial, tamanho, orientacao):
    if orientacao == 'horizontal':
        for i in range(tamanho):
            tabuleiro[linha_inicial][coluna_inicial * i] = '#'
    elif orientacao == 'vertical':
        for i in range(tamanho):
            tabuleiro[linha_inicial * i][coluna_inicial] = '#'
            
            
#colocar_navio(tabuleiro,1,1,3,'vertical')
#imprimir_tabuleiro(tabuleiro)

def dar_tiro(tabuleiro, linha, coluna):
    if tabuleiro[linha][coluna]== '#':
        tabuleiro[linha][coluna] = 'X'
        print('pow pow!!')
        return True
    elif tabuleiro[linha][coluna] == "~":
        tabuleiro[linha][coluna] = "o"
        print("Seu merda")
        return False
    else:
        print("Você ja atirou aqui")
        return False
    
#colocar_navio(tabuleiro,1,1,3,'vertical')
#imprimir_tabuleiro(tabuleiro)
#dar_tiro(tabuleiro,2,1)
#imprimir_tabuleiro(tabuleiro)

def jogo():
    #Cria dois tabuleiro dos jogadores
    tamanho=10
    tabuleiro_jogador1 = [['~'] * tamanho for _ in range (tamanho)]
    tabuleiro_jogador2 = [['~'] * tamanho for _ in range (tamanho)]
    
    #colocar os navios nas pasições
    colocar_navio(tabuleiro_jogador1,1,2,3, 'vertical')
    colocar_navio(tabuleiro_jogador2,3,2,4, 'horizontal')
    
    while True:
        print("jogador 1 atirando:")
        imprimir_tabuleiro(tabuleiro_jogador2)
        
        x = int (input("Jogador 1 escolha a linha de tiro (0,9): "))
        y = int (input("Jogador 1 escolha a linha de tiro (0,9): "))
        dar_tiro(tabuleiro_jogador2,x,y)
        
        #Verificar
        if all(cell !='#' for row in tabuleiro_jogador2 for cell in row):
            print("jogadro 1 ganhouu!")
            break
        
        print("jogador 2 atirando:")
        imprimir_tabuleiro(tabuleiro_jogador1)
        
        x = int (input("Jogador 2 escolha a linha de tiro (0,9): "))
        y = int (input("Jogador 2 escolha a linha de tiro (0,9): "))
        dar_tiro(tabuleiro_jogador1,x,y)
        
        #Verificar
        if all(cell !='#' for row in tabuleiro_jogador2 for cell in row):
            print("jogadro 2 ganhouu!")
            break
        
jogo()