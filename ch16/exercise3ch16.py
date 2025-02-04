# create any class and create count_instance variable in it. whenever any object is called increase count_instance and return the number of objects created
class Person:
    count_instance=0
    def __init__(self):
        Person.count_instance+=1
        
p1=Person()
p2=Person()
p3=Person()
print(Person.count_instance)  #o/p--> 3
