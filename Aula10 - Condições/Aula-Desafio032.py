from datetime import date
print('=-'*10+'Ano Bissexto'+'-='*10)
print('Digite 0 se quiser saber se o ano atual é ou não bissexto\n')
ano = int(input('Digite um ano: ').strip())
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('{} é um ano bissexto!'.format(ano))
else:
    print('{} não é um ano bissexto!'.format(ano))

