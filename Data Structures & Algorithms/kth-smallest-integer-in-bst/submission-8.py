# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.counter = 0
        
        def in_order(node):
            if not node:
                return None
            
            left = in_order(node.left)
            if left is not None:
                return left
                
            self.counter += 1

            if k == self.counter:
                return node.val

            right = in_order(node.right)
            if right is not None:
                return right
        
        return in_order(root)

# Time: O(h + k), Space: O(h), where h is height of tree and k target index
