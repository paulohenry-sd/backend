#questões de POO, questão 4 08/06/2026

class Produto:
    def __init__(self, preco):
        self.preco = preco

    def aplicar_desconto(self, porcentagem):
        self.preco = self.preco - (self.preco * porcentagem / 100)


preco = float(input("Digite o preço do produto: "))
produto = Produto(preco)

desconto = float(input("Digite o desconto (%): "))
produto.aplicar_desconto(desconto)

print(f"Preço final: R${produto.preco}")

#polimorfismo

