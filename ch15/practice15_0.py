#intro to generators
# A generator in Python is a special type of function that allows you to produce a sequence of values lazily, one at a time, instead of generating all values at once and storing them in memory. 
# This makes them more memory-efficient compared to lists, especially for large datasets.
#noraml function
def nums(n):
    for i in range(1,n+1):
        print(i,end=" ")
nums(10)
#generators
def nums1(n):
    for i in range(1,n+1):
        yield i
print("\n",nums1(10))  #o/p-->  <generator object nums1 at 0x0000015CC64702E0>
#we use yield in generators instead of return and print
#we can use for loop in this 
for i in nums1(10):
    print(i)

#generators don't store elements so first 1 will get in memeory printed then removed from memore then 2 will come and go then 3 and soon and in this way for loop will work
