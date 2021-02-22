# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        if not root: return 0
        totalSum = 0
        def traverseAndAccumulate(node, currPath):
            nonlocal totalSum
            
            if node.left is None and node.right is None:
                totalSum += int("".join(currPath + [str(node.val)]))
                
            if node.left: traverseAndAccumulate(node.left, currPath + [str(node.val)])
            if node.right: traverseAndAccumulate(node.right, currPath + [str(node.val)])
                
        
        traverseAndAccumulate(root, [])
        return totalSum
