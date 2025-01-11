# fabonacci series
def fabonacci_seq(n):
    a=0
    b=1
    if (n==1):
        print(a)
    elif(n==2):
        print(a,b)
    else:
        print(a,b,end=" ")
        for i in range(n-2):
            c=a+b
            a=b
            b=c
            print(b,end=" ")
num=int(input("enter a number: "))
fabonacci_seq(num)

# default parameters
def user_info(first_name,last_name="unkown",age=None): # this are called default parameters it means if no argument is passed 
    print(f"your first name is: {first_name}") # these parametrs will be printd in the output after default parameter you can't define simple parameter
    print(f"your last name is: {last_name}") # ex-> first-name,last_name="unknown",age this will give error as default is passed first
    print(f"your age is: {age}") 
    
user_info("yash","",24) # here for example default afe is given 23 and still here a arg is passed of 24 so 24 will override 23 and give output 24
#here it is 

# def user_info(first_name,last_name,age=23): 
#     print(f"your first name is: {first_name}")
#     print(f"your last name is: {last_name}") 
#     print(f"your age is: {age}") 
    
# user_info("yash","baviskar",24)

#def user_info(first_name,last_name="unknown",age):  ## will give error def parameter is written before hence error generated
#     print(f"your first name is: {first_name}")
#     print(f"your last name is: {last_name}") 
#     print(f"your age is: {age}") 
    
# user_info("yash",24)

# variable scope

# def fun():
#     x=7 #this is called local variable jo sirf uske khudke functions hi access kr skte h normally bhi x ko print nhi krva skte
#     return x
# def fun2():
#     print(x) # this will give error kyuki x fun ka variable h and fun2 cannot access it uska scope usi function(fun) tak h same as c++ 
# fun2()  
# above code will give error x is not defined

x=5 # it is called global variable har koi access kr skta h 
def fun():
    global x # this means if we have to chng value of global x mtlb har jagah x ki value chng hogi 
    x=7 # global x ko hji chng kiya h naya x (local) define nhi kiya h so output will be 7 7
    return x
print(x) # yaha pe 5 hi o/p aayega kyuki function abhi call nhi kiya h to x ki value chng nhi hui h abhi
print(fun()) # o/p 7
print(x) # o/p 7 agr global x nhi likha hota to iska o/p 5 hota