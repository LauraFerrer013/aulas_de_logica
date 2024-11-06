
def novo_artista(novo): #Criar uma função
    artistas.append(novo) #Coloca no final da lista um valor
    print("\n O Artista: ",novo," foi inserido na lista.") #Imprime o valor que foi inserido
    print("\n A lista nova ficou assim:",artistas) #imprime a lista completa
    
    
def sub_artista(antigo, novo): #Recebe os aparametros de artista antigo e novo
    indice = artistas.index(antigo) #Busco o valor do antigo artita na listae devolvo a sua posição na lista
    artistas[indice] = novo #Eu substituo o valor do antigo artista pelo novo
    print("\n O Artista: ",antigo," foi substituido pelo novo artista,",novo) #imprime o artista antigo e o novo
    print("\n A nova lista é: ",artistas) #imprime a lista completa
    
def lista_atual():    
    print("\n A nova lista é: ",artistas) #Imprime a lista atualizada dos artistas
    
def sair():
    
    
def quantidade():
    exit

    
print("------- SISTEMA DE AGENDAMENTO DE SHOWS! ----------")
while True:
    print("MENU:")
    print("1.INSERIR NOVO ARTISTAS NA LISTA")
    print("2.SUBSTITUIR ARTISTA DA LISTA")
    print("3.LISTA ATUAL")
    print("4.QUANTIDADE DE ARTISTAS")
    
    
    menu = int(input("O que você deseja fazer?"))
    
    if menu == 1:
        #insere o novo artista no final da lista 
        novo = input("Insira o nome do novo artista: ")
        novo_artista(novo)
        
    elif menu == 2:
        antigo = input("Insira o nome do artista que será removido: ")
        novo = input("Insira o nome do artista que será o inserido no lugar: ")
        #subistitui o nome do novo artista
        sub_artista(antigo,novo)
            
    elif menu == 3:
        lista_atual()
    
    elif menu == 4:
        quantidade()
    else:
        print("O código não é válido!")