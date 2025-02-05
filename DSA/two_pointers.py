#used on sorted arrays 
#two sum 
# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
#here its best to hashmap as in this the original indices will get chnged its just to show how two pointers approach work
def TwoPointers(l,target):
    res=[]
    l.sort()
    i,j=0,len(l)-1
    while i<j:
        if l[i]+l[j]==target:
            res.append(i)
            res.append(j)
            break
        elif(l[i]+l[j]>target):
            j-=1
        else:
            i+=1
    return res
l=[2,7,11,15]
target=9
print(TwoPointers(l,target))