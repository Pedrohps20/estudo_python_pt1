gameList = ["Fifa", "God of War", "Red Dead 2", "Uncharted", 90.50]

#for ... in ... = foreach

# 1 - Iterando valores de uma lista
for game in gameList:
    print(game)
    
# 2 - QUando a condição for atendida, o Loop será encerrado
for game in gameList:
    if game == "Red Dead 2":
        break                   # chegando em red dead ele vai encerrar a execução
    print(game)
    
# 3 - Quando a condição for atendida, o Loop vai para a próxima iteração
for game in gameList:
    if game == "Red Dead 2":
        continue                # ele pula o red dead
    print(game)
    
# 4 - Avaliação do Jogo
# for i in range(5):              # range define um valor limite
#     print("Hello World")
gameName = input("Digite o nome do jogo\n")
gameRating = int(input("Digite quantas avaliações deseja fazer no jogo\n"))

sum = 0
for i in range(gameRating):
    nota = float(input("Digite a nota para o jogo\n"))
    sum += nota
print(f"Média de avaliação do jogo {gameName} é {sum/gameRating:.2f}")