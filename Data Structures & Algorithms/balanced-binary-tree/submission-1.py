# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.valid = True
        
        def depth(node: Optional[TreeNode]) -> int:
            if node:
                l_depth = depth(node.left)
                r_depth = depth(node.right)

                if (l_depth - r_depth > 1) or (r_depth - l_depth > 1):
                    self.valid = False

                return 1 + max(l_depth, r_depth)
            else:
                return 0

        depth(root)

        return self.valid