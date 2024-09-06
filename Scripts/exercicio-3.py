distancia = float(input("Digite a distância que quer viajar\n"))

if distancia <= 200:
    valor = distancia * 0.5
else:
    valor = distancia * 0.35
print(f"O valor da sua passagem é de: {valor:.2f}")

# - Aumento sálario funcionário

salario = float(input("Digite o valor do seu salário\n"))

if salario > 1250.00:
    aumentoSalario = salario * 0.1 + salario
else:
    aumentoSalario = salario * 0.15 + salario

print("O novo valor salarial é de: ", aumentoSalario )