# if statement with list comprehension
# normal
num=list(range(1,11))
even_list=[]
for i in num:
    if(i%2==0):
        even_list.append(i)
print(even_list)

#list comprehension
numbers=list(range(1,11))
even_num=[i for i in numbers if i%2==0]
print(even_num) # o/p--> [2, 4, 6, 8, 10]
odd_num=[i for i in numbers if i%2!=0]
print(odd_num) # o/p--> [1, 3, 5, 7, 9]

#if else with lc
#if even print num*2 and if odd -ve (num)
res=[i*2 if i%2==0 else -i for i in numbers]
print (res) #o/p--> [-1, 4, -3, 8, -5, 12, -7, 16, -9, 20]