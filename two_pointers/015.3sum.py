# 需要复习一下 twoSumII, 基本上是在twoSumII情况下再套一层，注意要确认不要重复同样的组合
def twoSum(nums, start, result):
    left, right = start+1, len(nums)-1
    while left < right:
        three_sum = nums[start] + nums[left] + nums[right]
        if three_sum > 0:
            right -= 1
        elif three_sum < 0:
            left += 1
        else:
            result.append([nums[start], nums[left], nums[right]])
            left += 1
            right -= 1
            #避免会用相同数字
            while left < right and nums[left] == nums[left-1]:
                left += 1

    return result

def threeSum(nums):
    result = []
    # 数组从小到大排序，这样方便左右pointer移动
    nums.sort()
    for i in range(len(nums)):
        if nums[i] > 0:
            break 
        #确保数字不同，避免之后出现相同组合
        if i == 0 or nums[i] != nums[i-1]:
            twoSum(nums, i, result)
    
    return result

nums = [-1,0,1,2,-1,-4]
print(threeSum(nums))
# Output: [[-1,-1,2],[-1,0,1]]
