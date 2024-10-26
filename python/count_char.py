s="abcabbccaassnb"

# code to get the count of total char a4b4c3s2n1
# new_dict={}
# for i in s:
#     if i in new_dict:
#         new_dict[i]+=1
#     else:
#         new_dict[i]=1
# s=""
# for i,j in new_dict.items():
#     s=s+str(i)+str(j)

# print(s)
i=0
n = len(s)
ans=""
while i<n:
    j=i+1
    count=1
    while j<n and (s[i]==s[j]):
        j+=1
        count+=1
    ans = ans+s[i]+str(count)
    i=j

print(ans)

