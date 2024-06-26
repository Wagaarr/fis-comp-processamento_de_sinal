import numpy as np
import matplotlib.pyplot as plt
from dcst import dct2, dst2, idct2

###### ler os dados ######
def ler_dados(arquivo):
    with open(arquivo, 'r') as file:
        linhas = file.readlines()   
        dados = []
        for linha in linhas:
            dados.append([int(valor) for valor in linha.split()])
    return np.array(dados)


###### dividir 16x16, aplicar a DCT ######
def aplicar_dct(array, m=16):
    altura, largura = array.shape
    array_transf = np.zeros_like(array)
    
    for i in range(0, altura, m):
        for j in range(0, largura, m):
        
            bloco = array[i:i+m, j:j+m]
            bloco_transf = dct2(bloco)
            array_transf[i:i+m, j:j+m] = bloco_transf
    
    return array_transf


###### dividir 16x16, aplicar a IDCT ######
def aplicar_idct(array, m=16):
    altura, largura = array.shape
    array_transf = np.zeros_like(array)
    
    for i in range(0, altura, m):
        for j in range(0, largura, m):
            bloco = array[i:i+m, j:j+m]
            bloco_transf = idct2(bloco)
            array_transf[i:i+m, j:j+m] = bloco_transf
    
    return array_transf

def def_intervalo_zero(array, lim_inf, lim_sup):
    array_mod = np.copy(array)
    mascara = (array_mod > lim_inf) & (array_mod < lim_sup)
    array_mod[mascara] = 0
    
    return array_mod

# Função para criar e mostrar o gráfico de densidade
def criar_grafico_de_densidade(array):
    plt.imshow(array, cmap='gray', interpolation='nearest')
    plt.colorbar()
    plt.title('Gráfico de Densidade')
    #plt.show()
    plt.imsave('imagem2000.tiff', array, cmap='gray')

def contar_zeros(array):
    return np.count_nonzero(array == 0), np.size(array)

###### dados e limites da mascara ######
arquivo = 'house.txt'
lim_inf = -2000
lim_sup = 2000

dados = ler_dados(arquivo)
dados_transformados = aplicar_dct(dados)
dados_tratados = def_intervalo_zero(dados_transformados, lim_inf, lim_sup)
dados_finais = aplicar_idct(dados_tratados)

###### Criar e mostrar o gráfico de densidade ######
#criar_grafico_de_densidade(dados_finais)

###### Contar o número de zeros no array modificado ######
count_dados = contar_zeros(dados_tratados)
    
###### Mostrar o número de zeros ######
print(f"Num de coeficientes iguais a 0: {count_dados[0]}")
print("Taxa de compressao:", (count_dados[0]/count_dados[1])*100, "%")








