import os
import time
import random


def jogo_implementacao():
    pontuacao = 1000  # Define pontuação inicial
    ganhou = False  # Variável que definirá a vitória ou não do jogo
    numero_secreto = random.randrange(1, 101)  # Número secreto randomizado de 1 a 100

    total_de_tentativas = obter_dificuldade()

    for rodada in range(1, total_de_tentativas + 1):  # For que define a quantidade de tentativas
        limpar_tela()
        chute = -1
        print(f"Tentativa número {rodada} de {total_de_tentativas}.\n")

        while not 1 <= chute <= 100:  # Faz com que o usuário digite várias vezes, até a entrada esteja correta
            try:
                chute = int(input("Digite o seu número entre 1 e 100: "))
            except ValueError:  # (try-except) Gera uma exceção caso o número não possa ser convertido para inteiro.
                mensagem = "Valor inválido. " \
                           "Digite um número válido.\n"
                print(mensagem)

        print("Você Digitou:", chute, end="\n\n")

        if numero_secreto == chute:  # Compara o chute do usuário com o número randomizado.
            print("Você acertou!\n")
            ganhou = True
            time.sleep(3)
            break
        else:  # Caso o usuário erre o chute, receberá um feedback se o erro foi pra mais ou menos.
            if chute > numero_secreto:
                print("Você errou! O seu chute foi maior que o número secreto!\n")
            elif chute < numero_secreto:
                print("Você errou! O seu chute foi menor que o número secreto!\n")
            pontuacao -= abs(numero_secreto - chute)
            time.sleep(3)

    limpar_tela()

    if ganhou:  # Mensagem de vitória
        print(f"Sua pontuação foi de: {pontuacao}")
        print("Parabéns, você ganhou!\n")
    else:  # Mensagem de derrota
        print("Que pena, você perdeu!\n")

    print(f"O número secreto era: {numero_secreto}\n")
    print("Fim do jogo!\n")  # Mensagem de encerramento do jogo.


def apresentacao():
    print("================================")
    print("Bem vindo ao jogo de advinhação!")
    print("================================")


def limpar_tela():
    """Limpa a tela do console conforme o OS da pessoa."""
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


def obter_dificuldade():
    """
    Função para obter a dificuldade escolhida pelo jogador.
    Retorna a quantidade de tentativas referente a dificuldade selecionada.
    """
    tentativas = ["", "15", "10", "5"]  # Cria a lista de tentativas por dificuldade(index)
    limpar_tela()
    print("Escolha a dificuldade:")
    print("1 - Fácil")
    print("2 - Intermediário")
    print("3 - Difícil")
    while True:
        escolha = input("Digite o número da dificuldade desejada (1, 2 ou 3): ")
        if escolha in ["1", "2", "3"]:
            return int(tentativas[int(escolha)])
        else:
            limpar_tela()
            print("Opção inválida. Escolha uma dificuldade válida.")


def jogar():
    apresentacao()
    jogo_implementacao()


if __name__ == "__main__":  # Faz com que o arquivo possa ser executado sem a necessidade de outro.
    jogar()
