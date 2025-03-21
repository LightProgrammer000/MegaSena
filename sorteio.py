"""
# Metodo: Sorteio Mega Sena
"""

# Bibliotecas
from colorama import Fore
from random import randint
from report import relatorio

# Funcao de sorteio da Mega Sena
def sorteio_mega_sena(cartela, loop):

    # Variaveis de controle
    sena = 0; quina = 0; quadra = 0; trinca = 0; dupla = 0; una = 0; nula = 0

    # Quantidade de sorteios
    for l in range(0, loop):

        # Variaveis
        cont = 0        # Contador de acertos
        maquina = set() # Conjunto para numeros sorteados unicos

        """ Player: Exibe cartela do jogador """
        print(f"\n\n{Fore.GREEN}# {'=-=' * 20} SORTEIO {l + 1} {'=-=' * 20} {Fore.RESET}", end=" ")
        print(f"\n{Fore.LIGHTYELLOW_EX}# Palpites: {Fore.RESET}", end=" ")
        print(*cartela, end=" ")

        """ Maquina: Sorteia 6 numeros unicos para a maquina """
        while len(maquina) < 6:
            maquina.add(randint(1, 60))

        # Exibe numeros sorteados pela maquina (* -> Descompactando lista)
        print(f"\n{Fore.BLUE}# Sorteando... {Fore.RESET}", end=" ")
        print(f"\n{Fore.LIGHTBLUE_EX}# Numeros sorteados: {Fore.RESET}", end=" ")
        print(*sorted(maquina), end=" ")

        """ Exibicao de resultados """

        # Resultado: Cartela e Maquina
        for i in cartela:
            if i in maquina:
                cont += 1
    
        # Exibe resultado
        print(f"\n\n{Fore.LIGHTRED_EX}# RESULTADO: {Fore.RESET}", end="")

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

        print(f"\n{Fore.GREEN}# {'=-=' * 20}=-==-==-==-{'=-=' * 20} {Fore.RESET}")

    # Chamada de funcao: Relatorio
    relatorio(sena, quina, quadra, trinca, dupla, una, nula)