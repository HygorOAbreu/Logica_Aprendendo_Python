#lambda são funções anonimas compactas
from typing import Callable, Any

contador_letras = lambda lista: [len(x) for x in lista]
    # def contador_letras(lista_palavras): mesma função de forma compacta.
    #     contador = []
    #     for x in lista_palavras:
    #         quantidade = len(x)
    #         contador.append(quantidade)
    #     return contador
lista = ['gato','cachorro','rã']
letras = contador_letras(lista)
print(letras)

# soma = lambda a, b: a + b
# sub = lambda  a, b: a - b
# print(soma(5,10))
# print(sub(10,5))

calculadora = { #sintax de um dicionario
    'soma': lambda a, b: a + b,
    'sub': lambda a, b: a - b,
    'mult': lambda a, b: a * b,
    'div': lambda a, b: a / b,
}
soma = calculadora['soma']
print(soma(5,10))


