# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        stack, stackSaving = [],[]
        res, resList = [], []
        stack.append(root)
        flag = False
        while stack:
            for i in range(0,len(stack)):
                node = stack.pop(0)
                if not node:
                    continue
                res.append(node.val)
                stackSaving.append(node.left)
                stackSaving.append(node.right)
            if flag :
                res.reverse()
            flag = not flag
            resList.append(res)
            res = []
            stack = stackSaving
            stackSaving = []
        resList.pop()
        return resList