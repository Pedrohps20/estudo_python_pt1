# args e kwargs são argumentos especiais

"""
*args - Utilizamos ele quando não temos certeza de 
quantos argumentos queremos ter numa função

- Os argumentos são passados como uma tupla

**kwargs (tem um arterísco) - Além dos valores podemos passar 
também as respectivas chaves para cada argumento
- Os argumentos são passados como um dicionário
"""

# 1 - Soma de números
def sum (*num):     # quer dizer que posso ter vários números como argumento
    sum_total = 0
    for n in num:
        sum_total += n
    print(f"Soma é: {sum_total}")

sum(7)
sum(7,9)
sum(7,9,10,11)
sum(7,10,9,8,7,6)

# 2 - Apresentação de cursos
def presentation(**data):
    for key, value in data.items():     #data.items pega tanto as chaves quanto valores
        print(f"{key} - {value}")

print("####Curso###")
presentation(name = "Python", category = "Backend", level = "Iniciante")
