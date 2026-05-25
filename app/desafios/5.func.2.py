def maior(a, b):
    if a > b:
        print(a, "é maior")
    elif b > a:
        print(b, "é maior")
    else:
        print("Os números são iguais")

n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))

maior(n1, n2)