# write a decorator to calculate the execution time of the function
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
def square_finder(n):
    return [i**2 for i in range(1,n+1)]
square_finder(1000)