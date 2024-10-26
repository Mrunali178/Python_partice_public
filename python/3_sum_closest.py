def three_sum_closest(l, target):
    l.sort()
    closest_sum=float('inf')
    for i in range(len(l)):  

        j = i+1
        k = len(l)-1

        while j<k:
            current_sum = l[i]+l[j]+l[k]

            if abs(current_sum-target)< abs(closest_sum-target):
                closest_sum=current_sum


            if current_sum==target:
                return current_sum
            elif current_sum>target:
                k-=1
            elif current_sum<target:
                j+=1
    
    return closest_sum

l= [-1,2,1,-4]
target = 1 
print(three_sum_closest(l,target))
        
    
        
