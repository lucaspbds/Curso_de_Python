# Validação de Dados
r = 'S'
sexo = str(input('Digite o seu sexo [F/M]: ')).strip().upper()[0]
while sexo not in 'FM':
    sexo = str(input('Dados inválidos! Por favor, informe o seu sexo [M/F]: ')).strip().upper()[0]
print(f'Sexo {sexo} cadastrado com sucesso!')
