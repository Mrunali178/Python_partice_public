l=[1,4,7,8,2,3,5,4]
target = 8

# def get_index_sum(l,n):
#     return_list=[]
#     for i in range(len(l)):
#         for j in range(i+1,len(l)):
#             if(l[i]+l[j]==n):
#                 return_list.append((i,j))
#     return return_list
            
# print(get_index_sum(l,target))

def using_dict(l,n):
    dict_result={}
    return_list=[]
    for i,j in enumerate(l):
        diff= n-j
        if diff in dict_result:
            return_list.append((dict_result[diff],i))
           
        else:
             dict_result[j]=i
            
    return return_list
            
print(using_dict(l,target))


