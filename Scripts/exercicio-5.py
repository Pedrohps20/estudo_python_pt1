# Verificação letra maiuscula e minuscula
def check_char(text):
    type = {"Uppercase": 0, "Lowercase": 0}
    for char in text:
        if char.isupper():
            type["Uppercase"] += 1
        elif char.islower():
            type["Lowercase"] += 1
    
    print("Testo original: ", text)
    print("Número de letras maiúsuclas: ", type["Uppercase"])
    print("Número de letras minúsculas: ", type["Lowercase"])

check_char("A melhor forma de Prever o Futuro é Criá-lo")

# Verifica número par ou ímpar
# meu código


# def check_par(*num):
#     type = {"Par": 0, "Impar": 0}
#     for n in num:
#         if n % 2 == 0:
#             type["Par"] += 1
#         else:
#             type["Impar"] += 1
    
#     print(f"A quantidade de número pares são {type['Par']} e ímpares são {type['Impar']}")

# check_par(5, 6, 87, 12, 3, 90)


# resolvido
def check_numbers(numbers):
    pairs = []
    odd = []
    for number in numbers:
        if number % 2 == 0:
            pairs.append(number)
        else:
            odd.append(number)
    return pairs, odd
print(check_numbers([1, 2, 4, 6, 5, 7, 11, 20]))