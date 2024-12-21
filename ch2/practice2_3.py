#methods is used for removing spaces
#lstrip() method removes left side spaces of the string
name="      yash     "
dot="............."
print(name+dot) # printed along with the spaces
print(name.lstrip()+dot) #left space removed 

#rstrip() method removes right side spaces
print(name.rstrip()+dot) #gap between yash and dots removed

#strip() method is ued to remove space from left and right both sides
print(name.strip()+dot)

#but these methods don't remove the spaces between the string i.e ya sh this space between ya and sh is not removed for this we use replace method
name2="Y assh"
print(name2.replace(" ","")+dot) #1st argument consist the element to be replaced and 2nd arg from what to replace here space replaced by no space

#solution to exercise3ch2 problem of space is  
#remove all spaces from sides of name string using strip()method then chng it to lower case
#remove all spaces from sides of ch string using strip()method then chng it to lower case (same as name)
#name.strip().lower()---->chngs to lowercaes and removes spaces
#ch.strip().lower()---->chnges to lower case and remove spaces
#print(name.strip().lower().count(ch.strip().lower()))


# More about replace and find method 
string="she is beautiful and she is good dancer"
print(string.replace("is","was",1)) # it will replace 1st "is" with "was" 1 means only one out of 2 is replaced you can tell how many to replace
print(string.find("is")) # this will give the 1st position of the word is 
#it will print the position which it will get first
print(string.find("is",2)) # this will start finding "is" after 2nd index
#if you don't know what is the index of 1st is so you can do this
is_pos1=string.find("is") #is_pos1----->will give a index
#now we have to search after that index so
is_pos2=string.find("is",is_pos1+1) #+1 isliye lagaya kyuki index k baad se search kregas vo 
print(is_pos2)

# center() method--->?it adds whatever you want at the right and left side of the string
# ex---> want to add 2 start(**) at the starting and the ending of the string ex- **yash**
# so you have to use center(length of the string + how many stars to add,"what to add here it is *") 
#example-- print(name.center(8,"*")) ----> name yash length = 4 stars to add = 4 ehnce 4+4=8

name=input("enter your name: ")
#length=len(name)
print(name.center(len(name)+8,"@"))


#strings are inmutable example:
string="string"
#string[1]="T" this will give error as once strihng is created it can't be chnaged 
#2nd ex:
string.replace("t","T")
print(string) #it will print the original string as replace metho0d don't chng original string it makes new string hence it can print and can be stored in another variable but can't chng the original one
print(string.replace("t","T")) 
#this is called immutable string in python. In ruby language string is mutable


#assignment operator
name="harsh"
name= name+"it" 
print(name)#will give hasrhsit as variable can be chnged anytime in python 
#can also be written as name+="it" means the same as above
age= 18
age*=2 
print(age)