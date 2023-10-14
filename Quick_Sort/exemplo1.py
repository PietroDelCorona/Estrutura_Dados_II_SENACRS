#FreeCodeCamp

import random

z=[random.randint(0,100) for i in range(0,20)]
print("---------------------------------------")
print("Array pré-ordenação:", z)
def quicksort(z):
    if(len(z)>1):        
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
        
ans1=quicksort(z)
