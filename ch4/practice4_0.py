# functions
def add_two(a,b): # to define a function in python we use def
    return a+b # this willl return sum of a+b
total=add_two(5,4) # here we are calling funtion 5,4 are arguments whose sum we have to find
print(total)  # this will print the sum

# user input
a=int(input("Enter a num: "))
b=int(input("Enter another num: "))
def add(x,y):
    return x+y
print(add(a,b))

#string concatenation
f=input("enter first name: ")
l=input("enter last name: ")
print(add(f,l))

# create fuction which will return the last character of the string
def last_ch(name):
    return name[-1]
name=input("enter your name: ")
print(last_ch(name))

# create function to tell wheater number is odd or even
def odd_even(a):
    if (a%2==0):    # can also be wrriten as--> def odd_even(a):
        return "even"  #                                if(a%2==0):
    else:               #                                    return "even"
        return "odd"     #                               return "odd"
num=int(input("enter a num: ")) # this will give the same output if will run if condition is true and return even and exit the function 
print(odd_even(num))    # and condition false wiil return odd as output


# another way--> boolean vala
def is_even(no):
    if (no%2==0):
        return True
    return False
print(is_even(9))

#can be written as
def is_even(n): # parameters 
    return num%2==0 # true if condition is true and if false will return false
print(is_even(10)) # argument

# when we call a function the arguments are paased(iske anadr jo h vo argument) aur when we define funtion (it is called parameters)
# functions can be passed without any parameters
def song():
    return "happy birthday"
print(song())