print('=-'*10+'Maior e menor valores'+'-='*10)
n1 = int(input('Primeiro número: ').strip())
n2 = int(input('Segundo número: ').strip())
n3 = int(input('Terceiro número: ').strip())
menor = n1
maior = n1
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n2 and n3 < n1:
    menor = n3
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3
print('Maior: {} \nMenor: {}'.format(maior, menor))
