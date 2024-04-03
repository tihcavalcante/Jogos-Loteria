from LOTERIA.lib.interface import *
from LOTERIA.lib.system import *

while True:
    resp = menu(['Mega-Sena', 'Lotofácil', 'Quina', 'Lotomania', 'Milhonaria', 'Sair'])
    if resp == 1:
        mega()
        print()
        print('Estes foram os jogos sorteados BOA SORTE !!!')
        sleep(10)

    elif resp == 2:
        lotofacil()
        print()
        print('Estes foram os jogos sorteados BOA SORTE !!!')
        sleep(10)

    elif resp == 3:
        quina()
        print()
        print('Estes foram os jogos sorteados BOA SORTE !!!')
        sleep(10)

    elif resp == 4:
        lotomania()
        print()
        print('Estes foram os jogos sorteados BOA SORTE !!!')
        sleep(10)

    elif resp == 5:
        milhonaria()
        print()
        print('Estes foram os jogos sorteados BOA SORTE !!!')
        sleep(10)        

    elif resp == 6:
        cabecalho('\033[32mSaindo do sistema... Até Logo!\033[m')
        break
    else:
        print('\033[31mErro!! Digite uma opção\033[m')


