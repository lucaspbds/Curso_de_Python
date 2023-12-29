import ast

dados = [['Lucas', 17], ['Maria', 30]]
file = open('bd.txt', 'a+')
for dado in dados:
    file.writelines(f'{dado},')
file.seek(0)

bd = file.readlines()[0]
print(bd)
result = ast.literal_eval(bd)
file.close()
print(result)

