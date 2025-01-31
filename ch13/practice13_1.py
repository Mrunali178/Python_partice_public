# map function
def squares(a):
    return a**2
nums=[1,2,3,4]
new_list=[]
for i in nums:
    new_list.append(squares(i))
print(new_list)     #o/p--> [1, 4, 9, 16]


#using lambda and map
square=list(map (lambda a:a**2,nums))
print(square) #o/p--> [1, 4, 9, 16]

square2=map (lambda a:a**2,nums)
print(square2) #o/p---> <map object at 0x00000151ADD4B520>

#map is an iterator mweans we can iterate through it only once
square1=map(squares,nums)
for i in square1:
    print(i)
#o/p--> 1
    # 4
    # 9
    # 16


def squ(a):
    res=[]
    for i in a:
        res.append(i**2)
    return res
s=[1,2,3,4]
print(squ(s))