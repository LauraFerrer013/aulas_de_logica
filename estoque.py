#Preenchendo estoque

estoque = [10,20,15,50,20]

def atualizar(produto,tipo,quantidade):
    if 0 <= produto < len(estoque):
        if tipo == "vender":
            if estoque[produto] >= quantidade:
                estoque[produto]-=quantidade
                print(f"foram vendidos {quantidade}de produto")
            else:
                print("produto em falta no estoque")
        elif tipo == "repor":
            estoque[produto]+=quantidade
            print(f"foram adicionados{quantidade}unidades de produto{produto}")

def main():
    produto = int(input("Qual é o produto?"))
    tipo = input("O que deseja fazer?")
    quantidade = int(input("Qual a quantidade?"))
    atualizar(produto,tipo,quantidade)
    print("Estoque atual:")
    print(estoque)
    
while True:
    main()
    