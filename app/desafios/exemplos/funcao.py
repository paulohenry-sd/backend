def soma(num1,num2):
    total = num1+num2
    return total

def exebirmsg():
    print("isso é uma função")

def exebirmsg2():
    return "isso é uma função"

#temp =soma()
print(soma(5,15))

print(exebirmsg2)
exebirmsg()


def subtrair(num3,num4):
    total = num3-num4
    return total

def exebirmsg3():
    print("resultado da subtração:")

exebirmsg3()

print (subtrair(10,5))

def multiplicar(num5,num6):
    total = num5*num6
    return total

def exebirmsg6():
    print("sua multiplicação deu:")

exebirmsg6()

print (multiplicar(12,5))

#=====================================================

def test(senha):
    if senha =="12154":
        print("senha correta")
    else:
        print("senha incorreta")

test(input("digite a sua senha:\n"))

def contnum(num):
    for i in range(1,num):
        print(1)

contnum(15)

# =====================================================

def contwhile():
    count=0
    while count<3:
        print(count)
        count+1

contwhile()
# ====================================================


#importante: 

# +   # soma
# -   # subtração
# *   # multiplicação
# /   # divisão
# //  # divisão inteira
# %   # resto da divisão
# **  # potência

# ===================================================