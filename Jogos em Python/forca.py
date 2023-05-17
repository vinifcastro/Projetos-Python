import os
import time
import random


def jogo_da_forca():
    palavra_secreta = gera_palavra_secreta()  # Gera a palavra secreta

    #variáveis utilizadas no jogo.
    palavra_escondida = ["_" for _ in range(len(palavra_secreta))]  # Cria a lista inicial da palavra escondida
    erros = 0  # Quantidade de erros cometidos pelo jogador.
    forca = ["", "", "", " ", "", "", "", ""]  # Lista que contém a forca no estado atual.
    partes_forca = ["", "(_)", "|", "\\", "/", "|", "/", "\\"]  # Lista que atualizará o estado de forca.
    enforcou = False  # Define se o usuário perdeu.
    acertou = False  # Define se o usuário ganhou.

    letras_jogadas = []  # Lista que armazena as letras anteriormentes jogadas pelo usuario.

    while not enforcou and not acertou:  # While que controla o fim do jogo.
        limpar_tela()
        imprimir_forca(palavra_escondida, forca, letras_jogadas)
        chute = input("Digite uma letra: ").strip().upper()  # Lê a letra a ser chutada pelo usuario.

        if not validar_chute(chute):  # Realiza a validação do chute.
            continue  # Retorna ao início do loop se o chute não for válido.

        if chute in letras_jogadas:
            print("Essa letra ja foi anteriormente jogada, tente outra!")
            time.sleep(2)
            continue
        letras_jogadas.append(chute)

        index = 0
        errou = True
        for letra in palavra_secreta:  # Compara a letra chutada com cada letra da palavra secreta.
            if chute == letra.upper():  # Condição de acerto de letra com alguma da palavra.
                palavra_escondida[index] = letra
                errou = False
            index += 1

        if errou:  # Atualiza a forca em caso de erro do usuário.
            print("\n======= Errou a letra! =======")
            erros += 1
            forca[erros] = partes_forca[erros]
        else:  # Evidencia ao usuário que ele acertou uma letra.
            print("\n======= Acertou a letra! =======")

        enforcou = erros == 7  # Define a derrota no jogo.

        acertou = "_" not in palavra_escondida

        time.sleep(1)

    limpar_tela()
    imprimir_forca(palavra_escondida, forca, letras_jogadas)

    if acertou:  # Mensagem de parabéns, caso o usuário ganhe o jogo.
        print("Parabéns, você ganhou!!!", end="\n\n")
    if enforcou:  # Mensagem de derrota, caso o usuário perca o jogo.
        print(f"A palavra era: {palavra_secreta}", end="\n\n")
        print("Infelizmente você perdeu!!!", end="\n\n")

    print("Fim do jogo!", end="\n")  # Mensagem de encerramento do jogo.


def gera_palavra_secreta():
    # Função que abre o txt, seleciona uma palavra aleatoriamente e a retorna essa palavra.
    palavras = []
    arquivo = open("palavras.txt", "r")
    for linha in arquivo:
        palavras.append(linha.strip())
    palavra_secreta = palavras[random.randrange(0, len(palavras))]  # Palavra a ser descoberta pelo jogador.
    arquivo.close()
    return palavra_secreta


def apresentacao():
    # Essa função faz a apresentação do jogo.
    print("===========================")
    print("Bem vindo ao jogo de forca!")
    print("===========================")


def limpar_tela():
    # Função para limpar a tela do console
    if os.name == 'nt':
        os.system('cls')  # Limpa a tela no Windows
    else:
        os.system('clear')  # Limpa a tela em sistemas Unix


def imprimir_forca(palavra_escondida, forca, letras_jogadas):
    # Função para imprimir a forca e a palavra escondida na tela
    print(' '.join(palavra_escondida), end="\n\n")
    print("Forca:")
    print("  _______     ")
    print(" |/      |    ")
    print(" |   ", f"  {forca[1]}  ")
    print(" |    ", forca[3], forca[2], forca[4])
    print(" |      ", forca[5])
    print(" |     ", forca[6], forca[7])
    print(' '.join(letras_jogadas), end="\n\n")


def validar_chute(chute):
    # Função para validar se o chute do usuário é válido (apenas uma letra)
    if len(chute) != 1 or not chute.isalpha():
        print("Por favor, digite apenas uma letra.")
        return False
    return True


def jogar():
    apresentacao()
    time.sleep(1)
    jogo_da_forca()


if __name__ == "__main__":  # Faz com que o arquivo possa ser executado sem a necessidade de outro.
    jogar()
