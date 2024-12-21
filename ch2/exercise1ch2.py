# take 3 nos as input and print the average using style formating, all inputs must be taken in single line
num1,num2,num3=input("enter 3 numbers ").split()
avg=(int(num1) +int(num2) +int(num3))/3
print("avg is " + str(avg))

#with style formating
print(f"avg is {(int(num1) +int(num2) +int(num3))/3}")