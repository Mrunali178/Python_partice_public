# lambda practice questions
#normal
def iseven(a):
    return a%2==0

# in lambda
is_even=lambda a:a%2==0
print(is_even(4))   #o/p--> True

# normal
def last_char(s):
    return s[-1]
print(last_char("mrunali")) #o/p---> i

# in lambda
last_char1=lambda s : s[-1]  
print(last_char1("yash"))   #o/p---> h

# lambda with if else
#normal
def length(s):
    if len(s)>5:
        return True
    else:
        return False
length("avhgshgx")  #o/p---> True

# using lambda
length1=lambda s : True if len(s)>4 else False
print(length("abcd"))   #o/p---> False