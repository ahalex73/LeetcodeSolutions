# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # Time: O(n)  # Total nodes in binary tree
    # Space: O(h) # Stack usage during code run - height of binary tree

    def isSymmetric(self, root: Optional[TreeNode]) -> bool:    
        # ln = leftNode and rn = rightNode in terms of symmetry
        def is_mirror(ln, rn):
            # Base case
            if not ln and not rn:
                return True
            
            if not ln or not rn:
                return False
            
            return ln.val == rn.val and is_mirror(ln.left, rn.right) and is_mirror(ln.right, rn.left)
        
        return is_mirror(root.left, root.right)
