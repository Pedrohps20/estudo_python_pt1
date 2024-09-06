gameFifa = {
    "name": "Fifa 23",
    "yearLaunch": "2022",
    "gamePrice": 90.50,
    "classification": 8.5,
    "genre": ["esport", "família"]
}
print(gameFifa)
print(len(gameFifa))
print(type(gameFifa))

# 1 - Recuperar um elemento do dicionário
print(gameFifa['genre'])
print(gameFifa.get('classification'))   #posso usar as " " sem problemas

# 2 - Buscar apenas as chaves do dicionário
print(gameFifa.keys())

# 3 - Buscar apenas os valores do dicionário
print(gameFifa.values())

# 4 - Buscar itens do dicionário com chaves e valor
print(gameFifa.items())

# 5 - Adicionar itens no dicionário
gameFifa["players"] = 2
print(gameFifa)

# 6 - Atualizar itens do dicionário
gameFifa.update({"players": 1})
print(gameFifa)

# 7 - Remover itens do dicionário
gameFifa.pop("players")
print(gameFifa)