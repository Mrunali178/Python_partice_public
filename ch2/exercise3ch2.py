# take 2 comma seperated inputs name and a character and 1) print its length and 2) how many times the character given by user repeated (case insensitive count)

name,ch=input("Enter your name and a charater sperated by comma: ").split(",")
print(len(name))
low=name.lower() 
char=ch.lower()
print(low.count(char))

# can be wtitten as
print(name.lower().count(ch.lower()))
#here a problem will arise if after comma space is given then ch is entered so the ch will terat space+ch as whole character and will give 0 as ouput in count as space+ch is no character in the string
# so here's its solution ch2_3
rem=name.strip().lower()
print(len(rem))
print(name.strip().lower().count(ch.strip().lower()))
