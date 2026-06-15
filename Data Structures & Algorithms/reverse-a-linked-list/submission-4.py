# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        prev, curr = None, head
        while curr:
            temp_next = curr.next # Save
            curr.next = prev # Flip
            prev = curr # Move prev
            curr = temp_next # Move curr
        return prev
        