# list
# data structure that can store anything in such as int float string 
# ordered collection of items
numbers=[1,2,3,4]
print(numbers) #   o/p--> [1, 2, 3, 4]
print(numbers[1]) #   o/p--> 2

words=["word1","word2",'word3']
print(words) #   o/p--> ['word1', 'word2', 'word3']
print(words[:2])  #   o/p-->  ['word1', 'word2']

mixed=[1,2,3,"word1","word2",2.3,None]
print(mixed) #   o/p--> [1, 2, 3, 'word1', 'word2', 2.3, None]
print(mixed[-1]) # same as string last value dega   o/p-->None

mixed[2]="two" #this will replace 2nd index value by two
print(mixed) #   o/p--> [1, 2, 'two', 'word1', 'word2', 2.3, None]
mixed[1:]="two" # this will replace all the values after 1st index but o/p will be 1,"t","w","o" because it will treat as string
print(mixed) #   o/p--> [1, 't', 'w', 'o']
mixed[1:]=["two"] # this will replace all values after 1st index but will treated as a list mtlb two pura ek sath print hoga uper vale jesa nhi
print(mixed)  #  o/p-->  [1,'two']

mixed.append('grapes') # append is used to add an element to the list but at the last

#more methods to add 
# insert()
fruits1=['mango','apple']
fruits1.insert(1,'grapes') # insert element at given index 1st argument of index 2nd of what to add 
print(fruits1) #   o/p--> ['mango', 'grapes', 'apple']

# concatenation of list
fruits2=['chicu'] 
fruits=fruits1+fruits2 #will add two list but has to be stored in another list can't be stored in same one 
print(fruits) #   o/p--> ['mango', 'grapes', 'apple', 'chicu']

#extend() -> add two list but in same list no need to create a new list as above concatenation does
fruits2.extend(fruits1)
print(fruits2)  #   o/p--> ['chicu', 'mango', 'grapes', 'apple']

# difference b/t append and extend
# append me list k anadr list banti h it add in form of list and not string and extend add in form of string
fruits2.append(fruits1)
print(fruits2) #   o/p--> ['chicu', 'mango', 'grapes', 'apple', ['mango', 'grapes', 'apple']]


#delete data from list
#pop() -> if argument is not passed default it will delete last element and if passed it will delete elemnt of that index
car=["car1",'car2',"car3",'car4','car5']
car.pop() # delete last element
print(car) #  o/p-->  ['car1', 'car2', 'car3', 'car4']
car.pop(1) # delete the 1st index element
print(car) #  o/p-->  ['car1', 'car3', 'car4']

# del operator-->(delete)
del car[2] 
print(car) #  o/p-->  ['car1', 'car3']
# remove() method --> whwn you don't know the index you can simply use remove method and pass the string which is to be removed
car.remove('car3') # car4 at index 2 will be removed
print(car) #  o/p-->  ['car1']
# if for example the element is not present in the list ex car 6 and we write car.remove('car6) so it will give error x not in list
# if list has two values of same name mtlb car=['car1','car2','car1'] and we write car.remove('car1') so this will only remove 1st car1 and not 2nd ek hi delete hoga