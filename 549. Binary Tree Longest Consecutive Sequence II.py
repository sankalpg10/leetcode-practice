# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestConsecutive(self, root: TreeNode) -> int:
        
        def traverseAndFind(node):
            if not node: return (0, 0)
            inc, dec = 1, 1
            if node.left is not None:
                linc, ldec = traverseAndFind(node.left)
                if node.val == node.left.val + 1:
                    dec = ldec + 1
                elif node.val == node.left.val - 1:
                    inc = linc + 1
            
            if node.right is not None:
                rinc, rdec = traverseAndFind(node.right)
                if node.val == node.right.val + 1:
                    dec = max(dec, rdec + 1)
                elif node.val == node.right.val - 1:
                    inc = max(inc, rinc + 1)
                    
            nonlocal maxval
            maxval = max(maxval, dec + inc - 1)
            return (inc, dec)
            
            
        maxval = 0
        traverseAndFind(root)
        return maxval
