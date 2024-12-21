#string methods
#1. len() function--> it used to find the length of the string
print(len("Mrunali"))
# or can be stored in variable ans it counts spaces in between as well
name="MrUnaLi bavIskAr"
length=len(name)
print(length)

#2. lower() method --> it will print all the letters in lowercase
print(name.lower())

#3.upper() method--> it will chng all the letters to upper case
print(name.upper())

#4.tile() method
print(name.title())

#5. count() method--> returns the count of the letter tells how many times repeated
print(name.count("a")) # it is case sensetive counts only small a

## NOTE --> methods are used by putting dots and fuctions are used directly without dots