# TC/5 = (TF – 32)/9
print('-='*10+'Conversor de Temperatura (C° e F°)' +'=-'*10)
modulo = float(input('Módulo da temperatura (valor): '))
print('-='*20)
print('Quer converter para qual unidade?')
print('1 - Cº \n2 - Fº')
undnova = input('Digite: ')
if undnova == '1':
    TC = ((modulo - 32)/9)*5
    print(f'{modulo}Fº em Celsius: {TC:.2f}Cº')
if  undnova == '2':
    TF = ((modulo/5)*9)+32
    print(f'{modulo}Fº em Celsius: {TF:.2f}Fº')