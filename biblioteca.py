biblioteca = [] #vetor biblioteca

#função add livro
def adicionar_livro(titulo,autor,genero):
    livro =  {'titulo':titulo, 'autor':autor,'genero':genero, 'disponivel':True}
    biblioteca.append(livro)
    print(f"O livro {titulo} foi adicionada com sucesso")
    
#adicionar_livro('A voz do silencio', 'Luis Fernando', 'drama')
#print(biblioteca)

def remove_livro(titulo):
    for livro in biblioteca:
        if livro['titulo'] == titulo:
            biblioteca.remove(livro)
            print(f"O livro{titulo}foi removido com sucesso!")
        
#adicionar_livro('A voz do silencio', 'Luis Fernando', 'drama')
#print(biblioteca)
#remove_livro('A voz do silencio')
#print(biblioteca)

def buscar_livro (busca):
    for livro in biblioteca:
        if livro['titulo'] == busca or livro['autor'] ==  busca or livro['autor'] == busca:
            print ("Resultado da busca:\n")
            print(f"Livro: {livro['titulo']} | Autor: {livro['titulo']} | Genero:{livro['titulo']} - status {livro['disponivel']} ")
            return
        else:
            print("Livro não encontado!")

#adicionar_livro('Um', 'Laura', 'suspense')
#adicionar_livro('Dois', 'Sofia', 'drama')
#adicionar_livro('Tres', 'Igor', 'terror')
#adicionar_livro('Quatro', 'Kleber', 'romance')
#buscar_livro('Laura')

def listar_livro():
    if not biblioteca:
        print("Nenhum livro encontado!")
    else:
        print("lista de livros:\n")
        for livro in biblioteca:
            if livro ['disponivel'] == True:
                status = 'Disponivel'-
            else:
                status = 'Indisponivel'
                
            print(f"Livro: {livro['titulo']} | Autor: {livro['titulo']} | Genero:{livro['titulo']} - status {livro['disponivel']} ")
                                                                                                                                                                  
def mostrar_menu():
    print("\nMenu principal Biblioteca:")
    print("1. Adicionar Livro")
    print("2. Remover Livro")
    print("3. Buscar Livro") 
    print("4. Listar Livros")
    print("5. Verificar Disponibilidade")
    print("6. Emprestimo de Livro") #Função em Contrução 
    print("7. Sair")
 
        
        
