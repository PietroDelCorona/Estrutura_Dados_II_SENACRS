"""
Exercício 1:
Faça um programa que recebe vetor (lista comum) com 10 inteiros por um valor aleatório"""

import timeit

lista = []

def criar_lista(n, v):
    for i in range(n):
        lista.append(v)
    return lista

def busca_sequencial(l,v):
    for i in l:
        if v == l[i]:
            print("Achou\n")

    

v = 1
tam = 10000

lista = criar_lista(tam, v)

print(lista)

start_time = timeit.default_timer()

busca_sequencial(lista, 1)

final_time = timeit.default_timer() - start_time
print("Tempo: " + str(final_time) + " segundos")
        
        

        
   