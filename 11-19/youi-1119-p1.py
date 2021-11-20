# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reversePrint(self, head: ListNode) -> 'list[int]':
        res = []
        node = head
        if not node :
            return []
        while node:
            res.insert(0,node.val)
            node = node.next
        return res
        