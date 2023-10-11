
import timeit

chamadas = 0

def sequencia_fib(numero):
    global chamadas
    chamadas += 1
    if numero == 0 or numero == 1:
        return numero
    else:
        return sequencia_fib(numero - 2) + sequencia_fib(numero - 1)

numero = int(input("Que termo você deseja encontrar? "))



resultado = sequencia_fib(numero)
final_time = timeit.default_timer()


print(f'Para o número {numero}, foram realizadas {chamadas} chamadas.')
print(f'O valor da sequência de Fibonacci para {numero} é {resultado}.')
print(f'Tempo de execução: {final_time} segundos.')
       