nome = input("Digite o nome do jogo\n")
anoLancamento = int(input("Digite o ano de lançamento do jogo\n"))
precoDoJogo = float(input("Digite o preço do jogo\n"))
planoIncluso = bool(input("Está incluso no serviço semanal?\n"))

print("####Dados do Jogo###")
print("====================")
# Alternativa 1
# print("Nome do Jogo:", nome)
# print("Ano do Jogo", anoLancamento)
# print("Preço do Jogo:", precoDoJogo)
# print("esta incluso no plano?:", planoIncluso)


# Alternativa 2
# print("Nome do Jogo:", nome, "\nAno de Lançamento", anoLancamento, "\nPreço do Jogo", precoDoJogo, 
#       "\nEstá incluido no plano?", planoIncluso)


# Alternativa 3
print(f"Nome do Jogo: {nome} \nAno de Lançamento: {anoLancamento} \nPreço do Jogo:
      {precoDoJogo} \nEstá incluso no plano? {planoIncluso}")