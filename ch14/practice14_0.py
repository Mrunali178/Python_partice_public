#intro
def squares(a):
    return a**2
print(squares(6)) #o/p--> 36
s=squares(7)
print(s) #o/p--> 49
s=squares
print(s(5)) #o/p--> 25


print(s)    #o/p--> <function squares at 0x00000239F9561440>
print(squares) #o/p--> <function squares at 0x00000239F9561440>
print(s.__name__)  #o/p--> squares
print(squares.__name__)  #o/p--> squares
#this means both are same and are at same memory location and are equal

## pass function as argument
# jese map me hota h (function,iterable) pass krte h same we can create our own function

nums=[1,2,3] 
map_object=list(map(squares,nums))
print(map_object)   #o/p--> [1, 4, 9]

map_object1=list(map(lambda a:a**3,nums))
print(map_object1)   #o/p--> [1, 8, 27]


#this will work same as map_object
def my_map(func,l):
    new_list=[]
    for i in l:
        new_list.append(func(i))
    return new_list
print(my_map(squares,nums))  #o/p--> [1, 4, 9]
print(my_map(lambda a: a**3,nums)) #o/p-->[1, 8, 27]


#can be done using list comprehension
def my_map1(fun,a):
    return [fun(i) for i in a]

print(my_map1(squares,nums))  #o/p--> [1, 4, 9]
print(my_map1(lambda a: a**3,nums)) #o/p-->[1, 8, 27]

#function returning function (also called as closure and first class function)

def outer_func():
    def inner_func():
        print("this is inner function")
    return inner_func
var=outer_func() # no o/p...this var will contain the outer function and execute it but since we are not calling inner function in return with () it will be executed only when we write var()
print(var)  #o/p--> <function outer_func.<locals>.inner_func at 0x000001D8963B8360>
var()       #o/p--> this is inner function
print(var())  #o/p--> this is inner function
                      # None
#Explanation:
# return inner_func:

# This returns the inner_func itself (the function object) without executing it.
# The outer_func does not execute inner_func—it just returns the reference to it.
# var = outer_func():

# The outer_func is executed, and its result is assigned to var.
# Since outer_func returns inner_func (the function object), var now holds a reference to inner_func.
# var():

# Now, we execute inner_func by calling var().
# This prints this is inner function.
# print(var()):

# First, var() is executed, printing this is inner function.
# Then, since inner_func doesn’t return anything (implicitly returns None), the print statement outputs None after the function's execution.

def outer_func():
    def inner_func():
        print("this is inner function")
    return inner_func()
var=outer_func() #o/p--> this is inner function
# this var will contain the outer function and execute it directly and print the result

# Explanation:
# return inner_func():

# This executes the inner_func immediately and returns its result.
# The inner_func prints this is inner function when executed, but since it has no return statement, it returns None.
# var = outer_func():

# The outer_func executes, which in turn executes inner_func.
# The result of inner_func (which is None) is assigned to var.
# print(var):

# Since var holds the result of inner_func (i.e., None), this prints None.


def outer_func2(msg):
    def inner_func2():
        print(f"this is msg from outer {msg}")
    return inner_func2
var=outer_func2("Helloo!!!")
var() #o/p--> this is msg from outer Helloo!!!

#closures practice
#calculate the ans when power is provided along with number.  power can be anything like sqaure cube 4 etc
def to_power(x):
    def calc(num):
        return num**x
    return calc

cube=to_power(3)
print(cube(2))  #o/p--> 8

cube=to_power(3)
print(cube(5))  #o/p--> 125

square=to_power(2)
print(square(3)) #o/p--> 9 
