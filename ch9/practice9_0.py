# list comprehension
# with help of this we can create list in one line
squares=[i**2 for i in range(1,11)] # this will print squares of all nos. from 1 to 11
print(squares) # o/p--> [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

negative=[-i for i in range(1,11)]
print(negative)   # o/p--> [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10]

# print first letter of the string
names=['yash','rohit','ram']
new_list=[]
for name in names:
    new_list.append(name[0])
print (new_list) #o/p--> ['y', 'r', 'r']

#using list comprehension
names=['yash','rohit','ram']
new_list1=[name[0] for name in names]
print(new_list1) #o/p--> ['y', 'r', 'r']