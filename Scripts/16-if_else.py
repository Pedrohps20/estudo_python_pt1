name = input("Digite o nome do jogo\n")
yearLaunch = int(input("Digite o ano do jogo\n"))
classification = float(input("Digite a nota de classificação do jogo\n"))

if (classification >= 8.0):
    print(f"O jogo {name} é bom, recomendo jogá-lo")
else:
    print(f"o jogo {name} ainda não atingiu uma boa nota, por isso não recomendo")
    
# Operadores lógicos = AND é o mesmo de && e OR é o mesmo de ||