class Televisao:
    def __init__(self):
        self.ligado = False
        self.canal = 5

    def power(self):
        if self.ligado: #em variaveis booleanas, a condicional sempre vai trabalhar com uma verificação verdadeira(True), caso o resultado n seja verdadeiro, por padrão ela seguira para a proxima verificação.
            self.ligado = False
        else:
            self.ligado = True

    def aumento_canal(self):
        self.canal += 1
    def reducao_canal(self):
        self.canal -= 1


if __name__ == '__main__': #Main faz com que o que está dentro dele seja executado apenas quando o arquivo ou modulo é executado, se o modulo for chamado de outra forma o que esta contido nele não é executado.
    televisao = Televisao()
    print ('A Tv está ligada? \n{}' . format(televisao.ligado))
    televisao.power()
    print ('A Tv está ligada? \n{}' . format(televisao.ligado))
    televisao.power()
    print ('A Tv está ligada? \n{}' . format(televisao.ligado))
    print ('A Tv está em qual canal? \n{}' . format(televisao.canal))
    televisao.aumento_canal()
    print ('A Tv está em qual canal? \n{}' . format(televisao.canal))
    televisao.aumento_canal()
    print ('A Tv está em qual canal? \n{}' . format(televisao.canal))
    televisao.aumento_canal()
    print ('A Tv está em qual canal? \n{}' . format(televisao.canal))
    televisao.reducao_canal()
    print ('A Tv está em qual canal? \n{}' . format(televisao.canal))
    televisao.reducao_canal()
    print ('A Tv está em qual canal? \n{}' . format(televisao.canal))