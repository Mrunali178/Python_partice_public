#zip function---> iterator used to combine(zip) two or more lists(iterables)
user=[1,2,3]
names=["yash","mru","hashit"]
print(list(zip(user,names)))  #o/p--> [(1, 'yash'), (2, 'mru'), (3, 'hashit')]
print(zip(user,names)) #o/p--> <zip object at 0x000002CA3596FBC0>

# if 2 elemnts in tuples of a list we can convert in dict as well
print(dict(zip(user,names))) #o/p--> {1: 'yash', 2: 'mru', 3: 'hashit'}

#if one has less elements than other zip will give o/p according to less one
user1=[1,2]
names=("yash","mru","jyoti")
last_name='strs','abc','dfc'
print(list(zip(user1,names)))  #o/p--> [(1, 'yash'), (2, 'mru')]
print(list(zip(user1,names,last_name)))  #o/p--> [(1, 'yash', 'strs'), (2, 'mru', 'abc')]
# print(dict(zip(user1,names,last_name)))  #o/p--> ValueError: dictionary update sequence element #0 has length 3; 2 is required


# covert from l=[(1,2),(3,4),(5,6)] to this  l1=[1,3,5] l2=[2,4,6] using zip
# *operator with zip
l=[(1,2),(3,4),(5,6)]
print(zip(*l)) #o/p--> <zip object at 0x0000022A8F93F540>
print(list(zip(*l))) #o/p--> [(1, 3, 5), (2, 4, 6)]
l1,l2=list(zip(*l))
print(l1)  #o/p--> (1, 3, 5)
print(l2)  #o/p--> (2, 4, 6)
print(list(l1))  #o/p--> [1, 3, 5]
print(list(l2))  #o/p--> [2, 4, 6]

#now if you want to find max from two list mtlb l1=[1,4,5] l2=[2,3,4] o/p should be [2,4,5]
l1=[1,4,5] 
l2=[2,3,4]
res=[]
for pair in zip(l1,l2):
    res.append(max(pair))
print(res)  #o/p--> [2, 4, 5]