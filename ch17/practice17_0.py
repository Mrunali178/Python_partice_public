# errors and raise errors
class Animal:
    def __init__(self,name):
        self.name=name
    def sound(self): #in java such type of methods are called as abstract method in python there is no abstract method
        raise NotImplementedError ("please define sound method in subclass")

class Dog(Animal):
    def __init__(self,name,breed):
        super().__init__(name)
        self.breed=breed
    
    def sound(self):
        return "bahw bahw"

class Cat(Animal):
    def __init__(self,name,breed):
        super().__init__(name)
        self.breed=breed

doggy=Dog("chiku","pug")
print(doggy.sound())  #o/p--> bahw bahw

# catty=Cat("chiku","kitty")
# print(catty.sound())   #o/p--> raise NotImplementedError ("please define sound method in subclass")
                            # NotImplementedError: please define sound method in subclass  (this is because we didn't defined sound method in Cat class)

#example2
class Mobile:
    def __init__(self,name):
        self.name=name
class MobileStore:
    def __init__(self):
        self.mobiles=[]
    def addmobile(self,new_mobile):
        if isinstance(new_mobile,Mobile):
            self.mobiles.append(new_mobile)
        else:
            raise TypeError("new mobile should be object of mobile class")
oneplus=Mobile('oneplus6')
samsung="samsung galaxy s8"
mobostore=MobileStore()
# print(mobostore.mobiles)  #o/p-->[]
# mobostore.addmobile(samsung)  #o/p--> ['samsung galaxy s8'] (without error we can append any string as well)
#after raise error o/p will be  -- TypeError: new mobile should be object of mobile class
# print(mobostore.mobiles)
mobostore.addmobile(oneplus)
mobo_phones=mobostore.mobiles
print(mobo_phones[0].name)  #o/p--> oneplus6

#try except --> exception handling (erros that come at run time are known as exceptions and handling them using try and except is exception handling)
while True:
    try:
        age=int(input("enter age: "))
        break
    except ValueError:
        print("invalid input...please input in integer")
    except:
        print("unexpected input")
if age>18:
    print("you can play this game")
else:
    print("you can't play this game")

#in try we only write the part of code where the error can occur
#else finally with try except
try:
    age=int(input("enter age: "))
except ValueError:
    print("invalid input...please input in integer")
except:
    print("unexpected input")
else: #(instead of using while and break if we use else it directly executes the code if there is no error)
    if age>18:
        print("you can play this game")
    else:
        print("you can't play this game")
finally:
    print("this is finally always executes...")

#The finally block always executes, whether an exception occurs or not.
# It's commonly used for resource cleanup (like closing files, releasing memory, or network connections).