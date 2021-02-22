# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        currSum = 0
        
        def traverse(node):
            if not node: return
            nonlocal currSum
            
            traverse(node.right)
            
            currSum += node.val
            node.val = currSum
            
            traverse(node.left)
            
        traverse(root)
        return root
