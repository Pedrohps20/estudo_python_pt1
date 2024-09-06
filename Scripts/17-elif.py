num1 = float(input("Digite o número um\n"))
num2 = float(input("Digite o número dois\n"))
operation = input("Digite a operação a realizar (+ - * /)\n")

if operation == "+":
    result = num1 + num2

elif operation == "-":
    result = num1 - num2
    
elif operation == "*":
    result = num1 * num2

elif operation == "/":
    result = num1 / num2
    
print("Operação inválida")

print(f"Resutado é: {result:.2f}")