# **Kwargs ---> takes any of arguments in form of dictionary
def func(**kwargs):
    print(kwargs)    #o/p--> {'first_name': 'Mrunali', 'last_name': 'Baviskar'}
    print(type(kwargs)) #o/p--> <class 'dict'>
func(first_name="Mrunali",last_name="Baviskar")  


def funct(name,**kwargs): #if here any extra parameter is passed it is neccessary to give value of that parameter in argument
    for k,v in kwargs.items():
        print(f"{k}:{v}")
funct("mohit",first_name="Mrunali",last_name="Baviskar")#o/p---> first_name:Mrunali
                                                        #last_name:Baviskar

# **kwargs as an argument unpacks dict
def fun(**kwargs):
    for i,j in kwargs.items():
        print(f"{i}:{j}")
d={"first_name":"harshit","age":24}
# fun(d) #will give error TypeError: fun() takes 0 positional arguments but 1 was given
fun(**d) #o/p--> first_name:harshit
        # age:24
# in case if you want to use all the parameters in a function they must be in a sequence PADK
# parameter *args default **kwargs
def sequence(name,*args,last_name="unknown",**kwargs):
    print(name)         #o/p---> mohit
    print(args)         #o/p---> (1, 2, 3)
    print(last_name)    #o/p---> unknown
    print(kwargs)       #o/p---> {'a': 1, 'b': 2}
sequence("mohit",1,2,3,a=1,b=2)

# def sequence(*args,name,last_name="unknown",**kwargs): #changing the sequence will give the error TypeError: sequence() missing 1 required keyword-only argument: 'name'
#     print(name)         #o/p---> mohit
#     print(args)         #o/p---> (1, 2, 3)
#     print(last_name)    #o/p---> unknown
#     print(kwargs)       #o/p---> {'a': 1, 'b': 2}
# sequence("mohit",a=1,b=2)