# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # Time: O(n) - Number of nodes
    # Space: O(h) - Height of tree - best case O(log n)
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(root):
            if not root:
                return [True, 0] # Returning height of 0
            
            left_balanced, left_height = dfs(root.left)
            right_balanced,  right_height = dfs(root.right)

            is_balanced = left_balanced and right_balanced and abs(left_height - right_height) <= 1

            return [is_balanced, 1 + max(left_height, right_height)]

        return dfs(root)[0] # Returns a true or false considering we have two return values

            


