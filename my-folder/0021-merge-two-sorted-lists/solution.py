# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # Iterative version
        # Time: O(n + m) n = # of nodes in list1, m = # of nodes in list2
        # Space: O(1)
    
        # Handle the case either of the lists are empty
        if not list1:
            return list2
        if not list2:
            return list1
        
        # Create dummy node to make new linked list
        dummy = ListNode(-1)
        curr = dummy # Current tail of linked list

        while(list1 and list2):
            if list1.val <= list2.val:
                curr.next = list1
                list1 = list1.next

            else:
                curr.next = list2
                list2 = list2.next
            
            # Increment
            curr = curr.next
        
        # Add the remaining elements after lists are not the same length
        if list1:
            curr.next = list1
        if list2:
            curr.next = list2
        
        return dummy.next # our first "element" is a dummy, return the head of the actual list we care about

         















        # # Recursive version

        # # Time Complexity: O(n + m) where n and m are the lengths of list1 and list2.

        # # Space Complexity: O(n + m) due to recursion stack (one frame per node).

        # # Base case
        # if list1 is None:
        #     return list2
        
        # if list2 is None:
        #     return list1
        
        # # Recursive case
        # if list1.val < list2.val:
        #     list1.next = self.mergeTwoLists(list1.next, list2)
        #     return list1
        # else:
        #     list2.next = self.mergeTwoLists(list1, list2.next)
        #     return list2
