#define laptop class(last exercise) create a instance method apply_discount which will take a parameter i.e a number and that discount you have to apply to the price
class Laptop:
    def __init__(self,brand,model,price):
        self.brand=brand
        self.model=model
        self.price=price
        #we can create more instance variables and can combine attributes for that mtln 3 attribute h to its not neccessary to have 3 instance vars
        self.laptop_name=brand+ " "+model

    def apply_discount(self,percent):
        self.percent=percent
        discount=(self.price*percent)/100
        return f"after discount of {percent}% the price of {self.laptop_name} is {self.price-discount}"
   
l1=input("enter laptop brand: ")
l2=input('enter laptop model: ')
l3=int(input('enter price: '))
n=int(input('discount for this is: '))
l=Laptop(l1,l2,l3)
# l1=Laptop("asus","vivobook",30000)
# l2=Laptop("Lenovo","ideapad",55000)
print(l.apply_discount(n))   #o/p--> after discount of 10% the price of Lenovo ideapad is 49500.0