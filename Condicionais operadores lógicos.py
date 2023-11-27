a = int(input('Primeir valor: '))
while a > 10:
    a = int(input(' valores digitados incorretos, Digite novamente um valor valido: ')) #validação de valores durante digitação.

b = int(input('Segundo valor: '))
while b > 10:
    b = int(input(' valores digitados incorretos, Digite novamente um valor valido: '))

c = int(input('Terceiro valor: '))
while c > 10:
    c = int(input(' valores digitados incorretos, Digite novamente um valor valido: '))

d = int(input('Quarto valor: '))
while d > 10:
    d = int(input(' valores digitados incorretos, Digite novamente um valor valido: '))

# if a <= 10 and b <= 10 and c <= 10 and d <= 10: #validação de valores após digitação
media = (a + b + c + d)/4
if media > 7:
    print('Sua média foi: {} ,Aprovado'.format(media))
else:
    print('Sua média foi: {} ,Reprovado'.format(media))
# else:
#     print(' valores digitados incorretos')
# if a > b and a > c:
#     print ('o maior valor é o primeiro valor: {}'.format(a))
# elif b > a and b > c:
#     print('o maior número é o segundo valor {}' .format(b))
# else:
#     print('o maior número é o terceiro valor{}'.format(c))
# print('Fim do programa')

# if a % 2 == 0 or b % 2 == 0:
#     print('foi digitado um valor Par')
# else:
#     print('Não foi digitado um valor Par')