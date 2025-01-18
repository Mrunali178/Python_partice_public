# define a function which take list as a input and filter odd even
def even(l):
    even_list=[]
    
    for i in l:
        if (i%2==0):
            even_list.append(i)
    return even_list
def odd(l):
    odd_list=[]
    for i in l:
        if (i%2!=0):
            odd_list.append(i)
    return odd_list
num=[1,2,3,4,5,6,7]
even_element=even(num)
odd_elements=odd(num)
new=[]
new.append(odd_elements)
new.append(even_element)
print(new)

# optimal solution
def filter_nums(l):
    even_list=[]
    odd_list=[]
    for i in l:
        if (i%2==0):
            even_list.append(i)
        else:
            odd_list.append(i)
    return [even_list,odd_list]
            
num=[1,2,3,4,5,6,7]
elements=filter_nums(num)
print(elements)