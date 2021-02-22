# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        
        depthX = 0
        depthY = 0
        parentX = None
        parentY = None
        
        def traverse(node, currDepth, parent):
            if not node: return
            nonlocal depthX, depthY, parentX, parentY
            if node.val == x:
                depthX = currDepth
                parentX = parent
                
            if node.val == y:
                depthY = currDepth
                parentY = parent
                
            traverse(node.left, currDepth+1, node)
            traverse(node.right, currDepth+1, node)
               
        traverse(root, 1, None)
        return depthX == depthY and parentX != parentY
            
