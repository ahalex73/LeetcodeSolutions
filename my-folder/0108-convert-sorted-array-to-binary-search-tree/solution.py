# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        # Time: O(N) - number of nodes in tree
        # Space: O(log n) - due to recursion stack in balanced tree

        def constructBST(left, right):
            if left > right:
                return None
            
            mid = (left + right) // 2 
            node = TreeNode(nums[mid])
            node.left = constructBST(left, mid - 1)
            node.right = constructBST(mid + 1, right)

            return node
            
        return constructBST(0, len(nums) - 1)
            
        


        # i = 1

        # while(i < len(nums)):
        #     treeNode.left  = TreeNode()
        #     treeNode.left.val = nums[i]
            
        #     treeNode.right = TreeNode()
        #     treeNode.right.val = nums[i + 1]

        #     i += 1

