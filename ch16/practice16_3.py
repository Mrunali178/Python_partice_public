# class methods --> can be accessed using decorator-->@classmethod
class Person:
    count_insatnce_var=0  #class variable or attribute
    def __init__(self,first_name,last_name,age):
        Person.count_insatnce_var+=1
        self.first_name=first_name
        self.last_name=last_name
        self.age=age

    @classmethod
    def count_instance(cls):  ##this is class method
        return f"you have created {cls.count_insatnce_var} instances of {cls.__name__} class"

    def fullname(self):
        return f"{self.first_name} {self.last_name}"
    def is_above_18(self):
        return self.age>18

p1=Person("harsh",'sharma',24)
p2=Person("mru",'abc',19)
print(Person.count_instance())
print(p2.count_instance())  # can also be acessed using object name but it is not correct format so classname.methodname()


#class as constructor
# if suppose in above code instead of p1=Person("harsh",'sharma',24) i have to pass it as complete string p1=Person("harsh,sharma,24") so i will have to create my own constructor using @classmethod


class Person:
    count_insatnce_var=0  #class variable or attribute
    def __init__(self,first_name,last_name,age):
        Person.count_insatnce_var+=1
        self.first_name=first_name
        self.last_name=last_name
        self.age=age

    @classmethod
    def from_string(cls,strs):
        first,last,age=strs.split(",")
        return cls(first,last,age)
    @classmethod
    def count_instance(cls):  ##this is class method
        print("this is class constructor")
        return f"you have created {cls.count_insatnce_var} instances of {cls.__name__} class"

    def fullname(self):
        return f"{self.first_name} {self.last_name}"
    def is_above_18(self):
        return self.age>18

# p1=Person("harsh,sharma,24")  #o/p this will give error Person.__init__() missing 2 required positional arguments: 'last_name' and 'age' as this is calling normal init method
p1=Person.from_string("harsh,sharma,24")  #this will work properly

print(p1.fullname()) #and all the other methods can be accessed using this

#static method
# Does not take self (instance reference).
# Does not take cls (class reference).
# Acts like a regular function inside a class.
# Is related to the class logically, but does not modify class or instance attributes.
#it is accessed using @staticmethod decorator


class Person:
    count_insatnce_var=0  #class variable or attribute
    def __init__(self,first_name,last_name,age):
        Person.count_insatnce_var+=1
        self.first_name=first_name
        self.last_name=last_name
        self.age=age
    
    #class method
    @classmethod
    def from_string(cls,strs):
        first,last,age=strs.split(",")
        return cls(first,last,age)
    @classmethod
    def count_instance(cls):  ##this is class method
        print("this is class constructor")
        return f"you have created {cls.count_insatnce_var} instances of {cls.__name__} class"
    
    # static method
    @staticmethod
    def hello():  #this is static method just as normal function without parameters like self or cls
        print("Hello user from static method")

    #instance method
    def fullname(self):
        return f"{self.first_name} {self.last_name}"
    def is_above_18(self):
        return self.age>18

# p1=Person("harsh,sharma,24")  #o/p this will give error Person.__init__() missing 2 required positional arguments: 'last_name' and 'age' as this is calling normal init method
p1=Person.from_string("harsh,sharma,24")  #this will work properly
Person.hello()  #o/p--> Hello user from static method 

#encapusaltion--> data and methods stored at one place i.e data is encapsulated
#abstarction --> hiding dteails and only showing neccessary one ex sort() we don't know what is written in sort method or which type os sorting algo is used (python uses tim sort in sort method)

#naming convention
#_name--> specifies user to treat that variable as private i.e to not chng it
#in python there is no access specifiers such as private protected or public all functions and variables are public in python
# so to tell users that it is private and don't chng it we use _name (but its only convention it doesn't mean that we made it private we can chng it but we should not)
class Laptop:
    percent=10
    def __init__(self,brand,model,price): #(dunder or magic method)
        self.brand=brand
        self.__model=model
        self._price=price  #(this should be treated as private but we can chng it as its just convention its still public)
        self.laptop_name=brand+ " "+model

    def apply_discount(self):
        
        discount=(self.price*self.percent)/100
        return f"after discount of {self.percent}% the price of {self.laptop_name} is {self.price-discount}"

l1=Laptop("asus","vivobook",30000)
l2=Laptop("Lenovo","ideapad",55000)
# we can still chng it _price:
l2._price=40000
print(l2._price)  #o/p--> 40000


