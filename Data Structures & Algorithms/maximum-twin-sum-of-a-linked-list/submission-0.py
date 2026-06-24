# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        curr  = head
        pairSumList = []
        while curr:
            pairSumList.append(curr.val)
            curr = curr.next
        result = 0
        i,j=0,len(pairSumList)-1
        while(i<j):
            result = max(result,pairSumList[i]+pairSumList[j])
            i+=1
            j-=1
        return result