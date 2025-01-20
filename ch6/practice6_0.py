# tuples
example=('abc',1,'xyz',2.0)
print(example)  #('abc', 1, 'xyz', 2.0)
# tuples are immutable hence no append,insert,pop,remove method can be used
# count,index,len function and slicing can be done
days=('monday',"tues","wed") # mostly used for the data that is fixed such as days
print(days[:1]) # this is allowed print 1 item of the list
#days[1]='wed' #not allowed we vcann't chng in the tuple ->error->'tuple' object does not support item assignment


#looping in tuples
# for and while loop same as string and list
#tuple with one element
nums=(1) # it will not be a tuple as for the type to be the tuple there must be a comma at end let's see
print(type(nums)) # this will give int or whatever type of data is given
num=(1,)  # since atlast we putted comma it will be treated as tuple
print(type(num)) #type tuple
word=('word') #type string
words=('word',) #type tuple

#tuple without paranthesis
guitars='yamaha' , 'baton rouge' , 'taylor'
print(type(guitars)) # if you directly write strings without brackets it will consider it as tuple


#tuple unpacking
guitar1, guitar2, guitar3=(guitars) # this will automatically store the guitars element one by one in each variable 1,2,3
print(guitar1) #yamaha
#guitar1, guitar2=(guitars) # if we will give it less variables tahn than the tuple has it will give 
#error->too many values to unpack (expected 2)

# list inside tuples
fav=("south",['north','landscape'])
fav[1].pop() #this will work as at 1st position of tuple we have list and list is mutable hence it will pop and can append too
fav[1].append("u r sweet") #o/p ('south', ['north', 'u r sweet'])
#fav.append("we") #error--> 'tuple' object has no attribute 'append'
print(fav)

# mthods in tuple min,max,sum
mixed=(1,2,3,4.0)
print(min(mixed)) #o/p -1
print(max(mixed)) #o/p-4.0
print(sum(mixed)) #o/p-10.0 sum of all numbers in tuple

# function returning two values 
def func(int1,int2):
    add=int1+int2
    mul=int1*int2
    return add,mul # whwnever you return two values eksath then it will be in forn of tuple
print(func(2,3)) #o/p--> (5, 6) tuple form
# so if u want to get different value and not in form of tuple so store it in variable
add1,mul1=func(2,3) # add will store 1st returned value i.e sum and mul 2nd i.e is product
print(add1) #o/p-->5
print(mul1) #o/p-->6


#range same as list
num=tuple(range(0,11))
print(num) #o/p-> (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
num=list((1,2,3,4))
print(num) #o/p-> [1, 2, 3, 4] tuple to list


#in str o/p will be same as i/p mtlb
nums=str((1,2,3,4)) #tuple to str
print(nums) #o/p-> (1, 2, 3, 4)

list_ele=str([1,2,3,4,5])
print(list_ele) #o/p--> [1, 2, 3, 4, 5]
# same o/p aara h jesa input diya h but vo str me convert ho raha h vo aesa h str("[1,2,3,4]")