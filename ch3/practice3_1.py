# here in python instead of els if we use--> elif
##elif
age=int(input("enter age : "))
if (age>=21):
    print("you are adult")
elif(18<=age<21):  ##instead of else if here elif is used
    print("you are tennager")
else:
    print("you are a kid")

## in keyword ---> it checks wheather a particular character is present in the string or not,can be used in loops dsa etc
name="Yash"
if('a' in name):  # chechs wheater a is present in name or not 
    print("present")
else:
    print("not present")

# or can be written as (directly string name can be given instyead of var name)
if("m" in "mrunali"):
    print("yes")
else:
    print("no")

# check empty or not
name="abc"
if (name):  #this means it checks the var name and if its empty it will go to else block, if executes if the condition is true
    print("string is not empty")
else:
    print("string is empty")

# example\
name2=input("enter your name: ")
if(name2):
    print(f"your name is {name2}")
else:
    print("you didn't type anything")

# while loop (same as c c++)
i=1 #variable initialization
while(i<=10): #condition
    print("hello world " + str(i)) # will be printed 10 times
    i=i+1 # increament

# sum of nos 1 to 10 using while loop\
total=0
i=1
while(i<=10):
    total+=i
    i+=1 # in python we cann't use ++ we have to use +=1
print(total)