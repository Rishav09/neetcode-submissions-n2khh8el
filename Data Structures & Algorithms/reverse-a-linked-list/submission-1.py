# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        array_list = []
        curr = head
        while(curr):
            array_list.append(curr.val)
            curr = curr.next
        array_list.reverse()
        dummy = ListNode()
        curr = dummy
        for val in array_list:
            curr.next = ListNode(val)
            curr = curr.next
        return dummy.next