# 再3Sum基础上再套一圈
def fourSum(nums, target):
    result = []
    nums.sort()

    for i in range(len(nums)):
        if nums[i] > target:
            break

        if i > 0 and nums[i] == nums[i-1]:
            continue 

        for j in range(i+1, len(nums)):
            if j > i + 1 and nums[j] == nums[j-1]:
                continue 
            left, right = j+1, len(nums)-1
            while left < right:
                four_sum = nums[i] + nums[j] + nums[left] + nums[right]
                if four_sum < target:
                    left += 1
                elif four_sum > target:
                    right -= 1
                else:
                    result.append([nums[i], nums[j], nums[left], nums[right]])
                    left += 1
                    right -=1
                    while left < right and nums[left] == nums[left-1]:
                        left += 1
    return result

nums = [1,0,-1,0,-2,2]
target = 0
# Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
print(fourSum(nums, target))