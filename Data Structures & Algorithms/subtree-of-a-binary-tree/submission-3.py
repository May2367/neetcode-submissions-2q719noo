# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # A cleaner version
        def match(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
            if not p and not q:
                return True
            if not p or not q or p.val != q.val:
                return False

            return match(p.left, q.left) and match(p.right, q.right)

        def dfs(node: Optional[TreeNode]) -> bool:
            if not node:
                return False
            
            if node.val == subRoot.val and match(node, subRoot):
                return True
            
            return dfs(node.left) or dfs(node.right)

        return dfs(root)