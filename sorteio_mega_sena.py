# Bibliotecas
from colorama import Fore   # Colorir a saída no terminal
from random import randint  # Gerar números aleatórios


# Função de sorteio da Mega Sena
def sorteio_mega_sena(cartela, loop):

    ganhou = 0          # Contador de vitórias
    num_sorteio = []    # Lista dos sorteios ganhos

    for z in range(0, loop):

        cont = 0            # Contador de acertos
        acertos = []        # Lista de acertos
        maquina = set()     # Conjunto para números sorteados únicos
        var = "MegaSena"    # Nome da loteria para exibição

        # Exibe cartela do jogador
        print(f"\n\n{Fore.GREEN}# {'=-=' * 20} SORTEIO {z+1} {'=-=' * 20} {Fore.RESET}", end=" ")
        print(f"\n{Fore.LIGHTYELLOW_EX}# Palpites: {Fore.RESET}", end=" ")
        print(*cartela, end=" ")

        # Sorteia 6 números únicos para a máquina
        while len(maquina) < 6:

            # Sorteia números de 1 a 10
            maquina.add(randint(1, 10))

        # Exibe sorteio
        print(f"\n{Fore.BLUE}# Sorteando... {Fore.RESET}", end=" ")
        print(*var, end=" ")

        # Exibe números sorteados pela máquina
        print(f"\n{Fore.LIGHTYELLOW_EX}# Números sorteados: {Fore.RESET}", end=" ")
        print(*sorted(maquina), end=" ")

        # Verifica acertos
        for i in cartela:
            if i in maquina:
                cont += 1
                acertos.append(i)

        # Exibe resultado
        if cont == 6:
            print(f"\n\n{Fore.LIGHTCYAN_EX}# GANHOU! {Fore.RESET}")
            ganhou += 1
            num_sorteio.append(z + 1)

        else:
            print(f"\n\n{Fore.RED}# Perdeu! Acertou {cont}: {Fore.RESET} {' / '.join(map(str, acertos))}")

        print(f"\n{Fore.GREEN}# {'=-=' * 20} {'=-=' * 20} {Fore.RESET}", end=" ")

    # Exibe total de vitórias
    print(f"\n\n{Fore.LIGHTCYAN_EX}# GANHOU: {ganhou} {Fore.RESET}")
    print(f"{Fore.LIGHTCYAN_EX}# Números dos sorteios ganhos: {Fore.RESET} {' '.join(map(str, num_sorteio))}")
