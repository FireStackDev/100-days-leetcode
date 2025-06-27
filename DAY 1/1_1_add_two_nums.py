# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode()
        tail = head

        carry = 0
        p1, p2 = l1, l2

        while p1 or p2 or carry:  
            v1 = p1.val if p1 else 0
            v2 = p2.val if p2 else 0

            total = v1 + v2 + carry  # current digit + carry
            carry = total // 10  # new carry
            digit = total % 10  # node value

            tail.next = ListNode(digit)
            tail = tail.next

            # advance the input pointers
            p1 = p1.next if p1 else None
            p2 = p2.next if p2 else None

        return head.next
