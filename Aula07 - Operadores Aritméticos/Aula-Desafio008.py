print('=-'*10+'Conversão de Unidade'+'-='*10)
while True:
    n1 = float(input('Valor da medida: '))
    und = input('Unidade de medida (Km,Hm,Dam,M,Dm,Cm e Mm): ').upper()
    print('-='*20)
    print('CONVERTER PARA:')
    print()
    print('1 - Km', end=' '*5)
    print('2 - Hm')
    print('3 - Dam', end=' '*4)
    print('4 - M')
    print('5 - Dm', end=' '*5)
    print('6 - Cm')
    print('7 - Mm')
    opc = input('Digite: ')
    if (und == 'KM' and opc != '1') and opc == '2':
        print(f'Valor convertido: {n1*10} hm')
    if (und == 'KM' and opc != '1') and opc == '3':
        print(f'Valor convertido: {n1 * 100} dam')
    if (und == 'KM' and opc != '1') and opc == '4':
        print(f'Valor convertido: {n1*1000} m')
    if (und == 'KM' and opc != '1') and opc == '5':
        print(f'Valor convertido: {n1*10000} dm')
    if (und == 'KM' and opc != '1') and opc == '6':
        print(f'Valor convertido: {n1*100000} cm')
    if (und == 'KM' and opc != '1') and opc == '7':
        print(f'Valor convertido: {n1*1000000} mm')
    if (und == 'KM' and opc == '1'):
        print('Não pode transformar para a mesma unidade de medida!')

    if (und == 'HM' and opc != '2') and opc == '1':
        print(f'Valor convertido: {n1/10} km')
    if (und == 'HM' and opc != '2') and opc == '3':
        print(f'Valor convertido: {n1*10} dam')
    if (und == 'HM' and opc != '2') and opc == '4':
        print(f'Valor convertido: {n1/100} m')
    if (und == 'HM' and opc != '2') and opc == '5':
        print(f'Valor convertido: {n1/1000} dm')
    if (und == 'HM' and opc != '2') and opc == '6':
        print(f'Valor convertido: {n1/10000} cm')
    if (und == 'HM' and opc != '2') and opc == '7':
        print(f'Valor convertido: {n1/10} mm')
    if und == 'HM' and opc != '2':
        print('Não pode transformar para a mesma unidade de medida!')

    if (und == 'DAM' and opc != '3') and opc == '1':
        print(f'Valor convertido: {n1/100} km')
    if (und == 'DAM' and opc != '3') and opc == '2':
        print(f'Valor convertido: {n1/10} hm')
    if (und == 'DAM' and opc != '3') and opc == '4':
        print(f'Valor convertido: {n1*10} m')
    if (und == 'DAM' and opc != '3') and opc == '5':
        print(f'Valor convertido: {n1*100} dm')
    if (und == 'DAM' and opc != '3') and opc == '6':
        print(f'Valor convertido: {n1*1000} cm')
    if (und == 'DAM' and opc != '3') and opc == '7':
        print(f'Valor convertido: {n1*10000} mm')
    if und == 'DAM' and opc == '3':
        print('Não pode transformar para a mesma unidade de medida!')

    if (und == 'M' and opc != '4') and opc == '1':
        print(f'Valor convertido: {n1/1000} km')
    if (und == 'M' and opc != '4') and opc == '2':
        print(f'Valor convertido: {n1/100} hm')
    if (und == 'M' and opc != '4') and opc == '3':
        print(f'Valor convertido: {n1/10} dam')
    if (und == 'M' and opc != '4') and opc == '5':
        print(f'Valor convertido: {n1*10} dm')
    if (und == 'M' and opc != '4') and opc == '6':
        print(f'Valor convertido: {n1*100} cm')
    if (und == 'M' and opc != '4') and opc == '5':
        print(f'Valor convertido: {n1*1000} mm')
    if und == 'M' and opc == '4':
        print('Não pode transformar para a mesma unidade de medida!')

    if (und == 'DM' and opc != '5') and opc == '1':
        print(f'Valor convertido: {n1/10000} km')
    if (und == 'DM' and opc != '5') and opc == '2':
        print(f'Valor convertido: {n1/1000} hm')
    if (und == 'DM' and opc != '5') and opc == '3':
        print(f'Valor convertido: {n1/100} dam')
    if (und == 'DM' and opc != '5') and opc == '4':
        print(f'Valor convertido: {n1/10} m')
    if (und == 'DM' and opc != '5') and opc == '6':
        print(f'Valor convertido: {n1*10} cm')
    if (und == 'DM' and opc != '5') and opc == '6':
        print(f'Valor convertido: {n1*100} mm')
    if und == 'DM' and opc == '5':
        print('Não pode transformar para a mesma unidade de medida!')

    if (und == 'CM' and opc != '6') and opc == '1':
        print(f'Valor convertido: {n1/100000} km')
    if (und == 'CM' and opc != '6') and opc == '2':
        print(f'Valor convertido: {n1/10000} hm')
    if (und == 'CM' and opc != '6') and opc == '3':
        print(f'Valor convertido: {n1/1000} dam')
    if (und == 'CM' and opc != '6') and opc == '4':
        print(f'Valor convertido: {n1/100} m')
    if (und == 'CM' and opc != '6') and opc == '5':
        print(f'Valor convertido: {n1/10} dm')
    if (und == 'CM' and opc != '6') and opc == '7':
        print(f'Valor convertido: {n1*10} mm')
    if und == 'CM' and opc == '6':
        print('Não pode transformar para a mesma unidade de medida!')

    if (und == 'MM' and opc != '7') and opc == '1':
        print(f'Valor convertido: {n1/1000000} km')
    if (und == 'MM' and opc != '7') and opc == '2':
        print(f'Valor convertido: {n1/100000} hm')
    if (und == 'MM' and opc != '7') and opc == '3':
        print(f'Valor convertido: {n1/10000} dam')
    if (und == 'MM' and opc != '7') and opc == '4':
        print(f'Valor convertido: {n1/1000} m')
    if (und == 'MM' and opc != '7') and opc == '5':
        print(f'Valor convertido: {n1/100} dm')
    if (und == 'MM' and opc != '7') and opc == '6':
        print(f'Valor convertido: {n1/10} cm')
    if und == 'MM' and opc == '7':
        print('Não pode transformar para a mesma unidade de medida!')
    finalizar = input('Deseja continuar? S ou N').upper()
    if finalizar == 'N':
        print('Programa finalizado!')
        break