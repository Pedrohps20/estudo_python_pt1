# def é a palavra reservada de python para criar funções

# 1 - Função para imprimir Hello World
def wellcome():
    print("Hello World")

wellcome()

# 2 - Função para somar dois números
def sum():
    # print(5+4)
    return 5 + 4
    
print(sum())

# 3 - Função para cadastrar um jogo
def create_game():
    nome = input("Digite o nome do jogo\n")
    anoLancamento = int(input("Digite o ano de lançamento do jogo\n"))
    precoDoJogo = float(input("Digite o preço do jogo\n"))
    noteRating = float(input("Digite a nota de avaliação do jogo\n"))
    
    print(f"{nome} - R$ {precoDoJogo}")

create_game()