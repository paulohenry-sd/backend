#trabalho de funções data:22/06/2026  questão: 3

# 3. Função que calcula o fatorial usando FOR 
# Crie uma função fatorial(n) que usa um for para calcular o fatorial de um número. 

def fatorial(n):
    resultado = 1

    for i in range(1, n + 1):
        resultado = resultado * i

    return resultado


numero = int(input("Digite um número: "))
print(fatorial(numero))