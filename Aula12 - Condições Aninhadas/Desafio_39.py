print('=-'*10+'Alistamento Militar'+'-='*10)
from datetime import date
ano_atual = date.today().year
ano_nascimento = int(input('Digite o seu ano de nascimento: '))
idade = ano_atual - ano_nascimento
if idade < 18:
    print('Ainda falta {} ano(s) para você se alistar ao serviço militar.'.format(18 - idade), end=' ')
    print('Seu alistamento será em {}.'.format(ano_atual+(18 - idade)))
elif idade == 18:
    print('Já está na hora de você se alistar ao serviço militar.')
else:
    print('Já passou {} ano(s) do tempo do alistamento.'.format(idade - 18))
