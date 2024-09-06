gamesList = ["Resident Evil", "Star Wars Jedi Survivor",
             "The Legend of Zelda", "Red Dead 2"]

# 1 - Tamnaho da lista
print(len(gamesList)) #len vem de length (tamanho) - vai imprimir o tamanho da lista

# 2 - Recuperar um item da lista pelo índice
print(gamesList.index("The Legend of Zelda"))   # vai buscar a posição do item

# 3 - Adicionar item ao final da lista
gamesList.append("Gta V")   # Vai incluir itens ao final da lista
print(gamesList)

# 4 - Ordenar Lista
gamesList.sort()
print(gamesList)

# 5 - Copiar os itens de uma lista para outra
gameReset = gamesList.copy()    # copia os itens de uma lista para a outra
gameReset.remove("Resident Evil")
print(gameReset)

# 6 - Remove todos os itens da lista
gamesList.clear()
print(gamesList)