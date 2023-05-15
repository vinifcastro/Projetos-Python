import os
import time
import forca
import jogo_de_advinhacao

print("================================")
print("====== Escolha o seu Jogo ======")
print("================================")

print("\n\nDigite 1 para selecionar o jogo Forca.\nDigite 2 para selecionar o jogo Advinhação\n")

jogo = int(input("Digite o número correspondente ao jogo: "))

if jogo == 1:
    print("\nJogando Forca!")
    time.sleep(1)
    os.system('CLS') or None
    forca.jogar()

elif jogo == 2:
    print("\nJogando Advinhação!")
    time.sleep(1)
    os.system('CLS') or None
    jogo_de_advinhacao.jogar()
else:
    print("\nJogo selecionado inválido!")
