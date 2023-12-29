def leiaInt(label: str):
    while True:
        try:
            num = int(input(label).strip())
        except KeyboardInterrupt:
            num = 0
            print('\n\033[31mO usuário preferiu não digitar esse número.\033[m')
            return num
        except:
            print('\033[31mErro: Digite um número inteiro válido.\033[m')
        else:
            return num


def leiaFloat(label: str):
    while True:
        try:
            num = float(input(label).strip())
        except KeyboardInterrupt:
            num = 0
            print('\n\033[31mO usuário preferiu não digitar esse número.\033[m')
            return num
        except:
            print('\033[31mErro: Digite um número float válido.\033[m')
        else:
            return num
