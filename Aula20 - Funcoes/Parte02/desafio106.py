# Interactive helping system in Python
from time import sleep

cores = {
    'bgBrancoAzul': '\033[1;34;107m',
    'bgBrancoVermelho': '\033[1;31;107m',
    'limpar': '\033[m',
    'fgVermelho': '\033[1;31m',
    'fgAmarelo': '\033[1;33m',
    'bgPretoRosa': '\033[1;32;40m'
}


def ajuda(comand):
    return help(comand)


def title(texto):
    borda = 4
    qtdCaracteres = len(texto) + borda
    espaco = borda // 2
    print(f'{cores["bgBrancoAzul"]}={cores["limpar"]}' * qtdCaracteres)
    print(f'{cores["bgBrancoVermelho"]}' + ' ' * espaco + f'{texto}' + ' ' * espaco + f'{cores["limpar"]}')
    print(f'{cores["bgBrancoAzul"]}={cores["limpar"]}' * qtdCaracteres)


while True:
    title('Sistema de Ajuda do Python')
    comando = input("Digite uma função ou biblioteca que você tem dúvida: ").strip().lower()
    if comando == "fim":
        break
    print(f'{cores["fgAmarelo"]}Buscando a documentação do comando...{cores["limpar"]}')
    sleep(1.5)
    title(f"Manual do comando '{comando}'")
    print(f'{cores["bgPretoRosa"]}', end='')
    print(f'{ajuda(comando)}')
    print(f'{cores["limpar"]}', end='')

print(f'{cores["fgVermelho"]}<<PROGRAMA FINALIZADO>>{cores["limpar"]}')
