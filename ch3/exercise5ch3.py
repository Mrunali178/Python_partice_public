# take name input from user and print the count of each character that how many times repeated
name=input("enter your name: ")
temp=""
i=0
while(i<len(name)):
    if(name[i] not in temp):
        temp+=name[i]
        print(f"{name[i]}: {name.count(name[i])}")
    i+=1
   