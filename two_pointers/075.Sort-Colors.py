def sortColors(nums):
    left, mid, right = 0, 0, len(nums)-1
    while mid <= right:
        if nums[mid] == 0:
            #swap with left
            nums[left], nums[mid] = nums[mid], nums[left]
            mid += 1
            left += 1
        elif nums[mid] == 2:
            #swap with right
            nums[right], nums[mid] = nums[mid], nums[right]
            right -= 1
            #mid doesnt move, cause might need to swap with left
        else:
            mid += 1

nums = [2,0,2,1,1,0]
sortColors(nums)
print(nums)
# Output: [0,0,1,1,2,2]

nums2 = [1, 0, 2]
sortColors(nums2)
print(nums2)
# Output: [0,1,2]