# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diameter = 0

        def depth(node: Optional[TreeNode]) -> int:
            if node:
                l = depth(node.left)
                r = depth(node.right)

                self.diameter = max(r + l, self.diameter)
                return 1 + max(l, r)
            else:
                return 0

        depth(root)
        
        return self.diameter