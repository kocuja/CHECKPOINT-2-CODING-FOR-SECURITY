import time
import sys
sys.setrecursionlimit(10**6)

def mergesort(senhas):
    if len(senhas) <= 1:
        return senhas
    meio = len(senhas) // 2
    esquerda = senhas[:meio]
    direita = senhas[meio:]
    esquerda_ordenada = mergesort(esquerda)
    direita_ordenada = mergesort(direita)
    return merge(esquerda_ordenada, direita_ordenada)

def merge(esquerda, direita):
    resultado = []
    i = j = 0
    while i < len(esquerda) and j < len(direita):
        if esquerda[i] < direita[j]:
            resultado.append(esquerda[i])
            i += 1
        else:
            resultado.append(direita[j])
            j += 1
    resultado += esquerda[i:]
    resultado += direita[j:]
    return resultado

# Abre o arquivo rockyou
senhas_total = open('rockyou.txt', "r", encoding='latin-1')
senhas = []
for index, text in enumerate(senhas_total):
    if 0 <= index <= 1000:
        senhas.append(text)


# Mede o tempo de execução do merge sort
inicio = time.time()
senhas_mergesort = mergesort(senhas)
fim = time.time()
print(f"Tempo de execução do merge sort: {fim - inicio} segundos")

senhas = [senha.rstrip('\n') for senha in senhas]

# Ordena as senhas em ordem crescente com merge sort.
senhas_mergesort = mergesort(senhas)

# Exibe as senhas ordenadas
print("Senhas ordenadas com merge sort:")
for senha in senhas_mergesort:
    print(senha)