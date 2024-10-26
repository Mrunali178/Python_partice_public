# l=[2,0,2,1,1,0]
# for i in range(len(l)):
#     j=i+1
#     while j<len(l):
#         if l[i]>l[j]:
#             l[i], l[j] = l[j], l[i]
# print(l)
l = [2, 0, 2, 1, 1, 0]

for i in range(len(l)):  # Outer loop
    j = i + 1
    while j < len(l):  # Inner loop
        if l[i] > l[j]:  # Swap if the current element is greater than the next element
            l[i], l[j] = l[j], l[i]
        j += 1

print(l)
