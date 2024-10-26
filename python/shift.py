l=[1,2,3,4,5]
n=3

def shift(l,n):
    for i in range(n):
        pop_tem=l.pop()
        l.insert(0,pop_tem)
        print(l)

    return l

print(shift(l,n))