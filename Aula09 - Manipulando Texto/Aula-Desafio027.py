print('=-'*10+'Primeiro e último nome de uma pessoa'+'-='*10)
nome = input('Digite o seu nome: ').strip().split()
print('Seja Bem-Vindo {} {}!'.format(nome[0], nome[len(nome)-1]))
