# Classe Carro
class Carro:
    def __init__(self, motor="", quantas_rodas=0):
        self.motor = motor
        self.quantas_rodas = quantas_rodas

    def andar(self):
        print("O carro está andando")


# Classe Conta
class Conta:
    def __init__(self):
        pass


# Classe Funcionario
class Funcionario:
    def __init__(self, nome="", idade=0, cargo=""):
        self.nome = nome
        self.idade = idade
        self.cargo = cargo


# Criando objetos Carro
carro1 = Carro("V8", 4)
carro2 = Carro("V6", 4)

# Criando carro sem passar valores
carro3 = Carro()
carro3.motor = "V12"
carro3.quantas_rodas = 4

print(carro3.motor)
carro3.andar()

print("Carro 1 - Motor:", carro1.motor)
print("Carro 2 - Motor:", carro2.motor)


# Classe Cliente
class Cliente:
    def __init__(self, nome, cpf, telefone, email):
        self.nome = nome
        self.cpf = cpf
        self.telefone = telefone
        self.email = email


cliente1 = Cliente(
    nome="João",
    cpf="123.456.789-00",
    telefone="(11) 98765-4321",
    email="joao@email.com",
)

print("\n=== Dados do Cliente ===")
print("Nome:", cliente1.nome)
print("CPF:", cliente1.cpf)
print("Telefone:", cliente1.telefone)
print("Email:", cliente1.email)


# Classe Celular
class Celular:
    def __init__(self):
        pass

    def ligar(self):
        print("O celular está ligando")

    def desligar(self):
        print("O celular está desligando")

    def enviar_mensagem(self, mensagem):
        print("Enviando mensagem:", mensagem)

    def receber_mensagem(self, mensagem):
        print("Recebendo mensagem:", mensagem)


celular1 = Celular()

print("\n=== Teste do Celular ===")
celular1.ligar()
celular1.enviar_mensagem("Olá, tudo bem?")
celular1.receber_mensagem("Oi, tudo ótimo!")
celular1.desligar()


class Aluno:
    def estudar(self):
        for i in range(5):
            print("estudando")

    def vouEstudar(self, resposta):
        if resposta == "sim":
            print("Ótimo, continue!")
        else:
            print("acho melhor você estudar")


aluno = Aluno()
aluno.estudar()
resposta = input("Você vai estudar hoje?")
aluno.vouEstudar(resposta)
