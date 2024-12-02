from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head is None:
            return head
        
        curr = head
        target = head

        for _ in range(n):
            if target:
                prev = target
                target = target.next
        if target == None:
            curr = curr.next
            return curr
        while target and target.next:
            curr = curr.next
            target = target.next
        curr.next = curr.next.next
          
        return head