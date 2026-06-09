class Carro:
    def __init__(self, motor="", quantas_rodas=0):
        self.motor = motor
        self.quantas_rodas = quantas_rodas

    def andar(self):
        print("O carro está andando")
