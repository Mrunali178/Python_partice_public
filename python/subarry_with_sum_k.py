nums= [1]
for i in range(1,len(nums)):
    nums[i]+= nums[i-1]
print(nums)