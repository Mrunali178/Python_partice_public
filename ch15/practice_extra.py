#generate a fabonacci series using generator 
def fibonacci_generator(n):
    a, b = 0, 1
    if n == 1:
        yield a
    elif n >= 2:
        yield a
        yield b
        for i in range(1, n - 1):
            c = a + b
            a, b = b, c
            yield b
for num in fibonacci_generator(8):
    print(num)



#generator that yeilds fabonacci series upto n and calculate its execution time using decorator
from functools import wraps
import time
def calculate_time(function):
    @wraps(function)
    def wrapper_fun(*args,**kwargs):
        t1=time.time()
        returned_value=function(*args,**kwargs)
        t2=time.time()
        total_time=t2-t1
        print(f"function took {total_time} seconds to execute")
        return returned_value
    return wrapper_fun

@calculate_time
def fibonacci_generator(n):
    a, b = 0, 1
    while a <= n:
        yield a
        a, b = b, a + b
fib_gen = fibonacci_generator(8)
for num in fib_gen:
    print(num)
