"""
# Definition for a Node.
"""
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        temp = []
        nodelist = []
        randlist = []
        n = head
        a = None
        res = a        
        while n:
            a = Node(n.val, None, None)
            if not res:
                res = a 
            temp.append(a)
            nodelist.append(n)
            randlist.append(n.random)
            n = n.next
        nodelist.append(None)
        randlist.append(None)
        n = head
        count = len(temp)
        for i,k in enumerate(temp):
            if i < count-1:
               k.next = temp[i+1]
            if randlist[i] == None:
                k.random = None
            else:
                k.random = temp[nodelist.index(randlist[i])]   
        return res