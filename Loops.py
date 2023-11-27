# for x in range(100): # laço 'for'
#     print(x)

a = int(input('entre com um valor: '))
count = 0
for x in range(1, a+1): # for percorre todo o valor dentro do range fazendo a verificação.
    if a % x == 0:
        count += 1 # concatena o valor atual da variavel com um valor a escolha, no caso, soma 1 ao valor existente.
if count == 2:
    print(' o valor {} é um número primo'.format(a))
else:
    print(' O valor {} não é um número primo'.format(a))