import timeit

lista = []

def criar_lista(n,v):
    for i in range(1, n + 1):
        lista.append(i)
    return lista


def busca_binaria(l, v):
    #if not l:
        #return False, 0
    
    inicio = 0
    fim = len(l) - 1
    contador = 0

    while inicio <= fim:
        contador += 1
        meio = (inicio + fim) // 2
        if l[meio] == v:
            return True, contador
        elif l[meio] < v:
            inicio = meio + 1
        else:
            fim = meio - 1
    return False, contador

v = 1

tam = 10

lista = criar_lista(tam, v)

print(lista)

start_time = timeit.default_timer()

busca_binaria(lista, 1)

final_time = timeit.default_timer() - start_time

print('Tempo: ' + str(final_time) + ' segundos')


#vetor = (2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40)

#valor = int(input("Digite o valor que você deseja procurar: "))

#encontrado_binario, contador_binario = busca_binaria(vetor, valor)

#if encontrado_binario == True:
    #print(f"O valor {valor} foi encontrado na Busca Binária após {contador_binario} iterações.")
#else:
    #print(f"O valor {valor} não foi encontrado na Busca Binária após {contador_binario} iterações.")
