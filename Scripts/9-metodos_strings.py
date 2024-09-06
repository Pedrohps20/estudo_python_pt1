nomeJogo = "Tomb Raider"

descricaoJogo = '''
Tomb Raider é um jogo de mapa
estilo RPG em terceira pessoa
que possui uma experiência incrível!
'''

descricaoJogo2 = '''
Tomb, Raider, é um jogo, de mapa,
estilo RPG em terceira pessoa
que possui uma experiência incrível!
'''

print(nomeJogo.upper()) # Retornar string em maíusculo
print(nomeJogo.lower()) # Retornar string em minúsculo
print(nomeJogo.capitalize()) # Retorna a primeira letra em maiúsculo
print(nomeJogo.title()) # Retorna a primeira letra em maiúsculo 
print(nomeJogo.center(15, '-')) # Centraliza com caractere de preenchimento
print(nomeJogo.find("b")) # Retorna a posição de um determinado caractere
print(descricaoJogo.count("t")) # Conta caracteres
print(descricaoJogo.count("a")) # Conta caracteres
print(descricaoJogo.replace("Tomb", "Resident"))
print(descricaoJogo2.split(','))