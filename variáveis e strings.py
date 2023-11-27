#a = 2 # inicializa uma variavél com um valor estatico (python reconhece o tipo de acordo com a inicialização).
#b = 3 # inicializa uma variavél com um valor estatico (python reconhece o tipo de acordo com a inicialização)..
a = int(input('entre com o primeiro valor: ')) #input captura os valores digitados como string.
b = int(input('entre com o segundo valor: ')) #input o valor a ser capturado deve ser convertido para o tipo desejado no ato da captura.
soma = a + b     #gera uma soma entre dois valores.
sub = a - b      #gera uma subtração entre dois valores.
mult = a * b     #gera uma multiplicação entre dois valores.
div = a / b      #gera uma divisão entre dois valores.
fatorial = a % b #gera um cálculo de resto entre dois valores.
#print(type(soma))  # o metodo 'type' identifica o tipo de uma variavel.
#soma = str(soma)   # conversão de tipo.
print('soma: ' + str(soma))   # concatenação com conversão de tipos.
print('sub: {}'.format(sub))  # interpolação de print
print('mult: {mult}'.format(mult=mult))  # interpolação com definição de "apelido".
#print(int(div))  # converte o valor float para int, arredondando (removendo o valor apos o ponto) o valor.
print('div: {} \nFatorial: {}'.format(div, fatorial)) # Formatando com quebra de linha "/n".

