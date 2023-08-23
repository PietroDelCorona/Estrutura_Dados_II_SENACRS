"""
Exercício 1:
Faça um programa que recebe vetor (lista comum) com 10 inteiros por um valor aleatório"""


def busca_sequencial(vetor, elemento):
    contador = 0
    for i in range(len(vetor)):
        contador += 1
        if vetor[i] == elemento:
            return True, contador
    return False, contador
    

vetor = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

value = int(input("Digite o valor que você deseja procurar: "))

encontrado, contador = busca_sequencial(vetor, value)

if encontrado == True:
    print(f"Achei! O valor que você procurou era o: {value}")
else:
    print(f"Não achei! O valor {value} não está nessa lista")

"""
Exercício 2:
Crie uma lista que repete o valor pelo tamanho da lista"""
print("=================")
import timeit


lista = []

def gerar_lista(tamanho, valor):
    start = timeit.default_timer()
    for i in range(tamanho):
        lista.append(valor)
    end =timeit.default_timer()
    print(f"Tempo de iteração da lista é: {float(end - start)}")
    return lista

tamanho = 10
valor = 1

nova_lista = gerar_lista(tamanho, valor)
print(nova_lista)
    
        
        

        
   