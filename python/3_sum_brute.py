def three_sum_brute_force(l):
    l.sort()
    my_set=set()
    for i in range(len(l)):
        for j in range(i+1,len(l)):
            for k in range(j+1,len(l)):
                sum= l[i]+l[j]+l[k]
                if(sum==0):
                    temp = [l[i],l[j],l[k]]
                    my_set.add(tuple(temp))

    ans= [list(x) for x in my_set]
    return ans

l=[-1,4,2,8,2,-3,-5,-1,4]
print(three_sum_brute_force(l))


