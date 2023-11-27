class calculadora:  # a palavra 'class' inicializa uma classe.
    def __init__(self):  # o init nunca deve ser vazio, porem pode ser sem parametros inicializados.
        pass  # metodo que permite 'passar' esté etapa.

    def soma(a, b):
        return a + b

    def sub(a, b):
        return a - b

    def mult(a, b):
        return a * b

    def div(a, b):
        return a / b

    def resto(a, b):
        return a % b


print(' O valor da Soma de A + B é: \n{}'.format(calculadora.soma(10, 12)))
print(' O valor da Subtração de A - B é: \n{}'.format(calculadora.sub(10, 12)))
print(' O valor da Divisão de A / B é: \n{}'.format(calculadora.div(10, 12)))
print(' O valor da Multiplicação de A * B é: \n{}'.format(calculadora.mult(10, 12)))
print(' O valor do Resto de A % B é: \n{}'.format(calculadora.resto(10, 12)))
