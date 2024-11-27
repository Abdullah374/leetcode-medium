from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return head

        even = head.next
        purpose = even
        odd = head
        while odd.next and odd.next.next:
            purpose = odd.next
            odd.next = odd.next.next
            purpose.next = odd.next.next
            odd = odd.next
        
        odd.next = even
            
        return head
