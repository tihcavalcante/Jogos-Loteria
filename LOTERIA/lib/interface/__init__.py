def linha(tam =40):
    return '\033[32m-\033[m' * tam


def cabecalho(txt):
    print(linha())
    print(txt.center(46))
    print(linha())


def menu(lista):
    cabecalho(f'\033[33m{"MENU PRINCIPAL":^46}\033[m')
    c = 1
    for item in lista:
        print(f'\033[33m{c} - {item.upper()}\033[m')
        c += 1
    print(linha())
    opc = leia_int(f'\033[33mEscolha seu Jogo >>> \033[m')
    return opc


def leia_int(msg):
    while True:
        try:
            n = int(input(msg).strip())
        except (ValueError, TypeError):
            print('\033[31mERRO: digite um número inteiro válido.\033[m')
            continue
        except KeyboardInterrupt:
            print("\033[31mO usuário preferiu não digitar esse número\033[m")
            return 0
        else:
            return n