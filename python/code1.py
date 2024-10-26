arr=[7,6,5,8,9,2,7,8]
str_arr=['Y',"A","S","H","y","a","s"]
str_arr = ([x.upper()  for x in str_arr])
checked_number={}
checked_str={}
for i in str_arr:
    if(i in checked_str):
        checked_str[i]+=1
    else:
        checked_str[i]=1
print(checked_str)

for i in arr:
    checked_number[i]=checked_number.get(i,0)+1
print(checked_number)
