"""
# Metodo: Relatorio
"""

# Importacao
from colorama import Fore

def relatorio(sena, quina, quadra, trinca, dupla, una, nula):

    # Exibe relatorio de vitorias
    print(f"\n\n{Fore.GREEN}# {'=-=' * 20} RELATORIO {'=-=' * 20} {Fore.RESET}", end=" ")
    print(f"\n{Fore.LIGHTYELLOW_EX}# SENA: {Fore.RESET}{Fore.LIGHTGREEN_EX}{sena}{Fore.RESET}")
    print(f"{Fore.LIGHTYELLOW_EX}# QUINA: {Fore.RESET}{Fore.LIGHTGREEN_EX}{quina}{Fore.RESET}")
    print(f"{Fore.LIGHTYELLOW_EX}# QUADRA: {Fore.RESET}{Fore.LIGHTGREEN_EX}{quadra}{Fore.RESET}")
    print(f"{Fore.LIGHTYELLOW_EX}# TRINCA: {Fore.RESET}{Fore.LIGHTGREEN_EX}{trinca}{Fore.RESET}")
    print(f"{Fore.LIGHTYELLOW_EX}# DUPLA: {Fore.RESET}{Fore.LIGHTGREEN_EX}{dupla}{Fore.RESET}")
    print(f"{Fore.LIGHTYELLOW_EX}# UNA: {Fore.RESET}{Fore.LIGHTGREEN_EX}{una}{Fore.RESET}")
    print(f"{Fore.LIGHTYELLOW_EX}# NENHUMA: {Fore.RESET}{Fore.LIGHTGREEN_EX}{nula}{Fore.RESET}")
    print(f"{Fore.GREEN}# {'=-=' * 20}=-==-==-==-{'=-=' * 20} {Fore.RESET}")