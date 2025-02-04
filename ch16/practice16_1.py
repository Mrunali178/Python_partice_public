#instance methods--> methods are the functions defined in class
class Person:
    def __init__(self,first_name,last_name,age):
        self.first_name=first_name
        self.last_name=last_name
        self.age=age
    def fullname(self):
        return f"{self.first_name} {self.last_name}"
    def is_above_18(self):
        return self.age>18

p1=Person("harshit",'sharma',24)
print(p1.fullname()) #this we use but the inner working is shown below
#inner working of this fullname method

print(Person.fullname(p1)) #class--> method--> parameter self means object itself is argument ## o/p---> harshit sharma

print(p1.is_above_18())  #o/p--> True


#same in list 
l=[1,2,3]
# example let's say pop which is without parameter and append with parameter working
print(list.pop(l))
list.append(l,4)
print(l)

#this is the inner working but actully we use as
l.append(5)
print(l)
l.pop()
print(l)