# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[int]:
        queue = []
        res = []
        queue.append(root)
        while queue:
            node = queue.pop(0)
            if not node:
                continue
            res.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        return res