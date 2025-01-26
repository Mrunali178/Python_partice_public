# using list comprehension reverse of everuy string
l=['abc','tuv','xyz']
def reverse_string(l):
    reverse=[i[::-1] for i in l]
    return reverse
print(reverse_string(l)) #o/p--> ['cba', 'vut', 'zyx'] 