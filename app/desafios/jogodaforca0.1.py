import os
palavrasecreta = 'casaco'
letras_certas = ""
numero_de_tentativas = 0
letras_erradas = ''


while True:
    letras_digitadas = input("Digite uma letra: ")
    letras_digitadas = letras_digitadas.lower()
    numero_de_tentativas += 1

    if letras_digitadas in letras_certas:
        print("Você já digitou essa letra")
        continue

    if letras_digitadas in letras_erradas:
        print("Você já errou essa letra, pare de digitar ela.")
        continue

    if len(letras_digitadas) > 1:
        print("Digite apenas uma letra")
        continue
    if letras_digitadas in palavrasecreta:
        letras_certas += letras_digitadas
        print("Você acertou a letra")
    else:
        letras_erradas += letras_digitadas
        print("Você errou a letra")

    palavra_formada = ""

    for letra in palavrasecreta:
     if letra in letras_certas:
        palavra_formada += letra
    else:
        palavra_formada += "*"

    print("\n================================")
    print("Palavra formada:", palavra_formada)
    print("letras erradas:", letras_erradas)
    print("Número de tentativas:", numero_de_tentativas)
    print("\n================================")

    if palavra_formada == palavrasecreta:
        os.system("cls" if os.name == "nt" else "clear")
        print("Parabéns, você ganhou!")
        print("A palavra era:", palavrasecreta)
        print("Número de tentativas:", numero_de_tentativas)

        break

    print("\n jogo encerrado.")