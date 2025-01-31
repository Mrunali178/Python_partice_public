#filter function 
#used to filter out elements from an iterable based on whether they satisfy a certain condition. It returns only the elements for which the condition is True.
def is_even(a):
    return a%2==0
nums=[3,4,5,1,7,8,6]
evens=filter(is_even,nums)
# print(list(evens))  #o/p--> [4, 8, 6]

#filter is iterator same as map we can iterate but only once
for i in evens:
    print(i)
#o/p-->  4
        # 8
        # 6
print(evens)   #o/p--> <filter object at 0x000001F8FE0AADD0>


#using lambda
even_num=tuple(filter(lambda a:a%2==0,nums))
print(even_num)  #o/p--> (4, 8, 6)

