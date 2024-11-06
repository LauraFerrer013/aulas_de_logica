class Pessoa:
    def __init__(self, nome, email, senha):
        self.nome = nome
        self._email = email
        self.__senha = senha
    def apresentar(self):
        print(f"nome: {self.nome}, {self._email}")
pessoa1 = Pessoa("laura", "laura@hotmail", 999)
print(pessoa1.nome)
print(pessoa1._email)
pessoa1.apresentar()
print(pessoa1__senha)

