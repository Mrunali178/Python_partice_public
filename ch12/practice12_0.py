# lambda expression (anonymous function)
# used with built in functions like reduce map filter here is just for understanding we will se it using variable
# normal function 
def add(a,b):
    return a+b

# using lambda
add2=lambda a,b:a+b 
print(add2(2,3))  #o/p---> 5

mul=lambda a,b:a*b
print(mul(2,3)) #o/p---> 6

print(add) #o/p---> <function add at 0x000001BB1FEE1440>
print(add2) #o/p---> <function <lambda> at 0x000001BB200F8220>
print(mul) #o/p---> <function <lambda> at 0x000001BB200F8180>
# this (shows) means there is no name for lambda function