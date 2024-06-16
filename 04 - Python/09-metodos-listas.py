# > Métodos de listas

lista = [1, 3, 5, 7]

# append - insere no final

print( 'Antes do append: ', lista)

lista.append(9)

print( 'Depois do append: ', lista)

# insert - escolhe a posição do insert

lista.insert(2, 11)

print( 'Depois do insert: ', lista)

# extend - junta duas listas, adicionando no final

lista2 = [13, 15, 17]

lista.extend(lista2)

print( 'Depois do extend: ', lista)

# pop - remove o elemento, caso não informado a posição do elemento, remove o ultimo

lista.pop()

print( 'Depois do pop: ', lista)

# remove - remove o elemento da lista (remove o primeiro elemento)

lista.remove(11)

print( 'Depois do remove: ', lista)

# count - conta quantas vezes o elemento está presente na lista

print('Quantidade de 5 na lista: ', lista.count(5))

# index - retorna a posição do elemento na lista

print('Indice do elemento 5: ', lista.index(5))

# sort - ordena os elemento da lista

lista.sort()

print('Ordem crescente: ', lista)

lista.sort(reverse=True)

print('Ordem decrescente: ', lista)