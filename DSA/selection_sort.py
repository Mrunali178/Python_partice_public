#selection sort
def selection_sort(l):
    for i in range(0,len(l)):
        min_ele=i
        for j in range (i+1,len(l)):
            if l[j]<l[min_ele]:
                min_ele=j
        l[i],l[min_ele]=l[min_ele],l[i]
        print(l)
    return l
l=[4,1,5,2,3]
print(selection_sort(l))

