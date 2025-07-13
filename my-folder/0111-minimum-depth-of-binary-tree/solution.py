# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # Time: O(n) - number of nodes
    # Space: O(h) - height of recursion stack - O(n) in worst case 

    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        # Handle leaf nodes - We must do this considering if we only returned
        # 1 + min(self.minDepth(root.left), self.minDepth(root.right)) then we would have a situation
        # Where min(self.minDepth(None), self.minDepth(non-empty)) = min(0, real_depth) = 0
        # Creating a non-existent path that states that the minimum path length is 0 instead of how long it took to get there

        if not root.left:
            return self.minDepth(root.right) + 1 # Only right path
        if not root.right:
            return self.minDepth(root.left) + 1  # Only left path
        
        return 1 + min(self.minDepth(root.left), self.minDepth(root.right)) # Take the shorter path
