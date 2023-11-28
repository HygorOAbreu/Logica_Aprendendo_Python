from Funções_e_classes_TV import Televisao #é possivel importar uma função de outro modulo desta maneira.
from Funções_e_classes_calc_1 import Calculadora
from contatdor_letras import contador_letras

televisao = Televisao()

print(televisao.ligado)
televisao.power()
print(televisao.ligado)
televisao.power()
print(televisao.ligado)

calculadora = Calculadora(5,7)
print(calculadora.soma())

lista = ['gato', 'sapo', 'girafa']
total_letras = contador_letras(lista)
print(total_letras)