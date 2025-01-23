#sets
#unordered collection of unique items (no indexing allowed)
# no duplicate elements allowed and is mutable
# l=[1,2,[3,4],[3,4]] # how to convert list in list to set and remove duplicate
# for i,j in enumerate(l):
#     if(type(j)==list):
#         l[i]=set(j)
# print(l) #o/p--> [1, 2, {3, 4}, {3, 4}]
# for i,j in enumerate(l):
#     print(i,j) #i is printing index and j is priting element

s={1,2,3,2}
print(s) #o/p--> {1, 2, 3}

l=[1,2,3,2,4,5,6,3]
s1=set(l)
print(s1)  #o/p--> {1, 2, 3, 4, 5, 6}

s2=list(set(l)) #removing duplicate elements from list 
print(s2)  #o/p--> [1, 2, 3, 4, 5, 6]

#methods in set
# 1) add method--> to add element
s.add(4)
s.add(5)
s.add(4) # this 4 will not be added as duplicates not allowed
print(s) #o/p--> {1, 2, 3, 4, 5}

# 2) remove method--> deletes element from set
s.remove(5)
print(s) #o/p--> {1, 2, 3, 4}
# if we pass element that is not in set it will give error KeyError
# s.remove(6)
# print(s) # KeyError: 6

# 3) discard method--> removes element from set but if it is not present will not give error
s.discard(3)
print(s)#o/p--> {1, 2, 4}
s.discard(6)
print(s)#o/p--> {1, 2, 4}

# 4) clear method--> khali kr deti h set ko
# s.clear()
# print(s) #o/p--> set()

# 5) copy method
s1=s.copy() #makes copy of the set 
print(s1)  # o/p--> {1, 2, 4}
print(s)  # o/p--> {1, 2, 4}
  
s2={1,1.2,(3,4)} # we can store tuple in set but not list and dictionary
print(s2) # o/p-->{1, (3, 4), 1.2} set and dict can be printed in any order

# s3={1,1.2,[3,4]} # we can store tuple in set but not list and dictionary
# print(s3)   # o/p--> TypeError: unhashable type: 'list'

# in keyword--> checks element whether present or not
if(1.2 in s2):
    print("present")
else:
    print('not present') 

#for loop---> it will print in any order as set is unorderd collection -- no indexs
for i in s2:
    print (i)   #o/p-->1
                # (3, 4)
                # 1.2

# set maths --> union(|) intersection(&)
set_ele={1,2,3,4}
set_list={3,4,5,6}
print(set_ele|set_list)  #o/p--> {1, 2, 3, 4, 5, 6}
print(set_ele&set_list)  #o/p--> {3, 4}