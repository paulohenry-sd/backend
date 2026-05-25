"""
operador função 
+ soma
- subtração 
* multiplicação
/ divisão 
// divisão inteira
% resto divisão 
** ptencia
"""
num1 = float(input("digite um numero:"))
num2 = float(input("digite o segundo numero:"))

soma = num1 + num2

subtração = num1 - num2

multiplicação = num1 * num2

divisão = num1 / num2

divisão_inteira = num1 // num2

resto_divisão = num1 % num2

potencia = num1 ** num2


print(" resultado da + :", soma )

print(" resultado da - :", subtração )

print(" resultado da * :", multiplicação )

print(" resultado da / :", divisão )

print(" resultado da // :", divisão_inteira )

print(" resultado da % :", resto_divisão )

print(" resultado da ** :", potencia )

#é bem importante saber que ´pra numeros voce deve usar ou "int" ou "float" ex= float(input())