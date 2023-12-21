from datetime import datetime

ano = datetime.now().year
dados = dict()

dados['nome'] = input("Digite o seu nome completo: ")
dados['anoDeNascimento'] = int(input('Digite o seu ano de nascimento: '))
dados['idade'] = ano - dados['anoDeNascimento']
dados['ctps'] = input('Digite a numeração da sua carteira de trabalho (0 - Não tenho CTPS): ')
if dados['ctps'] != '0':
    dados['anoDeContratacao'] = int(input('Digite o ano de contratação: '))
    dados['idadeDeAposentar'] = (dados['anoDeContratacao'] + 35) - dados['anoDeNascimento']
    dados['salario'] = float(input('Digite o seu salário: R$'))
print("-=-" * 10 + "Dados" + "-=-" * 10)
print(f'Nome: {dados["nome"]}')
print(f'Ano de Nascimento: {dados["anoDeNascimento"]}')
print(f'Idade: {dados["idade"]}')
if dados["ctps"] != '0':
    print(f'CTPS: {dados["ctps"]}')
    print(f'Ano de contratação: {dados["anoDeContratacao"]}')
    print(f'Salário: R${dados["salario"]:.2f}')
    print(f'Idade que vai se aposentar: {dados["idadeDeAposentar"]}')
else:
    print(f'CTPS: Não tem!')
