#import subprocess

import os

#arquivo = open("app\desafios\exemplos\dados.txt", "r")
#conteudo = arquivo.read()
#print(conteudo)
#arquivo.close()
#leitura
try:
    with open("app\desafios\exemplos\dados.txt", "r") as arquivo:
        conteudo = arquivo.read()
        print(conteudo)
except FileNotFoundError:
    print("arquivo não encontrado")

#sobrescrita
with open("app\desafios\exemplos\dados.txt", "w") as arquivo:
    arquivo.write("bem vindo ao python")

#adicionar novo conteudo
with open("app\desafios\exemplos\dados.txt", "a") as arquivo:
    arquivo.write("  usuario logado\n")


#abrindo em uma da minha escolha
os.startfile("app\desafios\exemplos\dados.txt")
#subprocess.Popen(["code", "app\desafios\exemplos\dados.txt"])