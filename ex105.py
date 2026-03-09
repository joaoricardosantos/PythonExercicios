def notas(*n, sit=False):
    """
    -> Função para analisar notas e situações de vários alunos.
    :parametro n: um ou mais notas dos alunos (aceita várias).
    :parametro sit: (opcional), indicando se deve ou não adicionar a situação.
    :return: dicionário com várias informações sobre a turma.
    """
    r = dict()
    r['Total'] = len(n)
    r['Maior'] = max(n)
    r['Menor'] = min(n)
    r['Média'] = sum(n) / len(n)
    if sit:
        if r['Média'] >= 7:
            r['Situação'] = 'BOA'
        elif r['Média'] >= 5:
            r['Situação'] = 'RAZOÁVEL'
        else:
            r['Situação'] = 'RUIM'
    return r


resp = notas(9, 10, 7.5, sit=True)
print(resp)
help(notas)