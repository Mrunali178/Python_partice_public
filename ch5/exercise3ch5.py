#define a function that takes list of words as argument and return list with reverse of every element in that list
def reverse_elements(l):
    elements=[]
    for i in l:
        elements.append(i[::-1])
    return elements
# lst=['abc','cde','xyz']
# user input
lst=[]
n=int(input("enter no of elements"))
for i in range(0,n):
    ele=input("enter elements in list: ")
    lst.append(ele)
print(lst)
print(reverse_elements(lst))