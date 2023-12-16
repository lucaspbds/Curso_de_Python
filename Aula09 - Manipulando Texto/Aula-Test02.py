frase = 'Curso em Vídeo Python'
print(len(frase))
print(frase[3:14])
print(frase[:14])
print(frase[:20:3])
print(frase[0])
print(frase[::2])
print(frase[0::2])

print("""Motivação para a vida

Talvez você esteja preocupado(a) demais,
desanimado com essa ou aquela situação.
Vivendo sob grande tensão.
Sem saber por onde ir ou como fazer.
Pois vou lhe dar alguns motivos para melhorar.
mesmo sem grandes recursos financeiros,
mesmo sem médico, sem analista e sem dor.""")
print(frase.split())
print('-'.join(frase.upper().split()))
print(frase.upper().count('O'))
frase2 = '   Curso em Vídeo Python         '
print(frase2)
print(len(frase2))
print(frase2.strip())
print(len(frase2.strip()))
print(frase.replace('Python', 'Android'))
print(frase)
frase3 = frase.replace('Python', 'Android')
print(frase3)
print('Curso' in frase)
print(frase.find('Curso'))
print(frase.find('curso'))
print(frase.lower().find('curso'))
