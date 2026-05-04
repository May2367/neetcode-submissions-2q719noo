# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def invert(temp):
            if temp:
                temp2 = temp.left
                temp.left = temp.right
                temp.right = temp2

                if temp.left:
                    invert(temp.left)

                if temp.right:
                    invert(temp.right)
        
        temp = root

        invert(temp)

        return temp