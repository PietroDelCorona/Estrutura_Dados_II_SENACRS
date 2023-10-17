import random 
import time

def bubbleSort(arr):
    n = len(arr)
     
    # Traverse through all array elements
    for i in range(n):
        swapped = False
 
        # Last i elements are already in place
        for j in range(0, n-i-1):
 
            # Traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if (swapped == False):
            break
 
 
# Driver code to test above
if __name__ == "__main__":
    #arr = [64, 34, 25, 12, 22, 11, 90]
    arr = [random.randint(0,50000) for i in range(0,50000)]
    inicio = time.time()
    bubbleSort(arr)
    fim = time.time()
 
    #print("Sorted array:")
    #for i in range(len(arr)):
        #print("%d" % arr[i], end=" ")
    
    tempo_execucao = fim - inicio
    print(f"Tempo de execucao: {tempo_execucao:.6f} segundos")