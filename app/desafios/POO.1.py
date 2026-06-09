#questões de POO, questão 1 08/06/2026

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    def apresentar(self):
        print(f"nome do individuo: {self.nome}, idade: {self.idade}")

pessoa1 = Pessoa("João", 30)
pessoa1.apresentar()

pessoa2 = Pessoa("Maria", 25)
pessoa2.apresentar()

pessoa3 = Pessoa("Carlos", 40)
pessoa3.apresentar()