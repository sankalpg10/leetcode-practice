"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []
"""
O(N) | O(1)
class Solution:
    def findRoot(self, tree: List['Node']) -> 'Node':
        valSum = 0
        for i in range(len(tree)):
            valSum += tree[i].val
            for child in tree[i].children:
                valSum -= child.val
                
        for node in tree:
            if node.val == valSum:
                return node
            
        return None

O(N) | O(N)
class Solution:
    def findRoot(self, tree: List['Node']) -> 'Node':
        
        inDegrees = {node.val: 0 for node in tree} 
        
        for node in tree:
            for child in node.children:
                inDegrees[child.val] += 1
                
        for i in range(len(tree)):
            if inDegrees[tree[i].val] == 0:
                return tree[i]
            
        return None
