# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Time: O(n)
        # Space: O(1)

        prev = None
        curr = head

        while(curr):
            temp = curr.next # Store the next node in original LL

            curr.next = prev
            prev = curr

            curr = temp 

        return prev 
