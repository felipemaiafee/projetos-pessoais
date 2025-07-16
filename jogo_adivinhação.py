import random
import time
import sys
from colorama import init, Fore, Back, Style
init(autoreset=True)

def contador_percentual():
    print(Fore.YELLOW + Style.BRIGHT + "Verificando seu número...")
    for i in range(1, 101):
        sys.stdout.write(f"\r{i}% ")
        sys.stdout.flush()
        time.sleep(0.01)  # ajusta a velocidade aqui

def cabecalho(msg):
    largura = len(msg) + 4
    print(Back.BLACK + Fore.LIGHTBLUE_EX + Style.BRIGHT + "=" * largura)
    print(Back.BLACK + Fore.MAGENTA + Style.BRIGHT + msg.center(largura))
    print(Back.BLACK + Fore.LIGHTBLUE_EX + Style.BRIGHT + "=" * largura)

def jogo():
    while True:
        cabecalho("JOGO DA ADIVINHAÇÃO")
        print(Fore.RED + Style.BRIGHT + "1".center(3) + Fore.RESET + ") Para jogar")
        print(Fore.RED + Style.BRIGHT + "2".center(3) + Fore.RESET + ") Para sair do jogo")
        try:
            escolha = int(input(Style.BRIGHT + "Digite sua escolha: "))
        except ValueError:
            print(Fore.RED + " Digite um número válido (1 ou 2).")
            continue

        if escolha == 2:
            print("Saindo do jogo. Até mais!")
            return

        elif escolha == 1:
            numero_secreto = random.randint(1, 100)
            numero_tentativas = 0

            while True:
                try:
                    numero_escolhido = int(input(Back.WHITE + Fore.BLACK + Style.BRIGHT + "Digite o número secreto (1 a 100): "))
                    numero_tentativas += 1
                    contador_percentual()
                except ValueError:
                    print("Por favor, digite um número válido.")
                    continue

                if numero_escolhido == numero_secreto:
                    print(Back.BLACK + Style.BRIGHT + Fore.LIGHTGREEN_EX + f"🎉 PARABÉNS, você acertou o número {numero_secreto}!")
                    print(Style.BRIGHT + f"Você tentou {numero_tentativas} vez(es) até acertar.")
                    jogar_novamente = input(Style.BRIGHT + f"Você quer jogar novamente? [{Fore.GREEN + Style.BRIGHT}S{Fore.RESET}/{Fore.RED + Style.BRIGHT}N{Fore.RESET}] ").strip().upper()

                    if jogar_novamente == "N":
                        print("Obrigado por jogar!")
                        return
                    else:
                        break
                elif numero_escolhido < numero_secreto:
                    print("🔺 O número secreto é " + Fore.RED + Style.BRIGHT + "maior.")
                else:
                    print("🔻 O número secreto é " + Fore.GREEN + Style.BRIGHT + "menor.")
        else:
            print("Opção inválida. Escolha 1 ou 2.")

jogo()