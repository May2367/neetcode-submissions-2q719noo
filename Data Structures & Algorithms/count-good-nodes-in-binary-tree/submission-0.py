# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.count = 0
        if not root:
            return 0

        def traverse(node, curr_max):
            if not node:
                return

            if node.val >= curr_max:
                self.count += 1

            curr_max = max(node.val, curr_max)

            traverse(node.left, curr_max)
            traverse(node.right, curr_max)

        traverse(root, root.val)

        return self.count

#
