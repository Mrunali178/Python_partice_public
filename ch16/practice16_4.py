# inheritance --> when child class inherits the property of base class
class Phone:
    def __init__(self,brand,model,price):
        self.brand=brand
        self.model=model
        self.price=price
        
    def fullname(self):
        return f"{self.brand} {self.model} and {self.price}"

    def apply_discount(self,percent):
        self.percent=percent
        discount=(self.price*percent)/100
        return f"after discount of {percent}% the price of {self.laptop_name} is {self.price-discount}"

class SmartPhone(Phone):  #child class (parent class)
    def __init__(self,brand,model,price,ram):
    #two ways to take its attirbutes and methods
        # Phone.__init__(self,brand,model,price) #uncommon way
        super().__init__(brand,model,price)  #will work same and common way
        self.ram=ram
p1=Phone("Redmi","Note10",20000)
s1=SmartPhone("oneplus",'5',10000,'5GB')
print(p1.fullname())  #o/p--> Redmi Note10 and 20000
print(s1.fullname())  #o/p--> oneplus 5 and 10000 

#Hierarchical Inheritance
class Phone:
    def __init__(self,brand,model,price):
        self.brand=brand
        self.model=model
        self.price=price
        
    def fullname(self):
        return f"{self.brand} {self.model} and {self.price}"

    def apply_discount(self,percent):
        self.percent=percent
        discount=(self.price*percent)/100
        return f"after discount of {percent}% the price of {self.laptop_name} is {self.price-discount}"

class SmartPhone(Phone):  #child class (parent class)
    def __init__(self,brand,model,price,ram):
    #two ways to take its attirbutes and methods
        # Phone.__init__(self,brand,model,price) #uncommon way
        super().__init__(brand,model,price)  #will work same and common way
        self.ram=ram

class SmartPhone2(Phone):  #child class (parent class)
    def __init__(self,brand,model,price,ram,camera):
    #two ways to take its attirbutes and methods
        # Phone.__init__(self,brand,model,price) #uncommon way
        super().__init__(brand,model,price)  #will work same and common way
        self.ram=ram
        self.camera=camera
p1=Phone("Redmi","Note10",20000)
s1=SmartPhone("oneplus",'5',10000,'5GB')
s2=SmartPhone2("oneplus",'5',10000,'5GB',"8mp")
print(p1.fullname())  #o/p--> Redmi Note10 and 20000
print(s2.fullname())  #o/p--> oneplus 5 and 10000 


#multilevel inheritance
class Phone: #(base class)
    def __init__(self,brand,model,price):
        self.brand=brand
        self.model=model
        self.price=price
        
    def fullname(self):
        return f"{self.brand} {self.model} and {self.price}"

    def apply_discount(self,percent):
        self.percent=percent
        discount=(self.price*percent)/100
        return f"after discount of {percent}% the price is {self.price-discount}"

class SmartPhone2(Phone):  #child class (parent class)
    def __init__(self,brand,model,price,ram,camera):
    #two ways to take its attirbutes and methods
        # Phone.__init__(self,brand,model,price) #uncommon way
        super().__init__(brand,model,price)  #will work same and common way
        self.ram=ram
        self.camera=camera

#this is called method overriding(same name function two different classes)
    def fullname(self):
        return f"{self.brand} {self.model} and {self.price} along with ram {self.ram}"

#multilevel inheritance
class Flagship(SmartPhone2):
    def __init__(self,brand,model,price,ram,camera,front_camera):
        super().__init__(brand,model,price,ram,camera)
        self.front_camera=front_camera

p1=Phone("Redmi","Note10",20000)
s2=SmartPhone2("oneplus",'5',10000,'5GB',"8mp")
s3=Flagship("oneplus",'5',10000,'5GB',"8MP","5MP")
print(p1.fullname())  #o/p--> Redmi Note10 and 20000
print(s2.fullname())  #o/p--> oneplus 5 and 10000 along with ram 5GB (the smartphone fullname method is called as first it got that method in that clas)
print(s3.fullname())  #o/p--> oneplus 5 and 10000 along with ram 5GB (this is also printing of smartphone same reason agr flagship class me daal denge full name function to vo print krega)

#isinstance() method used to check wether the object is of that class or not

print(isinstance(s2,SmartPhone2))   #True
print(isinstance(s3,SmartPhone2))   #True
print(isinstance(s2,Phone))   #True (this is bcoz smartphone inherited phone class, phone is parent hence child bject is parent's objets but parent's object is not chils object)
print(isinstance(s2,Flagship))   #False (flagship chils of smartphone)

#isubclass() tells wether it is subclass of the given class or not
print(issubclass(SmartPhone2,Phone)) #True
print(issubclass(SmartPhone2,Flagship))  #False
print(issubclass(Flagship,Phone)) #True


##method resolution order---> it is for every class ,we can use help(classname) function --> this is the order in which python search the function and code and then execute it

# help(Phone)  #o/p--> class Phone(builtins.object)
                    #  |  Phone(brand, model, price)
                    #  |
                    #  |  #multilevel inheritance
                    #  |
                    #  |  Methods defined here:
                    #  |
                    #  |  __init__(self, brand, model, price)
                    #  |      Initialize self.  See help(type(self)) for accurate signature.
                    #  |
                    #  |  apply_discount(self, percent)
                    #  |
                    #  |  fullname(self)
                    #  order in which it gets executed
# help(Flagship)   #o/p:-
# Method resolution order:
#  |      Flagship
#  |      SmartPhone2 (here only got full name method so will execute this vala method)
#  |      Phone
#  |      builtins.object

