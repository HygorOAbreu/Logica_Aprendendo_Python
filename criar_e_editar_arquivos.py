# arquivo = open('teste.txt', 'a') #utilizado para abrir arquivos e editalos via sisstema, o 'W' é para informar um escrita no arquivo.
# # ao utilizar o 'A' ao invez do 'W' ele escreve um novo contéudo no arquivosempre o atualizando, e se nescessario criando um novo arquivo.
# arquivo.write('\nminha primeira escrita') #'write' utilizado para escrever diretamente no arquivo.
# arquivo.close() #utilizado para fechar um arquivo aberto.
import shutil
def escrever_arquivo(texto): # cria e escreve o texto desejado em um arquivo, sempre substituindo o anterior.
    diretorio = 'E:/Git/python/logica/teste.txt' #é possivel definir um diretorio expecifico.
    arquivo = open(diretorio, 'w')
    arquivo.write(texto)
    arquivo.close()

def atualizar_arquivo(nome_arquivo, texto): #cria e atualiza o texto desejado em um arquivo, sempre mantedo as informações anteriores.
    arquivo = open(nome_arquivo, 'a')
    arquivo.write(texto+'\n')
    arquivo.close()

def ler_arquivo(nome_arquivo): # faz a leitura de um tipo de arquivo.
    arquivo = open(nome_arquivo, 'r')
    texto = arquivo.read()
    print(texto)
def media_notas(nome_arquivo):
    arquivo = open(nome_arquivo, 'r')
    aluno_nota = arquivo.read()
    aluno_nota = aluno_nota.split('\n') #converte uma informação em lista com base em um parametro, no caso um 'enter (\n)'.
    lista_media = []
    for x in aluno_nota:
        lista_notas = x.split(',')
        aluno = lista_notas[0]
        lista_notas.pop(0)
        #print(aluno)
        #print(lista_notas)
        media = lambda notas: sum([int(i) for i in notas])/4 #faz uma busca na lista de notas, converte para int, soma os valores e devolve uma média.
        #print(media(lista_notas))
        lista_media.append({aluno: media(lista_notas)})
    return lista_media

def copia_arquivo(nome_arquivo): #copiar os arquivos para um novo diretorio
    shutil.copy(nome_arquivo, 'E:/Git/python/logica/')

def mover_arquivo(nome_arquivo):
    shutil.move(nome_arquivo, 'E:/Git/python/logica/')

if __name__ == '__main__':
    #lista_media =  media_notas('nota.txt')
    #print(lista_media)
    #escrever_arquivo('primeira linha\n')
    #aluno = 'Diogo,8,10,9,8'
    #atualizar_arquivo('nota.txt',aluno)
    #ler_arquivo('teste.txt')
    #copia_arquivo('nota.txt')
    #mover_arquivo('novo.txt')