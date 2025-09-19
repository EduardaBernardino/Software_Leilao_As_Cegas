# Leilão às Cegas (CLI)

Pequeno programa em Python para rodar um leilão às cegas no terminal.
Participantes informam nome, idade e valor da aposta. Ao encerrar, o script anuncia quem fez a maior oferta.

“Às cegas” porque os participantes não veem as ofertas anteriores (o console é “limpo” entre rodadas).

✨ O que ele faz

Recebe apostas de múltiplos jogadores.

Bloqueia menores de 18 anos.

Armazena apenas o maior lance por pessoa (último lance substitui o anterior).

Exibe o vencedor e o valor ao final.

📁 Arquivo

leilao_cego.py (o seu código abaixo)

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

🚀 Como executar

Pré-requisito: Python 3.9+

python leilao_cego.py

🕹️ Exemplo de sessão
Diga seu nome: Ana
Qual a sua idade? 27
Qual a sua aposta? $ 120
Você quer continuar? Responda 'sim' ou 'nao': sim


Diga seu nome: Bruno
Qual a sua idade? 19
Qual a sua aposta? $ 150
Você quer continuar? Responda 'sim' ou 'nao': nao
O ganhador é Bruno com a maior aposta de $150

🔎 Como funciona (resumo técnico)

As apostas são guardadas em um dict apostas: {nome -> valor}.

Cada leitura de usuário:

Pede nome e idade.

Se idade < 18, ignora (segue para o próximo).

Lê preco e atualiza apostas[nome].

Pergunta se continua; se não, chama ganhador(apostas).

ganhador percorre o dicionário e mantém o maior lance.

