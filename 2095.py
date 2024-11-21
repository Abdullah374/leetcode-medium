from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast = head
        slow = head

        if head is None:
            return head
        if head.next is None:
            head = None

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        curr = head
        while curr and curr.next != slow:
            curr = curr.next
        if curr:
            curr.next = curr.next.next

        return head