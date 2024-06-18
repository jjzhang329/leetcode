#
# @lc app=leetcode id=80 lang=python3
#
# [80] Remove Duplicates from Sorted Array II
#

# @lc code=start
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        left, right = 1, 2
        k = 0
        while right < len(nums):
            if nums[left] == nums[right] and nums[right] == nums[left-1]:
                right += 1
                k += 1
            else:
                nums[left+1] = nums[right]
                left += 1
                right += 1
        return len(nums)-k
# @lc code=end

