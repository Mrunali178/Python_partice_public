#define function which will take list containing numbers as input and return list containing squares of every element
def square(l):
    numbers=[]
    for i in l:
        numbers.append(i**2)
    return numbers
# num=list(range(1,6))
# print(square(num)) 
# user input
lst=[]
n=int(input("enter no of elemnts in list: "))
for j in range(0,n):
    num=int(input(f"enter element at position {j+1} : "))
    lst.append(num)

print(lst)
print(square(lst))