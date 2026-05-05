# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        #Serialization and Pattern Matching

        string = ""
        sub = ""

        def serialize(string: str, node: Optional[TreeNode]) -> str:
            if not node:
                return "#$"
            else:
                return str(node.val) + "$" + serialize(string, node.left) + serialize(string, node.right)

        string = serialize(string, root)
        sub = serialize(sub, subRoot)

        return sub in string