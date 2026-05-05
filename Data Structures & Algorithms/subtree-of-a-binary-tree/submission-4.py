# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root and not subRoot:
            return True
        elif not root or not subRoot:
            return False

        #search through root until you find subRoot.
        #if not found, return False
        #if found, check if both are equal then return true

        self.valid_node = []
        def dfs(node: Optional[TreeNode], sub: Optional[TreeNode]):
            if node and sub:
                if node.val == sub.val:
                    self.valid_node.append(node)
            
                dfs(node.left, sub)
                dfs(node.right, sub)
            else:
                return None

        dfs(root, subRoot)

        def match(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
            if not p and not q:
                return True
            elif not p or not q or p.val != q.val:
                return False

            return match(p.left, q.left) and match(p.right, q.right)

        boolean = False
        for node in self.valid_node:
            boolean = boolean or match(node, subRoot)

        return boolean

        # Run Time: O(n^2), Space Complexity: O(n)