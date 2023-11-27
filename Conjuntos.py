numerosA = {0, 1, 3, 5, 7, 9} # conjuntos são iniciados utilizando as '{}', dentro de um conjunto não existe duplicidade, ou seja, mesmo que seja adicionado valores iguais, somente será considerado um dos valores, não duplicando seu uso.
numerosB = {3, 2, 4, 6, 8, 0}
numerosA.add(100) # O metodo 'add' adiciona um novo valor ao conjunto.
numerosA.discard(100) # O metodo 'discard' remove um item do conjunto.

print('Conjunto A contem {}'.format(numerosA))
print('Conjunto B contem {}'.format(numerosB))

numeros_uniao = numerosA.union(numerosB)#O metodo 'union' unifica conjuntos criando um universo, removendo a duplicidade e ja pondo em ordem crescente.
print('União de A + B: \n{}' .format(numeros_uniao))
numeros_intersecçao = numerosA.intersection(numerosB) # O metodo 'intersection' seleciona a intersecção entre os conjutos, ou seja, os objetos semelhantes entre eles.
print('Intersecção de A = B: \n{}' .format(numeros_intersecçao))
numeros_diferença = numerosA.difference(numerosB) # O metodo 'difference' seleciona os falores diferentes entre o conjunto primario e o secundario.
print('Diferença entre A != B: \n{}' .format(numeros_diferença))
numeros_diferença = numerosB.difference(numerosA)
print('Diferença entre B != A: \n{}' .format(numeros_diferença))
numeros_diferença_simetrica = numerosA.symmetric_difference(numerosB) # O metodos 'symmetric_difference' seleciona a diferença entre ambos os juntos, ou seja remove a intersecção.
print('Diferença simetrica entre A e B: \n{}'.format(numeros_diferença_simetrica))

#Pertinencias retornam como booleanos:
conjuntoA = {1, 2, 3}
print('Conjunto A: \n{}'.format(conjuntoA))
conjuntoB = {1, 2, 3, 4, 5,}
print('Conjunto B: \n{}'.format(conjuntoB))
conjuntoSubSet = conjuntoA.issubset(conjuntoB) #o Metodo 'issubset' verifica se um conjunto é sub-conjunto do outro.
print('A é sub Conjunto de B? \n {}'.format(conjuntoSubSet))
conjuntoSubSet = conjuntoB.issubset(conjuntoA) #o Metodo 'issubset' verifica se um conjunto é sub-conjunto do outro.
print('B é sub Conjunto de A? \n {}'.format(conjuntoSubSet))
conjuntoSuperSet = conjuntoA.issuperset(conjuntoB) #o Metodo 'issuperset' verifica se existe os itens de conjunto comparados e alem.
print('A é sub super-conjunto de B? \n {}'.format(conjuntoSuperSet))
conjuntoSuperSet = conjuntoB.issuperset(conjuntoA)
print('B é sub super-conjunto de A? \n {}'.format(conjuntoSuperSet))

listaAnimais = ['gato', 'gato', 'cachorro', 'cachorro', 'cachorro', 'elefante', 'boi']
print(listaAnimais)
conjuntoAnimais = set(listaAnimais) # convertendo uma lista para conjunto, voce remove as duplicidades.
print(conjuntoAnimais)