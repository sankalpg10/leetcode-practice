# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        pathtop = self.getPath(root, p)
        pathtoq = self.getPath(root, q)
        if len(pathtop) > len(pathtoq): i, j = len(pathtop) - len(pathtoq), 0
        else:  i, j = 0, len(pathtoq) - len(pathtop)
        while i < len(pathtop) and j < len(pathtoq):
            if pathtop[i] == pathtoq[j]:
                return pathtop[i]
            i += 1
            j += 1
        
        return pathtop[i-1]
    
    def getPath(self, root, node):
        if not root:
            return
        if root.val == node.val:
            return [root]
        
        left = self.getPath(root.left, node)
        
        if left:
            left.append(root)
            return left
        right = self.getPath(root.right, node)
        if right:
            right.append(root)
            return right
        
        return
        
