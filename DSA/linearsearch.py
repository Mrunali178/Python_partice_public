# linear search iterative (O(n))
size=int(input("enter size of list: "))
res=[]
for i in range(0,size):
    element=int(input("enter element: "))
    res.append(element)
target=int(input("enter number to be searched: "))

def iterative_linear(l,target):
    for i in range(0,len(res)):
        if res[i]==target:
            print(f"element found at index: {i+1}")
            found=True
            break
    if not found:
        print("element not found")


#recursive
def recursive_linear(l,i,n,target):
    if i>n:
        return False
    if l[i]==target:
        return True
    return(recursive_linear(l,i+1,n,target))

iterative_linear(res,target)   #o/p--> element found at index: 4
print(recursive_linear(res,0,size-1,target))  #o/p--> True