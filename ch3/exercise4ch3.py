# take a number input form user and print the sum of the digits
num=input("enter a number: ")
total=0
i=0
while(i<len(num)):
    total=total+int(num[i])
    i=i+1
print(total)