# find avg from list using lambda l=[1,2,3],[4,5,6],[7,8,9] o/p= ([1+4+7]/3,[2,5,8]/3,[3,6,9]/3)
def avg_find(*args):
    avg=[]
    for pair in zip(*args):
        avg.append(sum(pair)/len(pair))
    return avg
print(avg_find([1,2,3],[4,5,6],[7,8,9]))  #o/p--> [4.0, 5.0, 6.0]

#using lambda
avg_finder=lambda *args:[sum(pair)/len(pair) for pair in zip(*args)]
print(avg_finder([1,2,3],[4,5,6],[7,8,9]))  #o/p--> [4.0, 5.0, 6.0]