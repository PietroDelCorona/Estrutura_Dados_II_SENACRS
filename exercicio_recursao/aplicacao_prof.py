import timeit

def fib_iterativo(num):
    a, b = 0, 1  
    for _ in range(num):
        a, b = b, a + b  
    final_time = timeit.default_timer()
    return [num, final_time, a]

num = int(input('Digite um número para encontrar o seu Fibonacci: '))

num, final_time, fib_i = fib_iterativo(num)
print("Fibonacci Iterativo de %d: %d" % (num, fib_i))
print('Tempo: ' + str(final_time) + ' segundos')
