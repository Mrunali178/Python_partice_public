# iterative
 
l=[1,2,3,4,5,6,7]
target=7
def iterative_binary_search(l,target):
    low=0
    high=len(l)-1
    while low<=high:
        mid=(low+high)//2
        if l[mid]==target:
            return f"element found at location {mid+1}"
        elif(l[mid]>target):
            high=mid-1
        elif(l[mid]<target):
            low=mid+1
    return -1
print(iterative_binary_search(l,target))


# recursive --> 

def recursive_binary(l,low,high,target):
    mid=(low+high)//2
    if low<=high:
        if target>l[mid]:
            return recursive_binary(l,mid+1,high,target)
        elif target<l[mid]:
            return recursive_binary(l,low,mid-1,target)
        else:
            return mid+1
    return False
print(recursive_binary(l,0,len(l)-1,7))  

# Find the first and last occurrence of an element in a sorted array.
l2=[1,1,1,2,3,4,5,6,7]

def bruteforce_find_occurence(l,target):
    res=[]   # this takes O(n) time 
    for i in range (0,len(l)):
        if l[i]==target:
            res.append(i)
    return [res[0],res[-1]]
print(bruteforce_find_occurence(l2,1))

#use binary search
#optimized
def first_occurence(l,target):
    low=0
    high=len(l)-1
    first=-1
    while low<=high:
        mid=(low+high)//2
        if l[mid]==target:
            first=mid
            high=mid-1
        elif l[mid]<target:
            low=mid+1
        else:
            high=mid-1
    return first 

def last_occurence(l,target):
    low=0
    high=len(l)-1
    last=-1
    while low<=high:
        mid=(low+high)//2
        if l[mid]==target:
            last=mid
            low=mid+1
        elif l[mid]<target:
            low=mid+1
        else:
            high=mid-1
    return last 
def find_first_and_last(l, target):
    return (first_occurence(l, target), last_occurence(l, target))

l1 = [1,1,1,2, 3, 4, 5]
target = 1
result = find_first_and_last(l1, target)
print(f"First occurrence: {result[0]}, Last occurrence: {result[1]}")  #o/p--.First occurrence: 0, Last occurrence: 2
