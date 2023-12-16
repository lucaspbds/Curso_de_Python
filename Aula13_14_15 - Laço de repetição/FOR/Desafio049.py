print('-=-'*10+'Tabuada v2.0'+'-=-'*10)
num = int(input('Qual tabuada você quer saber (1, 2, 3,...)?\n'))
for i in range(0, 11):
    print(f'{num} x {i} = {num*i}')
    