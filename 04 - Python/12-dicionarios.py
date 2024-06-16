# Criando dicionários

dicionario = {}
dicionario = dict()

dicionario = {'nome': 'Matheus', 'idade': 30, 'altura': 1.80}

print(dicionario)
print(dicionario['altura'])

# adicionando elemento no dicionário

dicionario['programador'] = True

print(dicionario)

#iterando sobre um dicionario

for variavel in dicionario:
    print(variavel)

#testando a existencia de uma chava

print('peso' in dicionario)
print('altura' in dicionario)