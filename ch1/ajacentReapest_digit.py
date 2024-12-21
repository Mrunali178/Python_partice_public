list_ele=[1,2,2,3,4,4]

def count_list(l):
    double=[]
    for i in range(0,len(l)-1):
        
        if(l[i]==l[i+1]):
            double.append((i,i+1))
    return double
print(count_list(list_ele))