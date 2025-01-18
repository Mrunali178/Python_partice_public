# define a function to reverse the list without using step argument and reverse function
num=[]
n=int(input("enter no of elements you want in list: "))
for i in range(0,n):
    lst=int(input(f"enter elements in list at position {i+1}: "))
    num.append(lst)
print(num)
def reverse_list(l):
    rev=[]
    for i in range(0,len(l)):
        popped_item=num.pop()
        rev.append(popped_item)
    return rev
print(reverse_list(num))

#for short we can use reverse method and string slicing
#def reverse_list(l):
    # l.reverse() #we cann't write return l.reverse as first we have to store the reversed list then return
    # return l
# and by using string slicing
#def reverse_list(l):
    # return l[::-1]