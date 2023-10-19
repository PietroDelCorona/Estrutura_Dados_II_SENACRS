#FreeCodeCamp

import random
import time

#z=[random.randint(0,500000) for i in range(0,500000)]
z=[random.randint(0,100) for i in range(0,20)]
print("---------------------------------------")
#print("Array pré-ordenação:", z)

def quicksort(z):
    if(len(z)>1):
        print("Array antes do algoritmo:", z)        
        piv=int(len(z)/2)
        val=z[piv]
        print("----------")
        print("Valor do pivô:", val)
        lft=[i for i in z if i<val]
        print("----------")
        print("subarray de elementos menores que o pivô:", lft)
        mid=[i for i in z if i==val]
        print("----------")
        print("subarray de elementos iguais que o pivô", mid)
        rgt=[i for i in z if i>val]
        print("----------")
        print("subarray de elementos maiores que o pivô", rgt)

        res=quicksort(lft)+mid+quicksort(rgt)
        print("---------------------------------")
        print("Array ordenado:", res)
        return res
    else:
        return z

inicio = time.time()        
quicksort(z)
fim = time.time()
tempo_execucao = fim - inicio
print(f"Tempo de execução: {tempo_execucao} segundos")
