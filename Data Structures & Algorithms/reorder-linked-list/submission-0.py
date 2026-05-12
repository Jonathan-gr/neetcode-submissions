# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        

        slow,fast = head,head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        
        
        prev = None
        while slow:
            temp = slow.next
            slow.next = prev
            prev=slow
            slow=temp
        

        res = ListNode(0)
        dummy = res

        while head and head.next:
            dummy.next = head
            head = head.next
            dummy = dummy.next

            dummy.next = prev
            prev=prev.next
            dummy = dummy.next
       