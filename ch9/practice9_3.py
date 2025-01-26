#nested list using lc
example=[[1,2,3],[1,2,3],[1,2,3]]
nested_comp=[[i for i in range(1,4)] for j in range(3)]
print(nested_comp) # o/p--> [[1, 2, 3], [1, 2, 3], [1, 2, 3]]

#normal
new_list=[]
for j in range(3):
    new_list.append([1,2,3])
print(new_list)