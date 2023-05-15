import os
import time
import random
import sys
def jogar():
    print("================================")
    print("Bem vindo ao jogo de advinhação!")
    print("================================")

    pontuacao = 1000
    rodada = 0
    ganhou = False
    numero_secreto = random.randrange(1, 101)

    dificuldade = int(input("Qual a dificuldade desejada?\n1 - Fácil\n2 - Intermediário\n3 - Difícil\nDigite a dificuldade (1,2 ou 3): "))

    if dificuldade == 1:
        total_de_tentativas = 15
    elif dificuldade == 2:
        total_de_tentativas = 10
    elif dificuldade == 3:
        total_de_tentativas = 5
    else:
        print("\n\nDificuldade selecionada inválida!\n")
        sys.exit()

    for rodada in range(1, total_de_tentativas+1):
        os.system('CLS') or None
        chute = -1
        print(f"Tentativa número {rodada} de {total_de_tentativas}.", end="\n\n")

        while int(chute) <= 0 or int(chute) > 100:
            chute = input("Digite o seu número entre 1 e 100: ")

        print("Voce Digitou: ", chute, end="\n\n")

        if numero_secreto == int(chute):
            print("Você acertou!", end="\n\n")
            ganhou = True
            time.sleep(3)
            break
        else:
            if int(chute) > numero_secreto:
                print("Você errou! O seu chute foi maior que o número secreto!", end="\n\n")
            elif int(chute) < numero_secreto:
                print("Você errou! O seu chute foi menor que o número secreto!", end="\n\n")
        pontuacao -= abs(numero_secreto - int(chute))
        time.sleep(3)

    os.system('CLS') or None
    if ganhou:
        print(f"Sua pontuação foi de: {pontuacao}")
        print("Parabéns, você ganhou!", end="\n\n")
    else:
        print("Que pena, você perdeu!", end="\n\n")

    print(f"O número secreto era: {numero_secreto}", end="\n\n")
    print("Fim do jogo!", end="\n")

if __name__ == "__main__":
    jogar()
