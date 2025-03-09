# Bibliotecas
from colorama import Fore
from montagem_cartela import montagem_cartela
from sorteio_mega_sena import sorteio_mega_sena

# Função do menu
def menu():

    try:
        print(f"{Fore.LIGHTYELLOW_EX}{'=-=' * 10} 💰 MEGA SENA 💰 {'=-=' * 10} {Fore.RESET}")
        print(f"{Fore.LIGHTMAGENTA_EX}# [1] Sorteio de 1 vez {Fore.RESET}")
        print(f"{Fore.CYAN}# [2] Jogar 1000 vezes {Fore.RESET}")
        opc = int(input("# Opc.: "))

        if opc == 1:
            sorteio_mega_sena(montagem_cartela(), 1)

        elif opc == 2:
            sorteio_mega_sena(montagem_cartela(), 10000)

        else:
            print(f"{Fore.RED}# Opção inválida!{Fore.RESET}")

    except ValueError:
        print(f"{Fore.RED}# Entrada inválida! Digite um número inteiro.{Fore.RESET}")

# Função principal
def main():
    menu()

# Execução
if __name__ == '__main__':
    main()