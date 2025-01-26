# set comprehension --> not used much o/p can be in any order
s={k**2 for k in range(1,6)}
print(s) #o/p--> {1, 4, 9, 16, 25}

names=['harshit','mohit','rohit']
first={i[0] for i in names}
print(first) #o/p--> {'r', 'm', 'h'}