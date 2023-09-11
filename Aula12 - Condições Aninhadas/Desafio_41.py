print('=-'*10+'Classificando Atletas'+'-='*10)
from datetime import date
ano_atual = date.today().year
ano_nascimento = int(input('Digite o seu ano de nascimento: '))
idade = ano_atual - ano_nascimento
print('De acordo com a sua idade ({} anos),'.format(idade),end=' ')
if idade <= 9:
    print('a sua categoria é MIRIM.')
elif idade <= 14:
    print('a sua categoria é INFANTIL.')
elif idade <= 19:
    print('a sua categoria é JUNIOR.')
elif idade == 20:
    print('a sua categoria é SÊNIOR.')
else:
    print('a sua categoria é MASTER.')
    