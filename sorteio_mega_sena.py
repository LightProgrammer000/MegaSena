"""
# Metodo: Sorteio Mega Sena
"""

# Bibliotecas
from colorama import Fore   # Colorir a saída no terminal
from random import randint  # Gerar números aleatórios
from relatorio import relatorio

# Função de sorteio da Mega Sena
def sorteio_mega_sena(cartela, loop):

    # Variavei de controle
    sena = 0
    quina = 0
    quadra = 0
    trinca = 0
    dupla = 0
    una = 0
    nula = 0

    for z in range(0, loop):

        cont = 0            # Contador de acertos
        maquina = set()     # Conjunto para numeros sorteados unicos

        # Exibe cartela do jogador
        print(f"\n\n{Fore.GREEN}# {'=-=' * 20} SORTEIO {z+1} {'=-=' * 20} {Fore.RESET}", end=" ")
        print(f"\n{Fore.LIGHTYELLOW_EX}# Palpites: {Fore.RESET}", end=" ")
        print(*cartela, end=" ")

        # Sorteia 6 números unicos para a maquina
        while len(maquina) < 6:

            # Sorteia números de 1 a 60
            maquina.add(randint(1, 60))

        # Exibe sorteio
        print(f"\n{Fore.BLUE}# Sorteando... {Fore.RESET}", end=" ")

        # Exibe numeros sorteados pela maquina (* -> Descompactando lista)
        print(f"\n{Fore.LIGHTYELLOW_EX}# Números sorteados: {Fore.RESET}", end=" ")
        print(*sorted(maquina), end=" ")

        # Verifica acertos
        for i in cartela:
            if i in maquina:
                cont += 1

        # Exibe resultado
        print(f"\n{Fore.LIGHTRED_EX}# Resultado: {Fore.RESET}", end="")

        if cont == 6:
            print(f"{Fore.LIGHTCYAN_EX} SENA !!!!!! {Fore.RESET}", end="")
            sena += 1

        elif cont == 5:
            print(f"{Fore.LIGHTCYAN_EX} QUINA !!!!! {Fore.RESET}", end="")
            quina += 1

        elif cont == 4:
            print(f"{Fore.LIGHTCYAN_EX} QUADRA !!!! {Fore.RESET}", end="")
            quadra += 1

        elif cont == 3:
            print(f"{Fore.LIGHTCYAN_EX} TRINCA !!! {Fore.RESET}", end="")
            trinca += 1

        elif cont == 2:
            print(f"{Fore.LIGHTCYAN_EX} DUPLA !! {Fore.RESET}", end="")
            dupla += 1

        elif cont == 1:
            print(f"{Fore.LIGHTCYAN_EX} UNA !! {Fore.RESET}", end="")
            una += 1

        else:
            print(f"{Fore.RED} NENHUMA ! {Fore.RESET}", end="")
            nula += 1

        print(f"\n{Fore.GREEN}# {'=-=' * 20} SORTEIO {z + 1} {'=-=' * 20} {Fore.RESET}", end=" ")
        print("")

    # Chamada de funcao
    relatorio(sena, quina, quadra, trinca, dupla, una, nula)