#all and any function
#all gives o/p ture if all values for the condition are true and any gives true if even one element satisfy and is true
nums1=[13,2,3,5,7]
print(any([nums%2==0 for nums in nums1])) #o/p--> True

nums1=[12,2,3,12,12]
print(all([nums%2==0 for nums in nums1])) #o/p--> False

nums1=[12,2,4,6,8]
print(all([nums%2==0 for nums in nums1])) #o/p--> True

#practice check input for sum should be int or float
def my_sum(*args):
    if all(type(arg)==int or type(arg)==float for arg in args):
        total=0
        for i in args:
            total+=i
        return total
    else:
        return "wrong input"
    
print(my_sum(1,2,3,4.5,["mru"],"abc"))  #o.p--> wrong input
print(my_sum(1,2,3,4.5))  #o.p--> 10.5

# advanced max min and sorted function --> todo later

#docstrings and help function
def add(a,b):
    '''this function return sum of two numbers'''
    return a+b
print(add.__doc__) #o/p--> this function return sum of two numbers
print(len.__doc__) #o/p--> Return the number of items in a container.
print(help(sum))