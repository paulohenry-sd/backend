#questões de POO, questão 5 08/06/2026

class Veiculo:
    def __init__(self, marca):
        self.marca = marca

    def exibir_marca(self):
        print(f"Marca: {self.marca}")


class Carro(Veiculo):
    pass


class Moto(Veiculo):
    pass


carro = Carro("Toyota")
moto = Moto("Honda")

carro.exibir_marca()
moto.exibir_marca()