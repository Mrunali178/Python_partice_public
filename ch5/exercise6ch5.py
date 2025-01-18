#define a function to check how many list are in side the list ex- i/p-> [1,2,3,[4,5]] o/p--> 1
def count_list(l):
    count=0
    for i in l:
        if (type(i)==list):
            count+=1
    return count

mixed=[1,2,3,[4,5,6]]
print(count_list(mixed))