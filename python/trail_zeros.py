l=[1,4,5,7,0,8,0,6]
# count=0
# for i in l:
#     if i==0:
#         l.remove(i)
#         count+=1
# while count!=0:
#     l.append(0)
#     count-=1
# print(l)

non_zero_helper =0
for i in range(len(l)):
    if l[i]==0:
        l[non_zero_helper],l[i]=l[i],l[non_zero_helper]
        non_zero_helper+=1
print(l)
