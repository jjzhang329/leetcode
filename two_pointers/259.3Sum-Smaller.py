# 3Sum的另一个变种，3个数字相加小于target， count + 1
def twoSum(nums, start, target):
    count = 0
    left, right = start, len(nums)-1
    while left < right:
        if nums[left] + nums[right] >= target:
            right -= 1
        else:
            count += right - left 
            left += 1
    
    return count

def threeSumSmaller(nums, target):
    count = 0
    nums.sort()

    for i in range(len(nums)):
        count += twoSum(nums, i+1, target-nums[i])
    
    return count

nums = [-2,0,1,3]
target = 2
#Output: 2
print(threeSumSmaller(nums, target))