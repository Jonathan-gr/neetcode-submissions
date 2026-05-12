# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        

        res = ListNode(0)
        
        res.next = head

        curr = res
        length = -1 
        while curr:
            curr = curr.next
            length+=1
        
        cut_off = length-n
        curr=res
        for _ in range(cut_off):
            curr=curr.next
        
        curr.next = curr.next.next
        return res.next

