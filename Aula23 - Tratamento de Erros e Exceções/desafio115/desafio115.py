from funcoes.titulos import *
from funcoes.menu import *
from BancoDeDados import *

while True:
    titulo('menu principal', cor=True)
    menu('ver pessoas cadastradas', 'cadastrar uma nova pessoa', 'sair do programa', cor=True)
    op = str(input('\033[33mSua opção: \033[m')).strip()
    if op == '1':
        titulo('pessoas cadastradas', cor=True)
        listarCadastros()

    elif op == '2':
        titulo('Novo Cadastro', cor=True)
        cadastrarPessoa()

    elif op == '3':
        titulo('Programa finalizado', cor=True)
        print('\033[1;32mVolte sempre! =D\033[m')
        break
    else:
        print('\033[31mNÃO EXISTE ESSA OPÇÃO!\033[m')
