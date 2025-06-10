# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# class Solution:
#     def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
#         dummy_head = ListNode(0)
#         current = dummy_head
#         carry = 0

#         while l1 or l2 or carry:
#             # Get current values (or 0 if the list is done)
#             val1 = l1.val if l1 else 0
#             val2 = l2.val if l2 else 0

#             # Sum and carry
#             total = val1 + val2 + carry
#             carry = total // 10
#             new_digit = total % 10

#             # Add new node
#             current.next = ListNode(new_digit)
#             current = current.next

#             # Move to next nodes
#             if l1:
#                 l1 = l1.next
#             if l2:
#                 l2 = l2.next

#         return dummy_head.next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(None)
        curr = dummy
        quotient = 0

        while l1 or l2:
            if l1 and l2:
                total = l1.val + l2.val + quotient
            elif l2:
                total = l2.val + quotient
            else:
                total = l1.val + quotient

            quotient = total // 10
            remainder = total % 10
            new_node = ListNode(remainder)
            curr.next = new_node
            curr = curr.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        
        if quotient != 0:
            new_node = ListNode(quotient)
            curr.next = new_node
        
        return dummy.next