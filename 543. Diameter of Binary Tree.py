# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        longestDiameter = 0
        
        def depth(node):
            if not node: return 0
            nonlocal longestDiameter
            leftDepth = depth(node.left)
            rightDepth = depth(node.right)
            
            longestDiameter = max(longestDiameter, leftDepth + rightDepth)
            return 1 + max(leftDepth, rightDepth)
        
        depth(root)
        return longestDiameter
