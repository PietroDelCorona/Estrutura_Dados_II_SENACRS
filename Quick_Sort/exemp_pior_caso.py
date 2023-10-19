
import random
import time

def quicksort_worst_case(A, low, high):
    if low < high:
        m = (low + high) // 2  # Escolha o elemento do meio como pivô

        A[low], A[m] = A[m], A[low]  # Troque o pivô com o primeiro elemento

        p = A[low]  # p é o pivô
        m = low  # S1 e S2 estão inicialmente vazios

        for k in range(low + 1, high + 1):
            if A[k] < p:
                m += 1
                A[k], A[m] = A[m], A[k]

        A[low], A[m] = A[m], A[low]

        quicksort_worst_case(A, low, m - 1)
        quicksort_worst_case(A, m + 1, high)

A = [random.randint(0, 500000) for i in range(0, 500000)]
#A = [57, 385, 24, 42, 3, 68, 94, 1, 12, 47, 33, 5]
#print("Array pré-quicksorting:", A)
#print("-----------------------")
inicio = time.time()
quicksort_worst_case(A, 0, len(A) - 1)
fim = time.time()
print("-----------------------------------------")
#print("Array organizado pelo quicksorting (pior caso)", A)
tempo_execucao = fim - inicio
print(f"Tempo de execucao:{tempo_execucao} segundos.")