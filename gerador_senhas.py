from random import choice
from colorama import init, Fore, Back, Style
init(autoreset=True)

def cabecalho(msg):
    largura = len(msg) + 24
    print(Back.BLACK + Fore.LIGHTCYAN_EX + Style.BRIGHT + "=" * largura)
    print(Back.BLACK + Style.BRIGHT + msg.center(largura))
    print(Back.BLACK + Fore.LIGHTCYAN_EX + Style.BRIGHT + "=" * largura)

def validar_sn(pergunta):
    while True:
        destaque = f"{pergunta.strip()} ({Fore.GREEN}S{Style.RESET_ALL}/{Fore.RED}N{Style.RESET_ALL}) "
        resposta = input(destaque).strip().upper()
        if resposta in ("S", "N"):
            return resposta
        else:
            print(Fore.YELLOW + "Resposta inválida! Digite apenas S ou N.")


def mostrar_senha(senha):
    mensagem = "SENHA GERADA ---> " + Fore.RED + senha
    largura = len(mensagem) + 4
    print(Back.BLACK + Style.BRIGHT + mensagem.center(largura))



def gerador():
    cabecalho("GERADOR DE SENHAS")
    maisculas = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "X", "Y", "Z"]
    minusculas = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "x", "y", "z"]
    numeros = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    simbolos = ["!", "@", "#", "$", "%", "&", "*", "-", "=", "+", ".", ",", "?", ";", "/", "ç"]
    caracteres_permitidos = []
    total_caracteres = 0
    while True:
        try:
            total_caracteres = int(input(Style.BRIGHT + "Quantos caracteres a senha deve ter? "))
            break
        except ValueError:
            print("ERRO! Digite um valor válido.")

    utilizar_maisculas = validar_sn(Style.BRIGHT + "Incluir letras maiúsculas? ")
    if utilizar_maisculas == "S":
        caracteres_permitidos.extend(maisculas)

    utilizar_minusculas = validar_sn(Style.BRIGHT + "Incluir letras minúsculas? ")
    if utilizar_minusculas == "S":
        caracteres_permitidos.extend(minusculas)

    utilizar_numeros = validar_sn(Style.BRIGHT + "Incluir números? ")
    if utilizar_numeros == "S":
        caracteres_permitidos.extend(numeros)

    utilizar_simbolos = validar_sn(Style.BRIGHT + "Incluir símbolos? ")
    if utilizar_simbolos == "S":
        caracteres_permitidos.extend(simbolos)

    if not caracteres_permitidos:
        print("Você precisa escolher pelo menos um tipo de caractere.")
        return
    else:
        senha = ""
        for c in range(total_caracteres):
            senha += choice(caracteres_permitidos)
        mostrar_senha(senha)






gerador()