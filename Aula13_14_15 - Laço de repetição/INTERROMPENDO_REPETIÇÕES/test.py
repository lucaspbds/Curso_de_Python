# # while True:
# #     break
# # print('OIIII')
# # while True:
# #     print('Amor')
# primos = list()
#
#
# def num_primos(num: int):
#     cont = 0
#     for i in range(1, num + 1):
#         if num % i == 0:
#             cont += 1
#     if cont == 2:
#         primos.append(num)
#
#
# while True:
#     num = int(input('Digite um número: '))
#     num_primos(num)
#     r = input('Deseja continuar?[S/N] ').strip().upper()[0]
#     if r == 'N':
#         break
# print('\033[31mPrograma finalizado!\033[m')
# print(f'Números primos:\033[32m{primos}')

from random import choice

par_impar = choice(['Par', 'Ímpar'])
print(par_impar[0])
