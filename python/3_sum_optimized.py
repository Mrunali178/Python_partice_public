def three_sum_optimized(l):
    my_set=set()
    l.sort()
    for i in range(len(l)):
        j = i+1
        k = len(l)-1
        while(j<k):
            sum= l[i]+l[j]+l[k]
            if(sum==0):
                my_set.add(tuple([l[i],l[j],l[k]]))
                j+=1
                k-=1
            elif(sum<0):
                j+=1
            else:
                k-=1
    ans= [list(x) for x in my_set ]
    return ans


l=[-1,4,2,8,2,-3,-5,-1,4]
print(three_sum_optimized(l))
