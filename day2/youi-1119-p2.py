# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        node = head
        bnode = None
        anode = None
        while node:
            anode = ListNode(node.val)
            anode.next = bnode
            bnode = anode
            node = node.next
        return anode
        