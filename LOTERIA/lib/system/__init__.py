from random import randint
from time import sleep
from LOTERIA.lib.interface import *
def mega():
    lista = []
    jogos = []
    print()
    cabecalho(f'\033[33m{"JOGO MEGA SENA"}\033[m')
    print()
    quant = int(input(f'\033[33mQuantos jogos? >>>   \033[m'.strip()))
    tot = 1
    while tot <= quant:
        cont = 0
        while True:
            num = randint(1, 60)
            if num not in lista:
                lista.append(num)
                cont += 1
            if cont >= 6:
                break
        lista.sort()
        jogos.append(lista[:])
        lista.clear()
        tot += 1
    print()
    cabecalho( f'\033[33mSORTEANDO {quant} Jogos\033[m')
    sleep(1)
    for i, l in enumerate(jogos):
        print(f'Jogo {i + 1}:  {l}')
        sleep(1)
    jogos.clear()


def lotofacil():
    lista = []
    jogos = []
    print()
    cabecalho(f'\033[33m{"JOGO LOTOFACIL"}\033[m')
    print()
    quant = int(input(f'\033[33mQuantos jogos? >>>   \033[m'.strip()))
    tot = 1
    while tot <= quant:
        cont = 0
        while True:
            num = randint(1, 25)
            if num not in lista:
                lista.append(num)
                cont += 1
            if cont >= 15:
                break
        lista.sort()
        jogos.append(lista[:])
        lista.clear()
        tot += 1
    print()
    cabecalho( f'\033[33mSORTEANDO {quant} Jogos\033[m')
    sleep(1)
    for i, l in enumerate(jogos):
        print(f'Jogo {i + 1}:  {l}')
        sleep(1)
    jogos.clear()


def quina():
    lista = []
    jogos = []
    print()
    cabecalho(f'\033[33m{"JOGO QUINA"}\033[m')
    print()
    quant = int(input(f'\033[33mQuantos jogos? >>>   \033[m'.strip()))
    tot = 1
    while tot <= quant:
        cont = 0
        while True:
            num = randint(1, 80)
            if num not in lista:
                lista.append(num)
                cont += 1
            if cont >= 5:
                break
        lista.sort()
        jogos.append(lista[:])
        lista.clear()
        tot += 1
    print()
    cabecalho( f'\033[33mSORTEANDO {quant} Jogos\033[m')
    sleep(1)
    for i, l in enumerate(jogos):
        print(f'Jogo {i + 1}:  {l}')
        sleep(1)
    jogos.clear()


def lotomania():
    lista = []
    jogos = []
    print()
    cabecalho(f'\033[33m{"JOGO LOTOMANIA"}\033[m')
    print()
    quant = int(input(f'\033[33mQuantos jogos? >>>   \033[m'.strip()))
    tot = 1
    while tot <= quant:
        cont = 0
        while True:
            num = randint(1, 99)
            if num not in lista:
                lista.append(num)
                cont += 1
            if cont >= 50:
                break
        lista.sort()
        jogos.append(lista[:])
        lista.clear()
        tot += 1
    print()
    cabecalho(f'\033[33mSORTEANDO {quant} Jogos\033[m')
    sleep(1)
    for i, l in enumerate(jogos):
        print(f'Jogo {i + 1}:  {l}')
        sleep(1)
    jogos.clear()


def milhonaria():
    lista = []
    jogos = []
    trevo =[]
    print()
    cabecalho(f'\033[33m{"MILIONARIA"}\033[m')
    print()
    quant = int(input(f'\033[33mQuantos jogos? >>>   \033[m'.strip()))
    tot = 1
    while tot <= quant:
        cont = 0
        while True:
            num = randint(1, 50)
            if num not in lista:
                lista.append(num)
                cont += 1
            if cont >= 6:
                break
        lista.sort()
        jogos.append(lista[:])
        lista.clear()
        tot += 1
    
    total = 1
    while total <= quant:
        cont = 0
        while True:
            num = randint(1, 6)
            if num not in lista:
                lista.append(num)
                cont += 1
            if cont >= 2:
                break
        lista.sort()
        trevo.append(lista[:])
        lista.clear()
        total += 1

    print()
    cabecalho( f'\033[33mSORTEANDO {quant} Jogos\033[m')
    sleep(1)
    for i, l in enumerate(jogos):
        print(f'Jogo {i + 1}:  {l}')
        sleep(1)
    jogos.clear()
        
    for i, l in enumerate(trevo):
        print(f'Jogo {i + 1}:  {l}')
        sleep(1)
    trevo.clear()
