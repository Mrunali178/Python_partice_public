# define a function which takes three numbers as a input and return greater of 2 numbers
# def greater(a,b,c):
#     if(a==b==c):
#         return "equal"
#     elif(c<a>b):
#         return a
#     elif(a<c>b):
#         return c
#     else:
#         return b
    
num1,num2,num3=input("enter 3 number with space: ").split()
num1=int(num1)
num2=int(num2)
num3=int(num3)
#print(f"{greater(num1,num2,num3)} is greater")

# this program can be written as function in function
def greater(a,b):
    if(a>b):
        return a
    else: 
        return b

def greatest(a,b,c):
    bigger=greater(a,b)
    #return greatest(greater(a,b),c) 
    return greater(bigger,c)  # this can be written as return greatest(greater(a,b),c) it will give same output
print(greatest(num1,num2,num3)) 