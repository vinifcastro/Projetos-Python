import os
import time
import forca
import jogo_de_advinhacao


def limpar_console():
    # Limpa a tela do console
    os.system('cls' if os.name == 'nt' else 'clear')


def exibir_menu():
    # Exibe o menu de seleção de jogos
    print("===============================")
    print("====== Escolha o seu Jogo =====")
    print("===============================")
    print("\nDigite 1 para selecionar o jogo Forca.")
    print("Digite 2 para selecionar o jogo Advinhação.\n")


def jogar_jogo(jogo):
    # Inicia o jogo selecionado
    print(f"\nJogando {jogo}!")
    time.sleep(1)
    limpar_console()

    if jogo == 'forca':
        forca.jogar()
    elif jogo == 'advinhacao':
        jogo_de_advinhacao.jogar()


def main():
    limpar_console()
    exibir_menu()
    jogo = int(input("Digite o número correspondente ao jogo: "))  # O Usuário digita o jogo que deseja iniciar

    if jogo == 1:   # Seleciona o jogo escolhido ou filtra a entrada caso ela seja invalida
        jogar_jogo('forca')
    elif jogo == 2:
        jogar_jogo('advinhacao')
    else:
        print("\nJogo selecionado inválido!")


if __name__ == "__main__":  # Faz com que o arquivo possa ser executado sem a necessidade de outro.
    main()
