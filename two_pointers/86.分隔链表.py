#
# @lc app=leetcode.cn id=86 lang=python3
#
# [86] 分隔链表
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        dummy1, dummy2 = ListNode(), ListNode()
        p1 = dummy1
        p2 = dummy2
        current = head 

        while current:
            if current.val < x:
                p1.next = current
                p1 = p1.next
            else:
                p2.next = current
                p2 = p2.next 
            next = current.next
            current.next = None
            current = next

        p1.next = dummy2.next 
        return dummy1.next



# @lc code=end