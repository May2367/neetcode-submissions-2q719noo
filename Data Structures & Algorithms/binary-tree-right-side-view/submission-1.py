# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        if root:
            q = collections.deque([root])
        else:
            return res

        while q:
            curr_len = len(q)

            for i in range(curr_len):
                curr_node = q.popleft()
                
                if curr_node.left:
                    q.append(curr_node.left)
                if curr_node.right:
                    q.append(curr_node.right)

                if i == curr_len - 1:
                    res.append(curr_node.val)
                
        return res

# Basically level order traversal but filter for the last val at each level
