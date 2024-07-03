#
# @lc app=leetcode id=142 lang=python3
#
# [142] Linked List Cycle II
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast, slow = head, head 
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next 
            if fast == slow:
                break
        if fast == None or fast.next == None:
            return None
        slow = head 
        while fast != slow:
            fast = fast.next 
            slow = slow.next 
        
        return fast
# @lc code=end

