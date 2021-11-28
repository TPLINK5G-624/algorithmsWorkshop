# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def mirrorTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return root
        q = [root]
        while q:
            node = q.pop(0)
            if node.left: q.append(node.left) 
            if node.right: q.append(node.right)
            #print(node)
            #print(q)
            t = node.left
            node.left = node.right
            node.right = t
        return root