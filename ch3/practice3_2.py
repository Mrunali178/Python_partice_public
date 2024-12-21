# infinite loop can be stopped by ctrl+c 
#in python for True and False we use this--->boolean variables
#for loop --> in python unlike c c++ we use range function
# syntax--> for i in range(starting , ending): 
                #code with indentation

for i in range (1,11) :
   print(f"hello world {i+1}")
 
#example 1
# sum of 1 to 10
# total=0
# for i in range(1,11):
#     total=total+i
# print(total)

# # user input
# n=int(input("enter a num: "))
# total=0
# for i in range(1,n+1):
#     total=total+i
# print(total)

# example 2
#user input no print sum of digits
num=input("enter a num: ")
total=0
for i in range(0,len(num)):
    total=total+int(num[i])
print(total)

# count hoe many times the chrachters of string are repeated
name=input("enter your name: ")

temp=""
for i in range(0,len(name)):
    if name[i] not in temp:
        print(f"{name[i]} : {name.count(name[i])}")
        temp=temp+name[i]

## break and continue keyword
for i in range(1,11):
    if(i==5):
        break #this will break the loop when i will be equal to 5
    print(i)

for j in range(1,11):
    if(j==5):
        continue # this will only skip when j will be equal to 5 and the loop will continue ahead
    print(j)


# for loop using step argument
for k in range(1,11,2): # the last argument is called the step argument it is same as previous kitne steps aage badhna h 
    print(k) # in this it will take gap of two and will print series of odd numbers

# for loop with strings
# name="yash"
# for i in name:
#     print(i)

for i in "yash": # this will print letters one by one
    print(i)

# the sum of digits program can be written as
num=input("enter a number: ")
total=0
for i in num:
    total+=int(i)
print(total)