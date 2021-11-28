# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        queue = []
        resList = []
        res = []
        queue.append(root)
        queue.append('T')
        while queue:
            node = queue.pop(0)
            if not node :
                continue
            if node != 'T':
                res.append(node.val)
                queue.append(node.left)
                queue.append(node.right)
            #print(node)
            else:
                resList.append(res)
                res = []
                if queue:
                    queue.append('T')
        resList.pop() #清除最后一个
        return resList