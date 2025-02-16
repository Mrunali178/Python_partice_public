nums=[6,7,8,12]
target=12
for i in range(0,len(nums)):
    for j in range(i+1,len(nums)):
        if nums[i]>nums[j]:
            temp=nums[i]
            nums[i]=nums[j]
            nums[j]=temp
print(nums)