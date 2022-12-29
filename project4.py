# project to creat a rock paper scissors game #

from random import choice
from time import sleep

MSG_DE_VITORIA = "\033[1;31mAÊ! GANHEI!\033[m"
MSG_DE_EMPATE = "\033[1;33mOPS... empatou!!!\033[m"
MSG_DE_DERROTA = "\033[1;32mDroga, você venceu!\033[m"

lista = ["pedra", "papel", "tesoura"]
vitorias_jogador = vitorias_computador = 0

while True:
    print("-=" * 22)
    print("Vou fazer a minha jogada, tente me vencer!")
    print("-=" * 22)

    sleep(1)

    print("\033[33mDEIXA EU PENSAR...\033[m")
    computador = choice(lista)
    print("-=" * 22)

    sleep(2)

    jogada = str(input("Pronto, faça a sua jogada: ")).strip().lower()
    while jogada not in lista:
        jogada = str(input(
            "Jogada inválida. Faça a sua jogada: "
        )).strip().lower()

    print("-=" * 22)
    print("JO")
    sleep(1)
    print("KEN")
    sleep(1)
    print("PÔ....")
    sleep(1)
    print("-=" * 22)
    sleep(1)

    if computador == jogada:
        print(MSG_DE_EMPATE)
    elif computador == "pedra" and jogada == "tesoura":
        print(MSG_DE_DERROTA)
        vitorias_computador += 1
    elif computador == "papel" and jogada == "pedra":
        vitorias_computador += 1
        print(MSG_DE_DERROTA)
    elif computador == "tesoura" and jogada == "papel":
        print(MSG_DE_DERROTA)
        vitorias_computador += 1
    else:
        print(MSG_DE_VITORIA)
        print(f"Eu joguei {computador.upper()}!")
        vitorias_jogador += 1
    resp = str(input("Deseja continuar? ")).strip().upper()[0]
    if resp in "N":
        break

print(
    f"Ok! Você ganhou {vitorias_jogador} vezes"
    f"e eu {vitorias_computador} vezes!"
)
if vitorias_jogador > vitorias_computador:
    print("Parabéns, você ganhou o jogo!")
if vitorias_jogador < vitorias_computador:
    print("Eu ganhei o jogo!")
else:
    print("Nós empatamos!")
