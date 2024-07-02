#
# @lc app=leetcode id=23 lang=python3
#
# [23] Merge k Sorted Lists
#

# @lc code=start
# Definition for singly-linked list.
import heapq
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        pqueue = []
        dummy = ListNode()
        tail = dummy 

        for head in lists:
            if head:
                heapq.heappush(pqueue, (head.val,id(head), head))
        while pqueue:
            node = heapq.heappop(pqueue)[2]
            tail.next = node 
            if node.next:
                heapq.heappush(pqueue, (node.next.val, id(node.next),node.next))
            tail = tail.next 
        
        return dummy.next

# @lc code=end

