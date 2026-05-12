"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        

        random_pointer_hash = {None:None}
        curr = head

        while curr:
            random_pointer_hash[curr]=Node(curr.val,curr.next,curr.random)
            curr = curr.next
        
        res = None
  

        curr = head
        while curr:
            res = random_pointer_hash[curr]
            res.next = random_pointer_hash[curr.next]
            res.random = random_pointer_hash[curr.random]
            curr = curr.next
        return random_pointer_hash[head]








