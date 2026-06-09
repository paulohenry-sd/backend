class teclado:
    def __init__(self,marca,preço,cor):
        self.marca = marca
        self.preço = preço
        self.cor = cor

    def __str__(self):
        return f"marca: {self.marca}\n preço: {self.preço}\n cor: {self.cor}"

    def minhafunção(self):
        return f"marca: {self.marca}\n preço: {self.preço}\n cor: {self.cor}"
    
tecladologtac= teclado("Logitech", 150.00, "Preto")
print(tecladologtac)
tecladoOutro = teclado("Razer", 200.00, "Prata")
print(tecladoOutro.minhafunção())

#Herança
class animal:
    def __init__(self,revestimento_externo):
        self.revestimento_externo = revestimento_externo

    def __str__(self):
            return f"revestimento externo: {self.revestimento_externo}"

    def minhafunção(self):
        return f"revestimento externo: {self.revestimento_externo}"


class mamifero(animal):
    def comer():
        print("esta sendo amamentado")

class carnívoro(animal):
    def comer():
        print("esta comendo carne")

tubarão = animal("escamas")
print(tubarão.comer())

#polimorfismo
class Passaro:
    def voar(self):
        return "voando alto"

class Aviao:
    def voar(self):
        return "voando em velocidade máxima"

def decola(obj):
    print(obj.voar())

decola(Passaro())
decola(Aviao())