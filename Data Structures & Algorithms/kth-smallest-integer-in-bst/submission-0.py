# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # Brute Force

        elements = []

        def traverse(node):
            if node:
                elements.append(node.val)
                
                traverse(node.left)
                traverse(node.right)
            else:
                return

        traverse(root)
        elements.sort()

        return elements[k - 1]

# 
