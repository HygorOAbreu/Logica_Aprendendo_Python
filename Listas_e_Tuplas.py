numeros = [32, 1, 3, 5, 7]
animais = ['cachorro', 'gato', 'elefante']
mista = [1, 2, 3, 'cachorro', 1.2, 1.10] #É possivel ter tipos diferentes dentro de uma mesma lista, porem não é o recomendado por convenção.
# print (animais[0]) # è possivel acessar um item da lista definindo sua posição, lembrando que sempre se inicia o contador por 0.
# print ( numeros [2])

# for x in animais: percorre toda a lista armazenando o valor em x e printando.
#     print(x)
print (sum(numeros)) # o metodo 'sum' soma todos os valores dentro de uma lista.
print (max(numeros)) # o metodo 'max' revela o maior valor da lista,quando utilizado com string, leva em consideração a inicial da palavra na ordem alfabetica.
print (min(numeros)) #o metodo 'min' revela o menor valor da lista,quando utilizado com string, leva em consideração a inicial da palavra na ordem alfabetica.

if 'gato' in mista:  # busca por algo expecífico dentro da lista.
    print ('existe um gato na lista')
else:
    print ('Não existem um gato na lista')

nova_animais = animais * 3 #É possivel multiplicar os dados contidos em uma lista.
print(nova_animais)

animais.append('lobo') # metodo 'append' adiciona um novo item a lista.
print(animais)
animais.pop(0) #O metodo 'pop' caso n defina parametro remove o ultimo item da lista, caso contrario remove a posição informada.
print(animais)
animais.remove('elefante') #O metodo remove um item expecifico idependente da posição na lista)
print(animais)
animais.sort() # o metodo 'sort' ordena os itens contidos na lista de forma crescente.
numeros.sort() # o metodo 'sort' ordena os itens contidos na lista de forma crescente.
print(animais)
print(numeros)
numeros.reverse() # o metodo 'reverse' ordena os itens contidos na lista de forma decrescente.
print(numeros)
len(numeros) #o metodo'len' conta quantos elementos  existem dentro da lista ou tupla
numeros[0] = 100 # Listas são mutaveis, permitindo a substituição ou adição de valores/itens.
print(numeros)
tupla = (1 ,5 ,7 ,9 ,12) #tuplas são semelhantes a listas, porem são iniciadas com () ao invés de [] e são imutaveis.
print (tupla)
tupla_animais = tuple(animais) #É possivel converter uma lista em tupla, e para isso usamos o tipo 'Tuple'.
print(tupla_animais)
lista_tupla = list(tupla) #É possivel converter uma tupla em lista, e para isso usamos o tipo 'list'.
print(lista_tupla)