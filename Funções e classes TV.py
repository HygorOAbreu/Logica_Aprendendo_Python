class televisao:
    def __init__(self):
        self.ligada = False
        self.canal = 5

    def power(self):
        if self.ligada: #em variaveis booleanas, a condicional sempre vai trabalhar com uma verificação verdadeira(True), caso o resultado n seja verdadeiro, por padrão ela seguira para a proxima verificação.
            self.ligada = False
        else:
            self.ligada = True

    def aumento_canal(self):
        self.canal += 1
    def reducao_canal(self):
        self.canal -= 1

televisao = televisao()
print ('A Tv está ligada? \n{}' . format(televisao.ligada))
televisao.power()
print ('A Tv está ligada? \n{}' . format(televisao.ligada))
televisao.power()
print ('A Tv está ligada? \n{}' . format(televisao.ligada))
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