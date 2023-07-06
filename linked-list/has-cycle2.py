# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False
        pointer1 = head
        pointer2 = head.next
        while pointer2 and pointer2.next:
            if pointer1 == pointer2:
                return True
            pointer1 = pointer1.next
            pointer2 = pointer2.next.next
            
        
        return False
