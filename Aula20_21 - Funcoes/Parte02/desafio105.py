# Analisando e gerando Dicionários
bd = {}


def notas(*nota, sit=False):
    """
    => Função que recebe notas dos alunos e faz uma análise, mostrando a quantidade de notas,
    maior ou menor nota, média da Turma e a situação da turma (opcional).
    :param nota: uma ou mais notas dos alunos (aceita várias);
    :param sit: indica se deve mostrar ou não a situação da turma (opcional);
    :return: dicionário com a análise das notas.
    """
    bd['qtdDeNotas'] = len(nota)
    bd['maiorNota'] = max(nota)
    bd['menorNota'] = min(nota)
    media = sum(nota) / len(nota)
    bd['mediaDaTurma'] = media
    if sit:
        if bd['mediaDaTurma'] < 6:
            bd['situacao'] = 'RUIM'
        elif bd['mediaDaTurma'] < 7:
            bd['situacao'] = 'RAZOÁVEL'
        else:
            bd['situacao'] = 'BOA'
    return bd


resp = notas(5.5, 9.5, 10, 6.5, sit=True)
print(resp)
# help(notas)