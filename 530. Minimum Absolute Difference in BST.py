# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: TreeNode) -> int:
        
        prev = None
        res = inf
        
        
        def traverse(node):
            if not node: return
            nonlocal prev, res
            traverse(node.left)
            if prev != None: res = min(res, node.val - prev)
            prev = node.val
            traverse(node.right)
            
        traverse(root)
        return res
            