#__name__ these are called dunder or magic methods ex- __init__ , __dict__

#__name (mainly used with inheritance) its not convention is means the avr is only accessed in that class and python chnges its varname as _classname__varname so that it cant be accessed outside
# print(l1.__model) #o/p--> AttributeError: 'Laptop' object has no attribute '__model' ....but we have this variable or attribute so whats is its name?
print(l1.__dict__)  #o/p--> {'brand': 'asus', '_Laptop__model': 'vivobook', '_price': 30000, 'laptop_name': 'asus vivobook'} see model name is chnged to laptop model
print(l1._Laptop__model)  #o/p--> vivobook  ## this is called name mangling

#property(getter in other programming languages such as c++ or java) and setter method

class Laptop:
    percent=10
    def __init__(self,brand,model,price): #(dunder or magic method)
        self.brand=brand
        self.__model=model
        self._price=price  #(this should be treated as private but we can chng it as its just convention its still public)
        self.laptop_name=f"{brand} {model} price is {self._price}"

    def apply_discount(self):
        
        discount=(self.price*self.percent)/100
        return f"after discount of {self.percent}% the price of {self.laptop_name} is {self.price-discount}"

l1=Laptop("asus","vivobook",-30000)
l2=Laptop("Lenovo","ideapad",55000)
l2._price=-40000
print(l1.__dict__) # o/p--> 'brand': 'asus', '_Laptop__model': 'vivobook', '_price': -30000, 'laptop_name': 'asus vivobook price is -30000'} 
print(l2.__dict__)  #o/p--> {'brand': 'Lenovo', '_Laptop__model': 'ideapad', '_price': -40000, 'laptop_name': 'Lenovo ideapad price is 55000'}
print(l2.laptop_name)  #o/p--> Lenovo ideapad price is 55000 
# there is problem i.e price can't be negative and also in laptop_name the price even after changing it is not chnegd here so for solution we can create laptop_name function rather than var
# and use if else so that in arguments no one can pass -ve value

class Laptop:
    percent=10
    def __init__(self,brand,model,price): #(dunder or magic method)
        self.brand=brand
        self.model=model
        #self.price=max(price,0)    instead of if else we can also write this
        if price>0:
            self._price=price  
        else:
            self.price=0
    
    def laptop_name(self):
        return f"{self.brand} {self.model} price is {self._price}"

    def apply_discount(self):
        
        discount=(self.price*self.percent)/100
        return f"after discount of {self.percent}% the price of {self.laptop_name} is {self.price-discount}"

l1=Laptop("asus","vivobook",-30000)
l2=Laptop("Lenovo","ideapad",55000)
# we can still chng it _price:
l2._price=-40000  #but this vali value still not chng so we have use setter method
print(l1.__dict__) # o/p--> 'brand': 'asus', '_Laptop__model': 'vivobook', '_price': 0} 
print(l2.__dict__)  #o/p--> {'brand': 'Lenovo', '_Laptop__model': 'ideapad', '_price': -40000}
print(l2.laptop_name())  #o/p--> Lenovo ideapad price is -40000 now this problem got solved but we have to call function intead using it as attribute


#solution
class Laptop:
    percent=10
    def __init__(self,brand,model,price): #(dunder or magic method)
        self.brand=brand
        self.model=model
        self._price=max(price,0)    #instead of if else we can also write this
        # if price>0:
        #     self._price=price  
        # else:
        #     self.price=0
    @property  #by using this we can use laptop_name as attribute instead of method
    def laptop_name(self):
        return f"{self.brand} {self.model} price is {self._price}"

    @property
    def price(self):
        return self._price
    #it is neccessary to stter just next by property else it will give error
    @price.setter
    def price(self,new_price):
        self._price=max(new_price,0)


    def apply_discount(self):
        
        discount=(self.price*self.percent)/100
        return f"after discount of {self.percent}% the price of {self.laptop_name} is {self.price-discount}"

l1=Laptop("asus","vivobook",-30000)
l2=Laptop("Lenovo","ideapad",55000)

l2.price=-40000  #now this value is also chnged to 0 if negative (here don't directly chng _price write price)
print(l1.price) # o/p--> 0 
print(l2.price)  #o/p--> 0
print(l2.laptop_name)  #o/p--> Lenovo ideapad price is 0 now we can this as attribute instead of method