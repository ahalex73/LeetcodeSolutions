# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    # Time: O(n) Number of nodes in tree
    # Space: O(h) height of binary tree

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # Time: O(n) - numbers of nodes
        # Space: O(w) - width of the tree
        if not root:
            return 0

        q = deque()
        q.append(root)
        depth = 0

        while q:
            depth += 1

            for _ in range(len(q)):
                # Pop the parent node
                node = q.popleft() 
                # Append children nodes
                if(node.left):
                    q.append(node.left)
                if(node.right):
                    q.append(node.right)
            
        return depth
