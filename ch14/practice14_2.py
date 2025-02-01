#practice of decorators
from functools import wraps
def only_int(fun):
    @wraps(fun)
    def wrapper(*args,**kwargs):                #this can also be written using list comprehension as
        data_type=[]                                #if(all[type(arg)==int for arg in args]):
        for arg in args:                                    # return fun(*args,**kwargs)
            data_type.append(type(arg)==int)        #return "invalid"
        if all(data_type):
            return fun(*args,**kwargs)
        else:
            return "invalid argument"
    return wrapper
@only_int
def add(*args):
    total=0
    for arg in args:
        total+=arg
    return total
print(add(1,2,3,4))  #o/p-->10
print(add(1,2,3,4,[1,2,3]))  #o/p-->invalid argument
print(add(1,2,3,4.5)) #o/p-->invalid argument

#decorator with arguments
from functools import wraps
def only_data_type_decorator(data_type): #this will take data type which is specified in the argument and will check if all the arguments are of that type or not
    def decorator(fun): 
        @wraps(fun)
        def wrapper(*args,**kwargs):                #this acn also be written using list comprehension as
            if all([type(arg)==data_type for arg in args]):
                return fun(*args,**kwargs)
            return "invalid"
        return wrapper
    return decorator
@only_data_type_decorator(str)
def add(*args):
    total=''
    for arg in args:
        total+=arg
    return total
print(add("abc","bcd")) #o/p-->abcbcd
print(add(1,2,3,4,[1,2,3]))  #o/p-->invalid 
print(add(1,2,3,4.5)) #o/p-->invalid 