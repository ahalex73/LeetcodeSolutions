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
        def check(node):
            if not node:
                return 0

            # Check for left subtree being balanced
            left = check(node.left)
            if left == -1:
                return -1

            # Check for right subtree being balanced
            right = check(node.right)
            if right == -1:
                return -1

            # Check if the height difference of the left and right subtrees are balanced i.e  height_diff <= 1
            if abs(left - right) > 1:
                return -1

            # Return the height
            return max(left, right) + 1

        return check(root) != -1
