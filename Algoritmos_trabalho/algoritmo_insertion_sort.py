import random
import time

def insertionSort(arr):
 
    # Traverse through 1 to len(arr)
    for i in range(1, len(arr)):
 
        key = arr[i]
 
        # Move elements of arr[0..i-1], that are
        # greater than key, to one position ahead
        # of their current position
        j = i-1
        while j >= 0 and key < arr[j] :
                arr[j + 1] = arr[j]
                j -= 1
        arr[j + 1] = key
 
 
# Driver code to test above
arr = [12, 11, 13, 5, 6]
#arr = [random.randint(0,500000) for i in range(0,500000)]
#inicio = time.time()
insertionSort(arr)
for i in range(len(arr)):
    print ("% d" % arr[i])
#fim = time.time()
#tempo_execucao = fim - inicio
#print(f"Tempo de execução: {tempo_execucao} segundos")