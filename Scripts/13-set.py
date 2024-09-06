gamesSet = {"Fifa 23", "Red Dead 2", "Star Wars", "The Legend of Zelda",
            "Mario Odissey", "Resident Evil 4"}
# set e tupla não posso repetir valores, na lista eu posso

print(gamesSet)
# ********- Não possibilita recuperar valores via fatiamento


# 1 - Buscar o tamanho do set
print(len(gamesSet))

# 2 - True e 1 são considerados o mesmo valor
exempleSet = {"Fifa 23", True, 1, 90.50}
print(exempleSet)

# 3 - Adicionar item de outro set
gamesSet.update(exempleSet)
print(gamesSet)

# 4 - Remover um item do set
gamesSet.remove(True)
gamesSet.remove(90.50)
print(gamesSet)