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
        def is_mirror(leftNode, rightNode):
            if not leftNode and not rightNode:
                return True 

            if not leftNode or not rightNode:
                return False

            return leftNode.val == rightNode.val and is_mirror(leftNode.left, rightNode.right) and is_mirror(leftNode.right, rightNode.left)
            
        return is_mirror(root.left, root.right)
