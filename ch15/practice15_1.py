#generator comprehension
#same as list only () this is used instead of []
square=[i**2 for i in range(1,11)]  #list comprehension
print(square)  #o/p--> [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
square=(i**2 for i in range(1,11))  #generator comprehension
print(square)  #o/p--> <generator object <genexpr> at 0x000001AA7FE6B5E0>
for i in square:
    print(i)
for i in square:
    print(i)#will only run once

