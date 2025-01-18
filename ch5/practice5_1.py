# in keyword in list
# it is used to search wehther the element is present in the list or not example:
fruits=['apple','grapes','mango','chiku']
if ('chiku' in fruits):
    print("chiku is present")
else:
    print("not present")

# some more methods
# count method same as string vali count batayega ki kitne times vo elements list me h
fruits=["apple","kiwi","apple","mango","grapes"]
print(fruits.count("apple"))  # o/p--> 2

#sort method--> sorts the original list 
fruits.sort() # will sort according to letter a-z
print(fruits) # o/p--> ['apple', 'apple', 'grapes', 'kiwi', 'mango']

# if numbers then will sort in ascending order
numbers=[3,1,7,5]
numbers.sort()
print(numbers) #o/p--> [1, 3, 5, 7]

# sorted function
fruits=["apple","kiwi","apple","mango","grapes"]
print(sorted(fruits)) # this will only print the sorted list but not make chnges in original one ['apple', 'apple', 'grapes', 'kiwi', 'mango']
print(fruits) # o/p--> ['apple', 'kiwi', 'apple', 'mango', 'grapes'] this is original list no chng

#clear method --> will make our list, empty sare elements remove kr dega
fruits.clear()
print(fruits) #o/p--> []

# copy method--> will copy the list to a new list
num=numbers.copy()
print(num) # o/p--> [1, 3, 5, 7] ye o/p isliye aaya kyuki apnne list sort kri h (at line 20) aur update hoke list ye ho gyi

## list comparision
# == checks the values of the list if same then return true else false
# is checks whether the list is stored at same memory or not
fruits1=['apple','grapes']
fruits2=['mango','kiwi','banana','chiku']
fruits3=['apple','grapes']
print(fruits1==fruits2) # false kyuki elements are different
print(fruits1==fruits3) # true kyuki elements are same
print(fruits1 is fruits3) # false because these are 2 different objects so stored at different memory location

# join and split method 
# split--> it converts string to the list syntax--> var_name='string '.split('kaha se todna h') baaki same as string vala 
user_info='yash 24'.split() # default is space
print(user_info) # o/p--> ['yash', '24']

# join --> converts list to string but all the elements of list must be in string format
# syntax--> print('jisse bhi add krna h example ,'.join(var_name))
user_info=["yash","24"]
print(','.join(user_info)) # o/p--> yash,24

# list vs array
# list me different data types store kr skte but not in array, python me bhi array moduke hota h but vo imp[ort krna pdta h one of its module is numpy
# list vs string 
# string immutable --> cannot be changed once cretaed but 
# lists--> muttable original list me chngs ho skte h with use of some methods ex- pop() original list me se remove krta h

#loops in list
# for loop
name=['word1','word2','word3','word4']
for i in name:
    print(i) # o/p --> word1
                       # word2
                       # word3
                       # word4
 

# while loop
i=0 # intialize
while i< len(name): # condition
    print(name[i]) # print position element o/p will be same as above
    i+=1 # increament

# list in list
matrix= [[1,2,3],[4,5,6],[7,8,9]]  # 1 list k andar 3 list
#if we print directly as matrix[0] 1st list [1,2,3] will be printed
print(matrix[1]) 
# now for printing whole list we have to use loops but if we use single loop it will get printed as same as above
for i in matrix:
    print(i) # o/p-->
             #[1, 2, 3]
             # [4, 5, 6]
             # [7, 8, 9]
# so to print normal series we have to use 2 loops
for sublist in matrix:
    for j in sublist:
        print(j) 
        #o/p-->
        # 1
        # 2
        # 3
        # 4
        # 5
        # 6
        # 7
        # 8
        # 9

# this type of list(list inside list) is called 2d list (matrix)
# to access element of matrix we write 
print(matrix[1][1]) #o/p -> 5 1st index ka 1st index vala element[1][1]


# type function --> this tells the data type of the data
s="string"
print(type(s)) #o/p--> <class 'str'>
print(type(matrix)) # o/p--> <class 'list'>

# more about list
# generate list with range function 
num=list(range(1,11))  # 1s arg starting index 2nd arg end +1 
print(num) #o/p--> [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# some more about pop()
# it returns the pooped value so that if we want back w can take it
popped_item=num.pop()
print(num) # o/p--> [1, 2, 3, 4, 5, 6, 7, 8, 9] print after popping value 
print(popped_item) # o/p-->10 return value that is pooped

#index method--> tells position of the element
print(num.index(4)) #o/p --> 3 ,means 4 3rd index pe h list me same as string vala
# print(num.index(1,3)) # ye 1 ko 3rd index k baad se search krega
# print(num.index(1,3,6)) # last vala h stop kaha pe krna h
# 1st arg what to search ,2nd from where to start, 3rd where to stop

#pass list6 to function
def negative_list(l):
    negative=[]
    for i in l:
        negative.append(-i)
    return negative
print(negative_list(numbers)) #o/p--> [-1, -3, -5, -7]