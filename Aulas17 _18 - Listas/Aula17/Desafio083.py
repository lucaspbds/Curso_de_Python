expressao = input('Digite a expressão: ').strip()
pilha = []
for simbolo in expressao:
    if simbolo == '(':
        pilha.append(simbolo)
    elif simbolo == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('\033[32mSua expressão está válida!')
else:
    print('\033[31mSua expressão está errada!')
