from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        maxSum = 0
        slow = head
        fast = head
    
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
       

        prev = None
        curr = head
        while curr and curr != slow:
            nextNode = curr.next
            curr.next = prev
            prev = curr
            curr = nextNode
        left = prev
        right = slow
        while left and right:
            maxSum = max(maxSum, left.val + right.val)
            left = left.next
            right = right.next
        return maxSum

