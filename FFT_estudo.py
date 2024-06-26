import numpy as np 
import matplotlib.pyplot as plt

###### ler os dados do arquivo txt ######
def amostra(nome_arquivo):
    with open(nome_arquivo, 'r') as arquivo:
        dados = [float(linha.strip()) for linha in arquivo]
    return dados

###### Fazer FFT ######
def fft(dados, n, sample_rate):
    FFT_amostra = np.fft.rfft(dados[:10000])
    freqs = np.fft.fftfreq(n, d=1/sample_rate)
    return FFT_amostra, freqs

###### plotar os dados ######

def plot_amostra(dados):
    plt.figure(figsize=(10, 4))
    plt.plot(dados, label='Amplitude')
    plt.title(nome_print2)
    plt.xlabel('tempo')
    plt.ylabel('Amplitude')
    plt.legend()
    plt.grid(True)
    plt.show()

def plot_fft(FFT_amostra, freqs, nome_print):
    plt.figure(figsize=(10, 6))
    plt.plot(freqs[:n//2], np.abs(FFT_amostra)[:n//2])  #espectro positivo
    plt.title(nome_print)
    plt.xlabel('Freq (Hz)')
    plt.ylabel('Magnitude')
    plt.xlim(0,5000)
    plt.grid()
    plt.show()


###### n de pontos e sample rate ######
n = 10000
sample_rate = 44100

###### Nome do arquivo de dados ######
nome_arquivo = 'trumpet.txt'
nome_arq_split = nome_arquivo.split('.') 
nome_print = 'FFT ' + nome_arq_split[0]
nome_print2 = 'Amostra ' + nome_arq_split[0]


###### Ler dados do arquivo ######
dados = amostra(nome_arquivo)
FFT_amostra, freqs = fft(dados, n, sample_rate)

###### Plotar os dados ######
plot_amostra(dados)
plot_fft(FFT_amostra, freqs, nome_print)






    













