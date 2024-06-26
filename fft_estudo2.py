import numpy as np 
from scipy.fftpack import dct, idct
import matplotlib.pyplot as plt

###### ler os dados do arquivo txt ######
def amostra(nome_arquivo):
    with open(nome_arquivo, 'r') as arquivo:
        dados = [float(linha.strip()) for linha in arquivo]
    return dados

###### Fazer FFT ######
def fft(dados_tratados):
    FFT_amostra = np.fft.rfft(dados_tratados)
    return FFT_amostra

###### Fazer FFT inverso ######
def ifft(dados_tratados):
    IFFT_amostra = np.fft.irfft(dados_tratados)
    return IFFT_amostra

###### Fazer DCT ######
def dct_(dados_tratados):
    DCT_amostra = dct(dados_tratados, type=2, norm='ortho')
    return DCT_amostra

###### Fazer DCT inverso ######
def idct_(dados_tratados):
    IDCT_amostra = idct(dados_tratados, type=2, norm='ortho')
    return IDCT_amostra

###### plotar os dados ######

def plot(dados, FFT_amostra, dados_tratados10,dados_tratados2,dados_tratados2_dct,dados_tratados90,dados_tratados98, IFFT_amostra, IFFT_amostra2, IFFT_amostra3,IFFT_amostra4,IDCT_amostra):
    plt.figure(figsize=(12, 6))
    plt.plot(dados, label='amostra', color='red')
    #plt.plot(FFT_amostra, label='fft', color='cyan')
    #plt.plot(dados_tratados10, label='fft 10%', color='green')
    #plt.plot(dados_tratados2, label='fft 2%', color='green')
    #plt.plot(dados_tratados2_dct, label='dct 2%', color='purple')
    #plt.plot(dados_tratados90, label='fft 90%', color='green')
    #plt.plot(dados_tratados98, label='fft 98%', color='green')
    #plt.plot(IFFT_amostra, label='ifft 10%', color='green')
    plt.plot(IFFT_amostra2, label='ifft 2%', color='blue')
    #plt.plot(IFFT_amostra3, label='ifft 90%', color='purple')
    #plt.plot(IFFT_amostra4, label='ifft 98%', color='purple')
    plt.plot(IDCT_amostra, label='idct 2%', color='purple')
    plt.title(nome_print2)
    plt.xlabel('dias uteis')
    plt.ylabel('preco medio')
    plt.legend()
    plt.grid(True)
    plt.show()

###### tratamento dados (porcentagem) ######

def set_(dados, porcentagem):
 
    dados_preservados = int(len(dados) * porcentagem)
    resultado = np.copy(dados)
    resultado[dados_preservados:] = 0
    
    return resultado

def set_2(dados, porcentagem):
 
    dados_preservados = int(len(dados) * porcentagem)
    resultado = np.copy(dados)
    resultado[:dados_preservados] = 0
    
    return resultado

###### Nome do arquivo de dados ######
nome_arquivo = 'dow2.txt'
nome_arq_split = nome_arquivo.split('.') 
nome_print2 = 'Amostra ' + nome_arq_split[0]


###### dados do projeto ######

dados = amostra(nome_arquivo)
FFT_amostra = fft(dados)
DCT_amostra = dct_(dados)
dados_tratados10 = set_(FFT_amostra, 0.1)
dados_tratados2 = set_(FFT_amostra, 0.02)
dados_tratados2_dct = set_(DCT_amostra, 0.02)
dados_tratados90 = set_2(FFT_amostra, 0.1)
dados_tratados98 = set_2(FFT_amostra, 0.02)
IFFT_amostra = ifft(dados_tratados10)
IFFT_amostra2 = ifft(dados_tratados2)
IFFT_amostra3 = ifft(dados_tratados90)
IFFT_amostra4 = ifft(dados_tratados98)
IDCT_amostra = idct_(dados_tratados2_dct)

###### Plotar os dados ######

plot(dados, FFT_amostra, dados_tratados10,dados_tratados2,dados_tratados2_dct,dados_tratados90,dados_tratados98, IFFT_amostra, IFFT_amostra2, IFFT_amostra3,IFFT_amostra4,IDCT_amostra)
