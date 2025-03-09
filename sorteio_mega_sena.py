# Bibliotecas
from colorama import Fore   # Colorir a saída no terminal
from random import randint  # Gerar números aleatórios
from relatorio import relatorio

# Função de sorteio da Mega Sena
def sorteio_mega_sena(cartela, loop):

    sena = 0
    quina = 0
    quadra = 0
    trinca = 0
    dupla = 0
    una = 0

    num_sorteio_sena = []
    num_sorteio_quina = []
    num_sorteio_quadra = []
    num_sorteio_trinca = []
    num_sorteio_dupla = []
    num_sorteio_una = []

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

            # Sorteia números de 1 a 60
            maquina.add(randint(1, 60))

        # Exibe sorteio
        print(f"\n{Fore.BLUE}# Sorteando... {Fore.RESET}", end=" ")
        print(var, end="")

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
            print(f"\n\n{Fore.LIGHTCYAN_EX}# GANHOU A SENA !!!!!! {Fore.RESET}")
            sena += 1
            num_sorteio_sena.append(z + 1)

        elif cont == 5:
            print(f"\n\n{Fore.LIGHTCYAN_EX}# GANHOU A QUINA !!!!!! {Fore.RESET}")
            quina += 1
            num_sorteio_quina.append(z + 1)

        elif cont == 4:
            print(f"\n\n{Fore.LIGHTCYAN_EX}# GANHOU A QUADRA !!!!!! {Fore.RESET}")
            quadra += 1
            num_sorteio_quadra.append(z + 1)

        elif cont == 3:
            print(f"\n\n{Fore.LIGHTCYAN_EX}# Acertou 3 vezes !!!!!! {Fore.RESET}")
            trinca += 1
            num_sorteio_trinca.append(z + 1)

        elif cont == 2:
            print(f"\n\n{Fore.LIGHTCYAN_EX}# Acertou 2 vezes !!!!!! {Fore.RESET}")
            dupla += 1
            num_sorteio_dupla.append(z + 1)

        elif cont == 1:
            print(f"\n\n{Fore.LIGHTCYAN_EX}# Acertou 1 vez !!!!!! {Fore.RESET}")
            una += 1
            num_sorteio_una.append(z + 1)

        else:
            print(f"\n\n{Fore.RED}# Perdeu! Acertou {cont}: {Fore.RESET} {' / '.join(map(str, acertos))}")

    relatorio(sena, quina, quadra, trinca, dupla, una)