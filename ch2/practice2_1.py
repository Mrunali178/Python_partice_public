#string concatenation
first_name="Mrunali"
last_name="Baviskar"
full_name=first_name+last_name # called as string concatenation--> adding 2 strings
#print(full_name)
print(first_name+" " + last_name)#can be also given as this
#print(first_name+3) --> type error as 3 is not a string
# print(print(first_name+"3") --> no error
# print(first_name+str(3)) --> no error str will chng int to string 

print(first_name*3) # (*)star can be used as it doesn't add string it helps to write the same thing multiple(number given) times hence no error
#print((first_name+"\n")*3)


#user_Input
#uses input function this function always take input in the for of the string
#name=input("What is your name ")
#print(name)
#age=input("enter age")
#print("your age is "+age) # --> this line doesnt give error which means age is passed as a string and not integer as above int can not be connected to the string


#int function
num=int(input("enter 1st number")) # as input is always taken in the form of the string we have to conert it in int 
num2=int(input("enter 2nd no")) # else instead of giving sum it eill concatenate
total=num+num2 #if not converted to int it will give output as (ex-23)
print("total is "+ str(total)) #since string cannot be added to int we have to again covert it in the string hence str is used
#type coversion 
#str
#4--->"4"
#int
#"4"--->4
#float
#"4"--->4.0
#int + float = ans in float


#declaration in same line 
name,age="Mrunali",20
print("name is "+ name + " age is "+ str(age))
x=y=z=1
print(x+y+z)


#two or more inputs in single line
name,age= input("enter name and age ").split() # dont press enter give space yash space 20
print(name)
print(age)
name,age= input("enter name and age ").split(",") # dont press enter dont give space too seperated by comma yash comma 20
print(name)
print(age)


# string formatting
name="Mrunali"
age=20
print("hello "+name + " your age is "+ str(age)) #ugly syntax to make it easy we use string formating
#this below is string formating  and here there is no need of worrying for type conversion
print("hello {} your age is {}".format(name,age)) #used in python 3
print(f"hello {name} your age is {age}") # used in python 3.6 f is mandatory else output will be different 
 

#string indexing
lan="python"
print(lan[2]) # prints 3rd letter of the string  
print(lan[-1]) # prints the last letter helpful when you don't know the length and still want to print last letter


#string slicing or selecting sub sequences
# syntax --> print(variable_name[start argument : stop argument + 1]) as it will print stop argument-1 
print(lan[3:6])
print(lan[-3:6]) #from last 3rd to the 6th index of the string
print(lan[:]) # whole string will be printed
print(lan[2:]) # starting from index 2 to end
print(lan[:3]) # from beigining to tha stop index
print("PYTHON" [2:5]) # this way can also be written output will be THO
#print(lan[3:3]) #nothing will be printed


#step argument
# syntax --> print(variable_name[start argument : stop argument + 1 : step argument])step argument means gap kitni leni h, 2 mtln 2 letter chod k print krega
print("PYTHON" [2:6:3]) # basically it is kitne kadam aage badhega "harshit" h then r then step
print("PYTHON" [::2])
print("PYTHON" [5::-1]) #print in reverse from the starting index to end -1 represents backward 
print("yash"[-1::-1]) # will print reverse string
#can also be written as 
print("yash"[::-1]) # automatically it will print reverse string 