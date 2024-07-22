#
# @lc app=leetcode id=704 lang=python3
#
# [704] Binary Search
#

# @lc code=start
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)
        while left < right:
            mid = left + (right-left) // 2
            if nums[mid] == target:
                return mid 
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid
        
        return -1
# @lc code=end