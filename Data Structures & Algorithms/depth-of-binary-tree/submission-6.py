# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        #DFS iterative
        if root:
            stack = []
            stack.append([root, 1])
            max_depth = 1
        else:
            return 0

        while stack:
            temp, depth = stack.pop()
            max_depth = max(depth, max_depth)
            stack.append([temp.left, depth + 1]) if temp.left else None
            stack.append([temp.right, depth + 1]) if temp.right else None

        return max_depth