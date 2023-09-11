from math import cos, tan, sin, radians
print('-='*10+'Seno, Cosseno e Tangente'+'=-'*10)
angulo = int(input('Digite o valor do ângulo: '))
print(f'Seno de {angulo}º: {sin(radians(angulo)):.2f} \nCosseno de {angulo}º: {cos(radians(angulo)):.2f} \nTangente de {angulo}: {tan(radians(angulo)):.2f}')
