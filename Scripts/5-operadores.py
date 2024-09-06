n1 = int(input("Digite o primeiro número\n"))
n2 = int(input("Digite o segundo número\n"))

# Aritméticos
soma = n1 + n2
sub = n1 + n2
div = n1 / n2
mult = n1 *  n2
resto = n1 % n2
exp = n1 ** n2      # exemplo: 4 elevado a 2
print(f"Qual é o resto de {n1} e {n2}: {resto}")
print(f"Qual é o número {n1} elevado a {n2}: {exp}")

# Comparação 
maior = n1 > n2
menor = n1 < n2
igual = n1 == n2
diferente = n1 != n2
maior_igual = n1 >= n2
menor_igual = n1 <= n2

print(f"O {n1} e {n2} são iguais? {igual}")
print(f"O número {n1} é maior ou igual a {n2}? {maior_igual}")

n1 += 2
n2 -= 1
n1 *= 4
n2 /= 2