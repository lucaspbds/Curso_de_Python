ced50 = ced20 = ced10 = ced1 = 0
print('\033[32m=' * 30)
print(f"\033[33m{'BANCO DO BRASIL':^30}")
print('\033[32m=\033[m' * 30)

sacar = int(input('Que valor você quer sacar? R$'))
falta = sacar
if falta // 50 != 0:
    ced50 = falta // 50
    falta = falta - ced50 * 50
    print(f'Total de {ced50} cédulas de R$50')
if falta // 20 != 0:
    ced20 = falta // 20
    falta = falta - ced20 * 20
    print(f'Total de {ced20} cédulas de R$20')
if falta // 10 != 0:
    ced10 = falta // 10
    falta = falta - ced10 * 10
    print(f'Total de {ced10} cédulas de R$10')
if falta // 1 != 0:
    ced1 = falta // 1
    print(f'Total de {ced1} cédulas de R$1')
print('\033[32m=\033[m' * 30)
print('\033[36mVolte sempre ao BANCO DO BRASIL! Tenha um bom dia!')

# OUTRO JEITO
'''
print('\033[32m=' * 30)
print(f"\033[33m{'BANCO DO BRASIL':^30}")
print('\033[32m=\033[m' * 30)

sacar = int(input('Que valor você quer sacar? R$'))
total = sacar
ced = 50 
totced = 0
while True:
    if total >= ced:
        total -= ced
        totced += 1
    else:
        if totced != 0:
           print(f'Total de {totced} cédulas de R${ced}')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totalced = 0  
        if total == 0:
        break
print('\033[32m=\033[m' * 30)
print('\033[36mVolte sempre ao BANCO DO BRASIL! Tenha um bom dia!')
'''
