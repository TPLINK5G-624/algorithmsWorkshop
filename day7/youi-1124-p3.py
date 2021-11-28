# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSym(self, left: TreeNode , right: TreeNode) -> bool:
        if not (left and right):
            if left == right :return True
            else: return False
        return left.val == right.val and self.isSym(left.left,right.right) and self.isSym(left.right,right.left)
    
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root: return True
        return self.isSym(root.left, root.right)