# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:
        
        
        def deepDive(node):
            if not node: return (None, 0)
            left, right = deepDive(node.left), deepDive(node.right)
            if left[1] > right[1]: return (left[0], left[1]+1)
            if left[1] < right[1]: return (right[0], right[1]+1)
            
            return (node, left[1]+1)
        
        return deepDive(root)[0]
        
