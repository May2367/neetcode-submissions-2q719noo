# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        def traverse(lower, upper, node):
            if not node:
                return True

            if node.val <= lower or node.val >= upper:
                return False

            return (
                traverse(lower, node.val, node.left) and 
                traverse(node.val, upper, node.right)
                )

        return traverse(float("-inf"), float("inf"), root)

#
