import time
import sys
sys.setrecursionlimit(10**6)

def quicksort(senhas):
    if len(senhas) <= 1:
        return senhas
    else:
        pivo = senhas[0]
        menores = [senha for senha in senhas[1:] if senha < pivo]
        maiores = [senha for senha in senhas[1:] if senha >= pivo]
        return quicksort(menores) + [pivo] + quicksort(maiores)

# Abre o arquivo rockyou
senhas_total = open('rockyou.txt', "r", encoding='latin-1')
senhas = []
for index, text in enumerate(senhas_total):
    if 0 <= index <= 1000:
        senhas.append(text)
    

# Mede o tempo de execução do quicksort
inicio = time.time()
senhas_quicksort = quicksort(senhas)
fim = time.time()
print(f"Tempo de execução do quicksort: {fim - inicio} segundos")

senhas = [senha.rstrip('\n') for senha in senhas]

# Ordena as senhas em ordem crescente com quicksort
senhas_quicksort = quicksort(senhas)

# Exibe as senhas ordenadas
print("Senhas ordenadas com quicksort:")
for senha in senhas_quicksort:
    print(senha)