# custom exceptions---> creating our own exception
def NameTooshortError(ValueError):  #for creating our own exception we need to inherit any of the in built exception so that our code works properly
    pass
def validate(name):
    if len(name)<8:
        raise NameTooshortError("please enter name above than 8 letters")
username=input("enter name: ")
validate(username)
print(f"hello {username}")