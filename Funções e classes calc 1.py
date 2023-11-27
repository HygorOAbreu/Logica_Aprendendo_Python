# função é tudo que retorna valor.
# Metodo é tudo que n retorna valor, em python isso é chamado de definição e inicializado por 'def'.

class calculadora: #a palavra 'class' inicializa uma classe.
    def __init__(self, n1, n2): #O metodo '__init__(self) inicializa uma class.
        self.a = n1 #o Metodo 'self' é utilizado para se referir a propria variavel, permitindo que a mesma receba parametros diversos de forma definida.
        self.b = n2
    def soma(self):
        return self.a + self.b
    def sub (self):
        return self.a - self.b
    def mult (self):
        return self.a * self.b
    def div(self):
        return self.a / self.b
    def resto (self):
        return self.a % self.b

calculadora = calculadora(10,3) #instanciando a class.
print(' O valor instanciado em A é: \n{}'.format(calculadora.a))
print(' O valor instanciado em B é: \n{}'.format(calculadora.b))
print(' O valor da Soma de A + B é: \n{}'.format(calculadora.soma()))
print(' O valor da Subtração de A - B é: \n{}'.format(calculadora.sub()))
print(' O valor da Divisão de A / B é: \n{}'.format(calculadora.div()))
print(' O valor da Multiplicação de A * B é: \n{}'.format(calculadora.mult()))
print(' O valor do Resto de A % B é: \n{}'.format(calculadora.resto()))
# def soma(a,b):
#     return a + b
#
# print(soma(5,5))

# def media():
#     a = int(input('Primeir valor: '))
#     while a > 10:
#         a = int(input(
#             ' valores digitados incorretos, Digite novamente um valor valido: '))  # validação de valores durante digitação.
#
#     b = int(input('Segundo valor: '))
#     while b > 10:
#         b = int(input(' valores digitados incorretos, Digite novamente um valor valido: '))
#
#     c = int(input('Terceiro valor: '))
#     while c > 10:
#         c = int(input(' valores digitados incorretos, Digite novamente um valor valido: '))
#
#     d = int(input('Quarto valor: '))
#     while d > 10:
#         d = int(input(' valores digitados incorretos, Digite novamente um valor valido: '))
#
#     media = (a + b + c + d)/4
#     if media > 7:
#         print('Sua média foi: {} ,Aprovado'.format(media))
#     else:
#         print('Sua média foi: {} ,Reprovado'.format(media))
