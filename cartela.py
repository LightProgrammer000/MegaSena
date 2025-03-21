"""
# Metodo: Montagem da cartela
"""

# Bibliotecas
from colorama import Fore


# Funcao para montar cartela
def montagem_cartela():

    cartela = list()
    print(f"\n{Fore.LIGHTGREEN_EX}# Escolha 6 numeros de 1 a 60 {Fore.RESET}")

    while len(cartela) < 6:

        try:
            num = int(input(f"# Numero {len(cartela) + 1}: "))

            if not 1 <= num <= 60:
                print(f"{Fore.RED}# Numero {num} fora dos limites! {Fore.RESET}")

            elif num not in cartela:
                cartela.append(num)

            else:
                print(f"{Fore.RED}# Numero '{num}' incluido! {Fore.RESET}")

        except ValueError:
            print(f"{Fore.RED}# Entrada invalida! Digite um numero inteiro.{Fore.RESET}")

    return cartela