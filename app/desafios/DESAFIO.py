# desafio bombastico de conta - pupansa/corrente 10/06/2026

class Cliente:
    def __init__(self, nome, cpf):
        self.nome = nome
        self.cpf = cpf

    def __str__(self):
        return f"Cliente: {self.nome} | CPF: {self.cpf}"


class Conta:
    def __init__(self, numero, titular):
        self.numero = numero
        self.titular = titular
        self.saldo = 0.0

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            print(f"Depósito de R${valor:.2f} realizado.")
        else:
            print("Valor inválido.")

    def sacar(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
            print(f"Saque de R${valor:.2f} realizado.")
        else:
            print("Saldo insuficiente.")

    def transferir(self, valor, destino):
        if valor <= self.saldo:
            self.saldo -= valor
            destino.saldo += valor
            print(f"Transferência de R${valor:.2f} realizada.")
        else:
            print("Saldo insuficiente.")

    def consultar_saldo(self):
        return self.saldo

    def extrato(self):
        print(f"Conta: {self.numero}")
        print(f"Titular: {self.titular.nome}")
        print(f"Saldo: R${self.saldo:.2f}")

    def __str__(self):
        return f"Conta {self.numero} | Titular: {self.titular.nome} | Saldo: R${self.saldo:.2f}"


class ContaCorrente(Conta):
    def __init__(self, numero, titular, limite):
        super().__init__(numero, titular)
        self.limite = limite

    def sacar(self, valor):
        if valor <= self.saldo + self.limite:
            self.saldo -= valor
            print(f"Saque de R${valor:.2f} realizado.")
        else:
            print("Limite excedido.")

    def __str__(self):
        return (
            f"Conta Corrente {self.numero} "
            f"Titular: {self.titular.nome} "
            f"Saldo: R${self.saldo:.2f} "
            f"Limite: R${self.limite:.2f}"
        )


class ContaPoupanca(Conta):
    def __init__(self, numero, titular, rendimento):
        super().__init__(numero, titular)
        self.rendimento = rendimento

    def calcular_rendimento(self):
        return self.saldo * (self.rendimento / 100)

    def __str__(self):
        return (
            f"Conta Poupança {self.numero} "
            f"Titular: {self.titular.nome} "
            f"Saldo: R${self.saldo:.2f} "
            f"Rendimento: {self.rendimento}%"
        )


cliente1 = Cliente("João", "123.456.789-00")
cliente2 = Cliente("Maria", "987.654.321-00")

conta_corrente = ContaCorrente("0001", cliente1, 500)
conta_poupanca = ContaPoupanca("0002", cliente2, 5)

print(cliente1)
print(cliente2)


conta_corrente.depositar(1000)
conta_poupanca.depositar(500)

print(f"\nSaldo conta corrente: R${conta_corrente.consultar_saldo():.2f}")
print(f"Saldo conta poupança: R${conta_poupanca.consultar_saldo():.2f}")


conta_corrente.sacar(120)


conta_corrente.transferir(200, conta_poupanca)

print(f"\nSaldo conta corrente: R${conta_corrente.consultar_saldo():.2f}")
print(f"Saldo conta poupança: R${conta_poupanca.consultar_saldo():.2f}")

print(
    f"\nRendimento da poupança: "
    f"R${conta_poupanca.calcular_rendimento():.2f}"
)

conta_corrente.extrato()
conta_poupanca.extrato()

print(conta_corrente)
print(conta_poupanca)