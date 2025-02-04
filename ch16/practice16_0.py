#oop --> used for real world programming based on class object and method 
#whenwever we create class we define a init method i.e. constructor and whenever we call object init method is called first
class Person:
    def __init__(self,first_name,last_name,age):
        #instance variables
        print("first init method is called..")
        self.first_name=first_name
        self.last_name=last_name
        self.age_num=age  #var name i.e lhs we can give any thing like here i gave age_num only keep in mind while printing
p1=Person("mru","abc",20)
p2=Person("yash","abcs",24)
print(p1.first_name)
print(p2.last_name)
print(p2.age_num)
#o/p--> first init method is called..
        # first init method is called..
        # mru
        # abcs
        # 24