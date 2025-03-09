from colorama import Fore

def relatorio(sena, quina, quadra, trinca, dupla, una):

    # Exibe total de vitórias
    print(f"\n{Fore.GREEN}# {'=-=' * 20} RELATORIO {'=-=' * 20} {Fore.RESET}", end=" ")
    print(f"\n{Fore.LIGHTYELLOW_EX}# SENA: {Fore.RESET}{Fore.LIGHTGREEN_EX}{sena}{Fore.RESET}")
    print(f"{Fore.LIGHTYELLOW_EX}# QUINA: {Fore.RESET}{Fore.LIGHTGREEN_EX}{quina}{Fore.RESET}")
    print(f"{Fore.LIGHTYELLOW_EX}# QUADRA: {Fore.RESET}{Fore.LIGHTGREEN_EX}{quadra}{Fore.RESET}")
    print(f"{Fore.LIGHTYELLOW_EX}# TRINCA: {Fore.RESET}{Fore.LIGHTGREEN_EX}{trinca}{Fore.RESET}")
    print(f"{Fore.LIGHTYELLOW_EX}# DUPLA: {Fore.RESET}{Fore.LIGHTGREEN_EX}{dupla}{Fore.RESET}")
    print(f"{Fore.LIGHTYELLOW_EX}# UNA: {Fore.RESET}{Fore.LIGHTGREEN_EX} {una}{Fore.RESET}")
    print(f"{Fore.GREEN}# {'=-=' * 20} RELATORIO {'=-=' * 20} {Fore.RESET}")

# # Exibe total de vitórias
# print(f"\n\n{Fore.LIGHTYELLOW_EX}# SENA: {sena} {Fore.RESET}")
# #print(f"{Fore.LIGHTCYAN_EX}# Números dos sorteios ganhos: {Fore.RESET} {' '.join(map(str, num_sorteio_sena))}")
#
# print(f"\n\n{Fore.LIGHTYELLOW_EX}# QUINA: {quina} {Fore.RESET}")
# #print(f"{Fore.LIGHTCYAN_EX}# Números dos sorteios ganhos: {Fore.RESET} {' '.join(map(str, num_sorteio_quina))}")
#
# print(f"\n\n{Fore.LIGHTYELLOW_EX}# QUADRA: {quadra} {Fore.RESET}")
# #print(f"{Fore.LIGHTCYAN_EX}# Números dos sorteios ganhos: {Fore.RESET} {' '.join(map(str, num_sorteio_quadra))}")
#
# print(f"\n\n{Fore.LIGHTYELLOW_EX}# TRINCA: {trinca} {Fore.RESET}")
# #print(f"{Fore.LIGHTCYAN_EX}# Números dos sorteios ganhos: {Fore.RESET} {' '.join(map(str, num_sorteio_trinca))}")
#
# print(f"\n\n{Fore.LIGHTYELLOW_EX}# DUPLA: {dupla} {Fore.RESET}")
# #print(f"{Fore.LIGHTCYAN_EX}# Números dos sorteios ganhos: {Fore.RESET} {' '.join(map(str, num_sorteio_dupla))}")
#
# print(f"\n\n{Fore.LIGHTYELLOW_EX}# UNA: {una} {Fore.RESET}")
# #print(f"{Fore.LIGHTCYAN_EX}# Números dos sorteios ganhos: {Fore.RESET} {' '.join(map(str, num_sorteio_una))}")