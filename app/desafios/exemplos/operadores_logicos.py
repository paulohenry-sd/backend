"""
op1 logico    op2
operando1 >   operando2
operando1 >=  operando2
operando1 <  operando2
operando1 <=  operando2
operando1 ==  operando2
operando1 !=  operando2  ou not no if
resultados valor true/false
"""
valor = float(input("escreva o seu primeiro valor: "))

valor2 = float(input("escreva o seu segundo valor: "))

print("o numero", valor, "é maior que o ", valor2,"?:")
print(valor > valor2)

print("o numero", valor, "é maior ou igual ao ", valor2,"?:")
print(valor >= valor2)

print("o numero", valor, "é menor que o ", valor2,"?:")
print(valor < valor2)

print("o numero", valor, "é menor ou igual ao ", valor2,"?:")
print(valor <= valor2)

print("o numero", valor, "é igual ao ", valor2,"?:")
print(valor == valor2)

print("o numero", valor, " NÂO é igual ao", valor2,"?:")
print(valor != valor2)