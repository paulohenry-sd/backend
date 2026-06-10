#questoes de POO, questão 8 08/06/2026

class Pessoa:
    contador = 0

    def __init__(self, nome):
        self.nome = nome
        Pessoa.contador += 1


p1 = Pessoa("João")
p2 = Pessoa("Maria")
p3 = Pessoa("Pedro")

print("Quantidade de objetos criados:", Pessoa.contador)