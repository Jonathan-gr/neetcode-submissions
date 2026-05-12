# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        


        res = ListNode(0)
        dummy = res
        total=0
        carry=0

        while l1 or l2 or carry>0:

            if l1:
                total+=l1.val
                l1=l1.next
            if l2:
                total+=l2.val
                l2=l2.next
            

            carry = total//10
            n = total%10
            total=carry

            dummy.next = ListNode(n)
            dummy = dummy.next
        return res.next