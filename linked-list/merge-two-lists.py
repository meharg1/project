# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        lnk = ListNode()
        curr = lnk
        while list1 and list2:
            
            if list2.val > list1.val:
                lnk.next = list1
                list1 = list1.next
                
            else:
                lnk.next = list2
                list2 = list2.next

            lnk = lnk.next

            
        if list1:
            lnk.next = list1
        if list2:
            lnk.next = list2

        
        return curr.next
