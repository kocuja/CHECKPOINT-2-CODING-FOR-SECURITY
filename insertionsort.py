import time
import sys
sys.setrecursionlimit(10**6)

def insertionsort(senhas):
    for i in range(1, len(senhas)):
        chave = senhas[i]
        j = i - 1
        while j >= 0 and senhas[j] > chave:
            senhas[j + 1] = senhas[j]
            j -= 1
        senhas[j + 1] = chave
    return senhas


# abre o arquivo rockyou
senhas_total = open('rockyou.txt', "r", encoding='latin-1')
senhas = []
for index, text in enumerate(senhas_total):
    if 0 <= index <= 1000:
        senhas.append(text)


# Mede o tempo de execução do insertion sort
inicio = time.time()
senhas_insertionsort = insertionsort(senhas)
fim = time.time()
print(f"Tempo de execução do insertion sort: {fim - inicio} segundos")

senhas = [senha.rstrip('\n') for senha in senhas]

# Ordena as senhas em ordem crescente com insertion sort
senhas_insertionsort = insertionsort(senhas)

# Exibe as senhas ordenadas
print("Senhas ordenadas com insertion sort:")
for senha in senhas_insertionsort:
    print(senha)