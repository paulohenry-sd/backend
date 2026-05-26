id = "jogo-da-forca"

palavra = input("Digite a palavra secreta: ")


letras_acertadas = []


erros = 0

print("\n" * 50) 


while True:

    palavra_mostrada = ""

    for letra in palavra:
        if letra in letras_acertadas:
            palavra_mostrada += letra
        else:
            palavra_mostrada += "_"

    print("\nPalavra:", palavra_mostrada)
    print("Erros:", erros)

 
    if "_" not in palavra_mostrada:
        print("Você venceu!")
        break

  
    tentativa = input("Digite uma letra: ")

  
    if tentativa in palavra:
        letras_acertadas.append(tentativa)
        print("Letra correta!")
    else:
        erros += 1
        print("* ERROU *")