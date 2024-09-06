# Gerando substrings a partir de uma string

nomeJogo = "Tomb Raider"

descricaoJogo = '''
Tomb Raider é um jogo de mapa
estilo RPG em terceira pessoa
que possui uma experiência incrível!
'''

# string[inicio : fim] - indice começa na posição 0 / índice final - 1

# 1 - Busque toda string a partir da primeira posição
print(nomeJogo[0:])

# 2 - Busque toda string até a última posição
print(nomeJogo[:11])    # o nome da minha variável tem 10 letras (contando com o 0) - por isso q coloco 1 a mais

# 3 - Busque toda string da terceira até a última posição
print(nomeJogo[2:])

"""
string [início: fim: passo] - índice começa na posição 0 | índice final -1
passo - determina o incremento. Por padrão esse número é o 1.
"""

# 4 - Busque toda string de 2 em 2 caracteres
print(nomeJogo[::2])

# 5 = Busque toda a string nos índeces ímpares
print(nomeJogo[1::2])

# 6 - Inverter uma string de trás pra frente
print(nomeJogo[::-1]) # -1 vai inverter a string, imprimindo de trás para frente

