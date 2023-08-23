
def busca_binaria(vetor, elemento):
    inicio = 0
    fim = len(vetor) - 1
    contador = 0

    while inicio <= fim:
        contador += 1
        meio = (inicio + fim) // 2
        if vetor[meio] == elemento:
            return True, contador
        elif vetor[meio] < elemento:
            inicio = meio + 1
        else:
            fim = meio - 1
    return False, contador



vetor = (2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40)

valor = int(input("Digite o valor que você deseja procurar: "))

encontrado_binario, contador_binario = busca_binaria(vetor, valor)

if encontrado_binario == True:
    print(f"O valor {valor} foi encontrado na Busca Binária após {contador_binario} iterações.")
else:
    print(f"O valor {valor} não foi encontrado na Busca Binária após {contador_binario} iterações.")
