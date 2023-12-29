import ast


def listarCadastros():
    try:
        file = open('bd', 'rt')
        file.seek(0)
        dado = file.readlines()[0]
        bd = ast.literal_eval(dado)
        for dados in bd:
            if dados[1] == '1':
                print(f'{dados[0]:<50}{dados[1]} ano')
            else:
                print(f'{dados[0]:<50}{dados[1]} anos')
        file.close()
    except FileNotFoundError:
        print('\033[1;31mNÃO HÁ CADASTROS NO MOMENTO!\033[m')


def cadastrarPessoa():
    nome = input('Nome: ').strip().title()
    idade = input('Idade: ').strip()
    pessoa = tratamentoDeDados(nome, idade)
    try:
        file = open('bd', 'at')
        file.write(f'{pessoa},')
        file.close()
    except FileNotFoundError:
        print('\033[31mErro ao tentar cadastrar o usuário!\033[m')
    else:
        print(f'<{pessoa[0]}> \033[32mcadastrado(a) com sucesso!\033[m')


def tratamentoDeDados(nome, idade):
    while True:
        if nome == '':
            nome = '<desconhecido>'
        if idade.isnumeric():
            pessoa = [nome, idade]
            return pessoa
        else:
            print(f'\033[31mErro: valor inválido na idade ({idade}).\033[m')
            idade = input('Idade: ').strip()
