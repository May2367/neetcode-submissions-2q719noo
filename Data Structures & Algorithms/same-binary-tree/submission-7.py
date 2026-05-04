# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        #recursive dfs
        
        self.valid = True
        
        def dfs(p: Optional[TreeNode], q: Optional[TreeNode]):
            if self.valid == False:
                return

            if p and q:
                if p.val != q.val:
                    self.valid = False

                dfs(p.left, q.left)
                dfs(p.right, q.right)
            elif p != None or q != None:
                self.valid = False

        dfs(p, q)
        return self.valid

        # Run Time: O(n), Space Complexity: O(n)