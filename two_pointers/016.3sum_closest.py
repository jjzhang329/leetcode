#在上一题015的基础上，记录一个min_diff, result根据min_diff来变化
def threeSumClosest(nums,target):
    result = 0
    min_diff = float('inf')
    if len(nums) == 3:
        return sum(nums)
    nums.sort()
    for i in range(len(nums)):
        current = nums[i]
        left, right = i+1, len(nums)-1
        while left < right:
            three_sum = current + nums[left] + nums[right]
            if abs(target-three_sum) <= min_diff:
                result = three_sum
                min_diff = abs(target-three_sum)
            
            if three_sum > target:
                right -= 1
            elif three_sum < target:
                left += 1
            else:
                return target
            
    
    return result
nums = [-1,2,1,-4]
target = 1
print(threeSumClosest(nums, target))
#outpot 2