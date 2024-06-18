#
# @lc app=leetcode id=26 lang=python3
#
# [26] Remove Duplicates from Sorted Array
#

# @lc code=start
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        left, right = 0, 1
        k = 0

        while right < len(nums):
            if nums[left] == nums[right]:
                k += 1
                right += 1
            else:
                nums[left+1] = nums[right]
                left += 1
                right += 1
                
        return len(nums)-k

# @lc code=end