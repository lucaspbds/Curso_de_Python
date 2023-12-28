# Funções para votação


def voto(anoDeNascimento):
    from datetime import datetime
    ano = datetime.today().year
    idade = ano - anoDeNascimento
    if idade < 16:
        return f'Com {idade} anos: NÃO VOTA!'
    elif 18 <= idade < 65:
        return f'Com {idade} anos: VOTO OBRIGATÓRIO!'
    else:
        return f'Com {idade} anos: VOTO OPCIONAL!'


anoDeNascimento = int(input('Em que ano você nasceu? '))
print(voto(anoDeNascimento))
