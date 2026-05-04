# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        def depth(node: Optional[TreeNode]) -> int:
            if node:
                return 1 + max(depth(node.left), depth(node.right))
            else:
                return 0

        l = self.diameterOfBinaryTree(root.left)
        r = self.diameterOfBinaryTree(root.right)
        diameter = max(depth(root.left) + depth(root.right), l, r)

        return diameter