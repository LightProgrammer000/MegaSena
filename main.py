"""
# Principal
"""

# Bibliotecas
from colorama import Fore
from montagem_cartela import montagem_cartela
from sorteio_mega_sena import sorteio_mega_sena

# Menu
def menu():

    try:
        print(f"\n{Fore.LIGHTYELLOW_EX}{'=-=' * 10} 💰 MEGA SENA 💰 {'=-=' * 10} {Fore.RESET}")
        print(f"{Fore.LIGHTMAGENTA_EX}# [1] Sorteio de 1 vez {Fore.RESET}")
        print(f"{Fore.LIGHTBLUE_EX}# [2] Com 1 cartela jogue 1000 (mil) vezes {Fore.RESET}")
        print(f"{Fore.LIGHTWHITE_EX}# [3] Com 1 cartela jogue 10.000 (dez mil) vezes {Fore.RESET}")
        print(f"{Fore.LIGHTGREEN_EX}# [4] Com 1 cartela jogue 100.000 (cem mil) vezes {Fore.RESET}")
        print(f"{Fore.LIGHTRED_EX}# [0] Saida {Fore.RESET}")
        print(f"{Fore.LIGHTYELLOW_EX}{'=-=' * 10} 💰 MEGA SENA 💰 {'=-=' * 10} {Fore.RESET}")

        opc = int(input(f"\n{Fore.LIGHTBLUE_EX}# Opc.: {Fore.RESET}"))

        if opc == 0:
            exit(1)

        if opc == 1:
            sorteio_mega_sena(montagem_cartela(), 1)

        elif opc == 2:
            sorteio_mega_sena(montagem_cartela(), 1000)

        elif opc == 3:
            sorteio_mega_sena(montagem_cartela(), 10000)

        elif opc == 4:
            sorteio_mega_sena(montagem_cartela(), 100000)

        else:
            print(f"{Fore.RED}# Opção inválida!{Fore.RESET}")

    except ValueError:
        print(f"{Fore.RED}# Entrada invalida! Digite um numero inteiro {Fore.RESET}")

    except KeyboardInterrupt:
        print(f"{Fore.MAGENTA}# Programa Encerrado !{Fore.RESET}")


# Função principal
def main():
    menu()


# Execução
if __name__ == '__main__':
    main()