# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        a,b = list1, list2
        
        result = ListNode()
        
        pointer = result
        while a and b:
            if a.val <= b.val:
                pointer.next = a
                a = a.next
            else:
                pointer.next = b
                b = b.next
            pointer = pointer.next
        
        pointer.next = a if a else b

        return result.next