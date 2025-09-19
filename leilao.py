def ganhador(apostas):
    vencedor = ""
    maior_aposta = 0

    for jogador in apostas:
        quantia_aposta = apostas[jogador]
        if quantia_aposta > maior_aposta:
            maior_aposta = quantia_aposta
            vencedor = jogador

    print(f"O ganhador é {vencedor} com a maior aposta de ${maior_aposta}")


apostas = {}
continuar_aposta = True

while continuar_aposta:
    nome = input("Diga seu nome: ")
    idade = int(input("Qual a sua idade? "))

    if idade < 18:
        print(" Você não pode jogar, sinto muito!")
        continue
    preco = int(input("Qual a sua aposta? $ "))
    apostas[nome] = preco

    devo_continuar = input("Você quer continuar? Responda 'sim' ou 'nao': ").lower()
    if devo_continuar == "nao":
        continuar_aposta = False
        ganhador(apostas)
    elif devo_continuar == "sim":
        print("\n" * 20)

