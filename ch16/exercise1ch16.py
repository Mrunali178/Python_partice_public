#create a laptop class with attributes like brand model price and create two instances for that class
class Laptop:
    def __init__(self,brand,model,price):
        self.brand=brand
        self.model=model
        self.price=price
        #we can create more instance variables and can combine attributes for that mtln 3 attribute h to its not neccessary to have 3 instance vars
        self.laptop_name=brand+ " "+model
l1=Laptop("Asus","vivobook","30000")
l2=Laptop("Lenovo","ideapad","55000")
print(l2.brand)  #o/p--> Lenovo
print(l2.price)         # 55000
print(l1.price)         # 30000
print(l2.laptop_name)   # Lenovo ideapad