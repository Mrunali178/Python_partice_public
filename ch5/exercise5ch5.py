#define function which vtake 2 lists as input and return a list which contains common elements of both lists
def common_list(l,m):
    common=[]
    for i in l:
        for j in m:
            if(i==j):
                common.append(i)
    return common
num1=[1,2,3,4]
num2=[1,2,5,3]
print(common_list(num1,num2))