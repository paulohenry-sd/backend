#questões de POO, questão 3 08/06/2026

class Contador:
    def __init__(self):
        self.valor = 0

    def aumentar(self):
        self.valor += 1

    def diminuir(self):
        self.valor -= 1

contador = Contador()
contador.aumentar()
contador.diminuir()

contador = Contador()

while True:
    print(f"\nValor atual: {contador.valor}")
    opcao = input("Digite '+' para aumentar, '-' para diminuir ou 'sair': ")

    if opcao == "+":
        contador.aumentar()

    elif opcao == "-":
        contador.diminuir()

    elif opcao.lower() == "sair":
        break

    else:
        print("Opção inválida!")