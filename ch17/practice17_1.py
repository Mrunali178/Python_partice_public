# custom exceptions---> creating our own exception
def NameTooshortError(ValueError):  #for creating our own exception we need to inherit any of the in built exception so that our code works properly
    pass
def validate(name):
    if len(name)<8:
        raise NameTooshortError("please enter name above than 8 letters")
username=input("enter name: ")
validate(username)
print(f"hello {username}")

# debugging in python
#import pdb module for debugging in python
#module- Python uses various classes and functions written by developers
# Debugging is the process of finding and fixing errors (bugs) in your code. Let’s break it down step by step, like explaining to a beginner.

# 🔹 Types of Bugs in Python
# Syntax Errors → Code is written incorrectly (e.g., missing colons : or parentheses ()).
# Runtime Errors → Code runs but crashes due to issues like division by zero or accessing an undefined variable.
# Logical Errors → Code runs fine but gives wrong results due to incorrect logic.
import pdb
pdb.set_trace() #set trace executes code line by line by showing arrow
name=input("enter name: ")
age=input("enter age: ")
age2=int(age)+2
print(f"{name}, age = {age2} after 2 years")