# Decorators --> enhances the functionality of the functions

#suppose this is awesome i have to add to every function before executing the function
def decorator_function(any_function):
    def wrapper_function():
        print("This is awesome")
        any_function()
    return wrapper_function
def func1():
    print("this is function1")
func1() #o/p-->this is function1

func1=decorator_function(func1)
func1()
#o/p--> This is awesome
        # this is function1
#now instead of writing this we can directly use @ symbol i.e. called as syntatic sugar for decorators
@ decorator_function
def func2():
    print("this is function 2")
func2()  #o/p-->This is awesome
                # this is function 2


# but this has one problem if we pass parameter to func1 or func2 it will give error
# @decorator_function
# def func3(a,b):
#     return a+b
# func3(2,3) #o/p--> TypeError: decorator_function.<locals>.wrapper_function() takes 0 positional arguments but 2 were given
# this is because the wrapper class is been called when we use decorator_function and there is no parameter in it so we will have to pass *args and ** kwargs to wrraper function

def decorator_function1(any_function):
    def wrapper_function1(*args,**kwargs):
        '''this is wrapper function'''
        print("This is awesome")
        return any_function(*args,**kwargs)
    return wrapper_function1

@decorator_function1
def add(a,b):
    '''this is add function'''
    return a+b
print(add(2,3)) #o/p--> 5

#one more problem is when we are printing then this function is ok but if we return something than it will give error hence we have to return the anyfunction
#now it is complete decorator function but still one problem i.e when we write doc string for add function and see it will give docstring of wrraper class beacuse we are calling wrraper function to execute add i.e
print(add.__doc__) #o/p---> this is wrapper function
print(add.__name__) #o/p--> wrapper_function1
#so it is a probelem in add it shouls show docstring of add and function name as add but its showing wrapper so to solve this 
#we neend to import wraps module from functools

from functools import wraps
def decorator_function1(any_function):
    @wraps(any_function)
    def wrapper_function1(*args,**kwargs):
        '''this is wrapper function'''
        print("This is awesome")
        return any_function(*args,**kwargs)
    return wrapper_function1

@decorator_function1
def add(a,b):
    '''this is add function'''
    return a+b
print(add.__doc__) #o/p---> this is add function
print(add.__name__)  #o/p --> add

#practice 
# make a decorator of print_function_data 
#it should give output as function name whichever function is called and also the docstring written in that particular function 

from functools import wraps
def print_function_data(anyfunction):
    @wraps(anyfunction)
    def wrapper_fun(*args,**kwargs):
        '''this is warpper'''
        print(f"you are calling {anyfunction} function")  #o/p-->you are calling <function addition at 0x00000125393284A0> function
        return anyfunction(*args,**kwargs)
    return wrapper_fun
@print_function_data
def addition(a,b):
    '''this function takes 2 parameters and give there sum'''
    return a+b
print(addition(4,6)) #o/p--> 10
print(addition.__doc__)  #o/p--> this function takes 2 parameters and give there sum
print(addition.__name__)   #o/p--> addition


#can be written as:- 

from functools import wraps
def print_function_data(anyfunction):
    @wraps(anyfunction)
    def wrapper_fun(*args,**kwargs):
        '''this is warpper'''
        print(f"you are calling {anyfunction.__name__} function") #o/p--> you are calling addition function
        print(anyfunction.__doc__)   #o/p--> this function takes 2 parameters and give there sum
        return anyfunction(*args,**kwargs)
    return wrapper_fun

@print_function_data
def addition(a,b):
    '''this function takes 2 parameters and give there sum'''
    return a+b
print(addition(4,6)) #o/p--> 10