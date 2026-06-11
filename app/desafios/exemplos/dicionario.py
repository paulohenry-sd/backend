pessoa = {"nome": "ana", "cpf": "122.344.566-00", "tellpone": 31976844290}

print(pessoa)
print(pessoa["cpf"])

pessoa["nome"] = "marilu"

print(pessoa["nome"])

for chave, valor in pessoa.items():
    print(f"seu {chave} é {valor}")

pessoa.update({"nome":"varyn", "cpf": "999.999.999.00", "tellpone": 21097778747})
print(pessoa)