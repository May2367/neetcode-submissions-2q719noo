# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        #BFS Iterative
        if not root:
            return 0

        queue = deque()
        queue.append(root)
        depth = 0

        while queue:
            depth += 1

            length = len(queue)
            for i in range(length):
                temp = queue.popleft()
                if temp:
                    queue.append(temp.left) if temp.left else None
                    queue.append(temp.right) if temp.right else None

        return depth