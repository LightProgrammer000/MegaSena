# Bibliotecas
from colorama import Fore

# Função para montar a cartela
def montagem_cartela():

    cartela = []
    print(f"\n{Fore.LIGHTGREEN_EX}# Escolha 6 números de 1 a 60 {Fore.RESET}")

    while len(cartela) < 6:

        try:
            num = int(input(f"# Número {len(cartela) + 1}: "))
            if 1 <= num <= 60 and num not in cartela:
                cartela.append(num)
            else:
                print(f"{Fore.RED}# Número inválido ou já incluído!{Fore.RESET}")

        except ValueError:
            print(f"{Fore.RED}# Entrada inválida! Digite um número inteiro.{Fore.RESET}")

    return cartela
