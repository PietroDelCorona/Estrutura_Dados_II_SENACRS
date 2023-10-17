import random
import time

#A = [64, 25, 12, 22, 11]
A = [random.randint(0,50000) for i in range(0,50000)]
 
inicio = time.time()
# Traverse through all array elements
for i in range(len(A)):
     
    # Find the minimum element in remaining 
    # unsorted array
    min_idx = i
    for j in range(i+1, len(A)):
        if A[min_idx] > A[j]:
            min_idx = j
             
    # Swap the found minimum element with 
    # the first element        
    A[i], A[min_idx] = A[min_idx], A[i]
fim = time.time()
# Driver code to test above
#print ("Sorted array")
#for i in range(len(A)):
    #print("%d" %A[i],end=" , ")

tempo_execucao = fim - inicio
print(f"Tempo de execução: {tempo_execucao} segundos")