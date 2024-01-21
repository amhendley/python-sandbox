
import timeit

print('***** NO CACHING *****')
print("Time taken:", timeit.timeit('''\
def fibonacci_nocache(n: int) -> int:
    if n <= 1:
        return n
    return fibonacci_nocache(n - 1) + fibonacci_nocache(n - 2)


for i in range(40):
    print(fibonacci_nocache(i))
''', number=1))


print('\n\n***** WITH CACHING *****')
print("Time taken:", timeit.timeit('''\
from functools import cache

@cache
def fibonacci(n: int) -> int:
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


for i in range(40):
    print(fibonacci(i))
''', number=1))
