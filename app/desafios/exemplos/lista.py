nome = "paulo"
listnomes = ["Bruno","maria","marta","luiz","rafael"]
print(nome)
print(listnomes)
print(len(listnomes)) #contar quantos elementos existem
listnomes.append("Ana") # adiciona um novo item na lista
print(listnomes)
print(listnomes.index("marta")) #recupera o index da pesquisa
nova_lista =[1,5,10,15,20,"carlos","Iory"]
print(nova_lista)
nova_lista.remove("carlos")# remove item da lista
nova_lista.remove(1)
nova_lista.reverse()
print(nova_lista)
nova_lista.append((10,56,9)) #adiciona uma lista dentro de outra lista
print(nova_lista)
lista_mercado = ["leite", "biscoito", "carne","guarana","cereal"]
print("biscoito" in lista_mercado)
print("poeira cosmica" in lista_mercado) #pergunta se esta na lista
print(lista_mercado[3]) #pega o item que voce deseja
print("biscoito" not in lista_mercado) #verifica palavra "biscoito" se não esta na lista
print(lista_mercado[-1]) 
numeros = [5,2,1,4,3]
numeros.sort()
print(numeros)   #ordenando crescente
numeros = [5,2,1,4,3]
numeros.sort(reverse=True)
print(numeros)  #ordenando crescente
listapaia = numeros.copy()  #Copiar listas
#fatiar lista
n1 = numeros[0]
n2 = numeros[1]
#ou
print(numeros[1:3])

(numeros.clear) #apagar tudo.
