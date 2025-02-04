# class variables
class Circle:
    pi=3.14
    def __init__(self,radius):
        self.radius=radius
    def circumference(self):
        return 2*Circle.pi*self.radius
c=Circle(3)
print(c.circumference())

#if we would have created pi as instance variable we have to again and again give the value of pi which time as well as memory comsuming hence we created class variable 
#which will be applied to every object and if we modify it, it will be modified for every instance example here
Circle.pi=22/7
c1=Circle(5)
print(c.circumference())
print(c1.circumference())


#suppose only for asus laptop I want to give 50% discount but other all 10% so if we create class variable it will be applied to all hence we use instance var for that particular product here's example:

class Laptop:
    percent=10
    def __init__(self,brand,model,price):
        self.brand=brand
        self.model=model
        self.price=price
        #we can create more instance variables and can combine attributes for that mtln 3 attribute h to its not neccessary to have 3 instance vars
        self.laptop_name=brand+ " "+model

    def apply_discount(self):
        
        discount=(self.price*self.percent)/100
        #if you want to chng value of class var at a particular instance just use self.varname
        return f"after discount of {self.percent}% the price of {self.laptop_name} is {self.price-discount}"

l1=Laptop("asus","vivobook",30000)
l2=Laptop("Lenovo","ideapad",55000)
l1.percent=50
print(l1.__dict__)  #o/p--> {'brand': 'asus', 'model': 'vivobook', 'price': 30000, 'laptop_name': 'asus vivobook', 'percent': 50}
print(l1.apply_discount())  #o/p--> after discount of 50% the price of asus vivobook is 15000.0
print(l2.__dict__)   #o/p--> {'brand': 'Lenovo', 'model': 'ideapad', 'price': 55000, 'laptop_name': 'Lenovo ideapad'}
print(l2.apply_discount())   #o/p--> after discount of 10% the price of Lenovo ideapad is 49500.0