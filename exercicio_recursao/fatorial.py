'''
Pseudocódigo Exercicio Recursão
1 . def função
2. Print
3. Chamar a def
4. Critério de Parada (contador)
'''

# Como calcular o fatorial de algum número

def calcular_fatorial(numero, contador=0):
    if numero == 0:
        return 1, contador
    else:
        contador += 1
        resultado, chamadas_recursivas = calcular_fatorial(numero - 1, contador)
        return numero * resultado, chamadas_recursivas

numero = int(input("Digite o número que você quer calcular o fatorial: "))
resultado, chamadas_recursivas = calcular_fatorial(numero)
print(f'O fatorial de {numero} é {resultado}, calculado em {chamadas_recursivas} chamadas recursivas')

