from time import sleep

cores = {
    'verde': '\033[1;32m',
    'clean': '\033[m',
    'vermelho': '\033[31m',
    'amarelo': '\033[33m',
    'azul': '\033[34m',
    'magenta': '\033[1;35m'
}

agenda = dict()


def verificacao_contato(nome: str):
    print(f'{cores["amarelo"]}Verificando se o contato já existe...{cores["clean"]}')
    sleep(2)
    if nome not in agenda:
        return False
    else:
        return True


def adicionar_contato(nome: str, telefone: str):
    agenda[nome] = telefone
    print(f'{cores["verde"]}Contato adicionado com sucesso!{cores["clean"]}')


def editar_contato(nome: str, telefone: str):
    agenda[nome] = telefone
    print(f'{cores["verde"]}Telefone alterado com sucesso!{cores["clean"]}')

def apagar_contato(nome: str):
    del agenda[nome]
    print(f'{cores["verde"]}Contato apagado com sucesso!{cores["clean"]}')

while True:
    print(f'{cores["azul"]}='*44)
    print(f'{cores["amarelo"]}{"AGENDA TELEFÔNICA":^44}{cores["clean"]}')
    print(f'{cores["azul"]}={cores["clean"]}'*44)
    print(f"""
{cores['verde']}1 - {cores['clean']}Adicionar contato    {cores['verde']}4 - {cores['clean']}Apagar contato
{cores['verde']}2 - {cores['clean']}Editar telefone      {cores['verde']}5 - {cores['clean']}Listar todos
{cores['verde']}3 - {cores['clean']}Pesquisar contato    {cores['verde']}6 - {cores['clean']}Sair
    """)
    opcao = input(f'{cores["magenta"]}Digite a sua escolha: {cores["clean"]}').strip()
    while opcao not in '123456':
        print(f'{cores["vermelho"]}Erro de digitação! Por favor, digite novamente...{cores["clean"]}')
        opcao = input('Digite a sua escolha: ').strip()
    if opcao == '1':
        print('-=-' * 10)
        print(f'{cores["verde"]}{"ADICIONAR CONTATO":^30}{cores["clean"]}')
        print('-=-' * 10)
        nome = input('Digite o nome do contato: ').strip().capitalize()
        if verificacao_contato(nome) == False:
            telefone = input('Digite o telefone do contato: ').strip()
            adicionar_contato(nome, telefone)
        else:
            print(f'{cores["vermelho"]}Esse contato já existe na sua agenda telefônica!{cores["clean"]}')
    elif opcao == '2':
        print('-=-' * 10)
        print(f'{cores["verde"]}{"EDITAR TELEFONE":^30}{cores["clean"]}')
        print('-=-' * 10)
        nome = input('Digite o nome do contato: ').strip().capitalize()
        if verificacao_contato(nome) == True:
            print(f'Nome: {nome}  -  Telefone: {agenda["telefone"]}')
            telefone = input('Digite o novo telefone: ').strip()
            editar_contato(nome, telefone)
        else:
            print(f'{cores["vermelho"]}Esse contato não existe!{cores["clean"]}')
    elif opcao == '3':
        print('-=-' * 10)
        print(f'{cores["verde"]}{"PESQUISAR CONTATO":^30}{cores["clean"]}')
        print('-=-' * 10)
        nome = input('Digite o nome do contato: ').strip().capitalize()
        if verificacao_contato(nome) == True:
            print(f'Nome: {nome}  -  Telefone: {agenda[nome]}')
        else:
            print(f'{cores["vermelho"]}Esse contato não existe!{cores["clean"]}')
    elif opcao == '4':
        print('-=-' * 10)
        print(f'{cores["verde"]}{"APAGAR CONTATO":^30}{cores["clean"]}')
        print('-=-' * 10)
        nome = input('Digite o nome do contato: ').strip().capitalize()
        if verificacao_contato(nome) == True:
            apagar_contato(nome)
        else:
            print(f'{cores["vermelho"]}Esse contato não existe!{cores["clean"]}')
    elif opcao == '5':
        print('-=-' * 10)
        print(f'{cores["verde"]}{"CONTATOS":^30}{cores["clean"]}')
        print('-=-' * 10)
        for nome, telefone in agenda.items():
            print(f'{cores["azul"]}{nome}{cores["clean"]}  -  {cores["amarelo"]}{telefone}{cores["clean"]}')

    elif opcao == '6':
        break
print(f'{cores["vermelho"]}PROGRAMA FINALIZADO!')
