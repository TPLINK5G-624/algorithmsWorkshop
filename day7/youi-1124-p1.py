# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSame(self, A:TreeNode, B:TreeNode) -> bool:
        if not B: return True
        if not A: return False
        return A.val == B.val and self.isSame(A.left, B.left) and self.isSame(A.right, B.right)

    def isSubStructure(self, A: TreeNode, B: TreeNode) -> bool:
        if not B:
            return False
        qA = [A]
        while qA:
            node = qA.pop()
            if self.isSame(node,B):
                return True
            if node.left: qA.append(node.left)
            if node.right: qA.append(node.right)
        return False